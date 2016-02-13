
MotionMeerkat
-----------------------------

MotionMeerkat is a standalone python executable that identifies candidate motion events of interest from an extensive video stream. After running a video through MotionMeerkat, the user can review a folder of candidate motion frames for the target organism. This tool greatly reduces the time needed to review videos and is flexible to a variety of video inputs.  The python source code is also available online for more advanced users.  

This repos is MotionMeerkat_Bisque, which is the source Repo for MotionMeerkat for Bisque Directory

Executable can be found here: http://benweinstein.weebly.com/motionmeerkat.html

README - Ben Weinstein Stony Brook University

BISQUE Development of Motion Detection Module - MotionMeerkat

MotionMeerkat.py  : Core script which takes in video, user specified sensitivity and returns folder full of jpegs

runtime-module.cfg: How the runtime should handle the module under command and condor platforms

MotionMeerkat.xml : The module description for BISQUE

public/           : Resources for BISQUE to show the module 

README			  : This file description dev/ folder contents

setup.py          : compile the module for condor exec (not needed for local command)

Bisque service engine: http://rogers.iplantcollaborative.org:11110/engine_service

