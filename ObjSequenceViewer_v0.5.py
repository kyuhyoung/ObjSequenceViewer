import pygame
import easygui
from pygame.locals import *

from pygame.time import Clock as clk
from OpenGL.GL import *
from OpenGL.GLU import *

import math
import pywavefront
from pywavefront import visualization
import numpy as np
import random
import os

wireframe=False

white=GLfloat_3(1,1,1)
black=GLfloat_3(0,0,0)
red=GLfloat_3(1,0,0.0)

pygame.init()

display = (1024, 768)
scree = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

glEnable(GL_DEPTH_TEST)
glEnable(GL_LIGHTING)
glShadeModel(GL_SMOOTH)
glEnable(GL_COLOR_MATERIAL)
glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)


glEnable(GL_LIGHT0)
glLightfv(GL_LIGHT0, GL_AMBIENT, [0.2, 0.2, 0.2, 1])
glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.8, 0.8, 1.0, 1])



glEnable(GL_FOG)
fogColor = [0.3, 0.3, 1.0, 1.0]

global fogMode
fogMode = GL_EXP
glFogi (GL_FOG_MODE, GL_EXP2)
glFogfv (GL_FOG_COLOR, fogColor)
glFogf (GL_FOG_DENSITY, 0.01)
glHint (GL_FOG_HINT, GL_DONT_CARE)
glFogf (GL_FOG_START, 1500.0)
glFogf (GL_FOG_END, 1550.0)
glClearColor(0.5, 0.5, 0.5, 1.0)

   

glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(45, (display[0]/display[1]), 0.1, 100.0)
#gluOrtho2D(0.0,1024.0,0.0,768.0)
glMatrixMode(GL_MODELVIEW)
gluLookAt(50, 0, 20, 0, 0, 0, 0, 0, 1)
viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
glLoadIdentity()


# init mouse movement and center mouse on screen
displayCenter = [scree.get_size()[i] // 2 for i in range(2)]
mouseMove = [0, 0]
pygame.mouse.set_pos(displayCenter)

path = easygui.diropenbox()
path+=os.sep
model_files=os.listdir(path)
max_num_of_models=len(model_files)

scenes=[]

scene_scale1=[]
scene_trans1=[]
for n,f in enumerate(model_files):
    scenes.append(pywavefront.Wavefront(path+f, collect_faces=True))
    print ("Loaded ", n ,"/", len(model_files))
    scene_box = (scenes[n].vertices[0], scenes[n].vertices[0])
    for vertex in scenes[n].vertices:
        min_v = [min(scene_box[0][i], vertex[i]) for i in range(3)]
        max_v = [max(scene_box[1][i], vertex[i]) for i in range(3)]
        scene_box = (min_v, max_v)

    scene_size     = [scene_box[1][i]-scene_box[0][i] for i in range(3)]
    max_scene_size = max(scene_size)
    scaled_size    = 5
    scene_scale1=[scaled_size/max_scene_size for i in range(3)]
    scene_trans1=[-(scene_box[1][i]+scene_box[0][i])/2 for i in range(3)]

    if n==max_num_of_models:
        break
    
permantent_rotation1=0
def Model1(scene_index):
    glPushMatrix()
    glRotatef(90,1,0,0)
    global permantent_rotation1
    glRotatef(permantent_rotation1,0,1,0)
    
    glScalef(*scene_scale1)
    glTranslatef(*scene_trans1)
    
    glColor3fv(white)
    glEnable( GL_POLYGON_OFFSET_FILL )
    
    visualization.draw(scenes[scene_index])
    glPopMatrix()

motionBlurFrames=5
rotateModels=0
up_down_angle = 0.0
paused = False
run = True
initTime=pygame.time.get_ticks()
frames_passed=0
model_index=0
while run:
    pastTime=pygame.time.get_ticks()-initTime
    #if pastTime>10000:
        #rotateModels+=0.008
        
    for event in pygame.event.get():


        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and not paused :
            initTime=pygame.time.get_ticks()
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                run = False
            if event.key == pygame.K_f:
                wireframe= not wireframe
            

    # get keys
    keypress = pygame.key.get_pressed()
    glClearColor(0.0, 0.0, 0.0, 0.5)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
      
    # init model view matrix
    glLoadIdentity()


    # init the view matrix
    glPushMatrix()
    glLoadIdentity()

    # apply the movment
    if keypress[pygame.K_w]:
        glTranslatef(0,0,0.05)
    if keypress[pygame.K_s]:
        glTranslatef(0,0,-0.05)
    if keypress[pygame.K_d]:
        
        rotateModels+=0.2
    
    if keypress[pygame.K_a]:
        rotateModels-=0.2


    # multiply the current matrix by the get the new view matrix and store the final vie matrix 
    glMultMatrixf(viewMatrix)
    viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)

    # apply view matrix
    glPopMatrix()
    glMultMatrixf(viewMatrix)

    glLightfv(GL_LIGHT0, GL_POSITION, [1, -1, 1, 0])

    glPushMatrix()
    glRotatef(rotateModels,0,0,1)



    glPushMatrix()
    glTranslatef(1, 0, 0)
    glTranslatef(0, 1, 0)

    if wireframe == True:
        glPolygonMode(GL_FRONT_AND_BACK,GL_LINE)
    else:
        glPolygonMode(GL_FRONT_AND_BACK,GL_FILL)
    #Draw the object here
    #glPolygonMode(GL_FRONT_AND_BACK,GL_FILL)

    if model_index == max_num_of_models:
        model_index=0
    if (pygame.time.get_ticks()-initTime) % 5 == 0:
        #pastTime=0
        model_index+=1
        print(model_index)
    if(len(scenes)<=model_index):
        model_index=0
    Model1(model_index)
    glPopMatrix()

    glPopMatrix()


    frames_passed+=1

    pygame.display.flip()

pygame.quit()
