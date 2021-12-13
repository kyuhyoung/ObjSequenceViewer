# ObjSequenceViewer V0.5
A minimal, standalone viewer for 3D animations stored as stop-motion sequences of individual .obj mesh files.

<p align="center">
<img src="sample_videos/solid.gif" width="200"><img src="sample_videos/wireframe.gif" width="200">
</p>

<b> Installation: </b>

 - pip3 install -r requirements.txt

<b> Execution: </b>

 - python3 ObjSequenceViewer_v0.5.py

After the program starts, you will be asked to specify the directory that the sequence of .obj meshes resides in (files need to be named in a consecutive manner).

All .obj meshes need to be loaded in RAM before the animation starts, which can be a time consuming process.

Tested on Ubuntu 20.04 and Windows 10.

<b> KeyBoard Controls: </b>

- Rotate left: A button
- Rotate right: D button
- Zoom in: W button
- Zoom out: S button
- Toggle solid/wireframe view: F button

<b>Output Recording: </b>

 - Use a screen capturing program (e.g., vokoscreen - https://github.com/vkohaupt/vokoscreenNG)

<b>TODO: </b>
 - Add sliders for controling animation speed
 - Add texture support
 - Control background color
 - Reduce loading time through parallelization
