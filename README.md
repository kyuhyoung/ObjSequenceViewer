# ObjSequenceViewer V0.5
A minimal viewer for 3D temporal mesh sequences, stored as collections of individual .obj meshes.

<p align="center">
<img src="sample_videos/solid.gif" width="200"><img src="sample_videos/wireframe.gif" width="200">
</p>

Installation:
pip3 install -r requirements.txt

<b> Execution: </b>

 - python3 ObjSequenceViewer_v0.5.py

After the program starts, you can specify the directory that the sequence of .obj meshes resides in (files need to be named in a sequential manner).
All .obj files need to be loaded in RAM before the animation starts.

Tested on Ubuntu 20.04.

<b> KeyBoard and Mouse Controls: </b>

- Rotate right: J button
- Rotate left: L button
- Zoom in: Scroll Up
- Zoom out: Scroll Down
- Toggle solid/wireframe views: F button

(If keyboard controls do not work, check capitalization.)
