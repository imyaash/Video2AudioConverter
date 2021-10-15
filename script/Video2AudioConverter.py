# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 10:16:35 2021

@author: imyaash
"""

import moviepy.editor as mp

# Video to Audio Converter
print("Video to Audio Converter")
print("Enter Video Path:")
address = input()
audio = mp.VideoFileClip(address)
audio.audio.write_audiofile("Audio.mp3")
print("Change Audio File Name Immediately.....")
