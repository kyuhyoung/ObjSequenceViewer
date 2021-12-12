# ObjSequenceViewer V0.5
A minimal viewer for 3D animations, stored as sequences of individual .obj mesh files.

<p align="center">
<img src="sample_videos/solid.gif" width="200"><img src="sample_videos/wireframe.gif" width="200">
</p>

<b> Installation: </b>

 - pip3 install -r requirements.txt

<b> Execution: </b>

 - python3 ObjSequenceViewer_v0.5.py

After the program starts, you will be asked to specify the directory that the sequence of .obj meshes resides in (files need to be named in a sequential manner).

All .obj meshes need to be loaded in RAM before the animation starts, which can be a time consuming process.

Tested on Ubuntu 20.04.

<b> KeyBoard and Mouse Controls: </b>

- Rotate left: J button
- Rotate right: L button
- Zoom in: Mouse scroll up
- Zoom out: Mouse scroll down
- Toggle solid/wireframe view: F button

(If keyboard controls do not work, check capitalization.)

<b>Output Recording: </b>

Use a screen capturing program (e.g., vokoscreen - https://github.com/vkohaupt/vokoscreenNG)
