#!/usr/bin/python2.6
import sys
import subprocess

import os
import os.path
from anim_encoder import capture, anim_encoder

directory = None
s = subprocess.Popen(['./AnimEncoderCapture.py'], stdout=subprocess.PIPE)
while True:
    line = s.stdout.readline()
    if not line:
        break
    if not 'ob = ' in line:
        continue
    directory = line.replace('\n','').replace('ob = ', '').encode('utf-8')

proc = subprocess.Popen([u'python', u'anim_encoder/capture.py', 'directory'], shell=True, close_fds=True)

s = subprocess.Popen(['./AnimEncoderStop.py'], stdout=subprocess.PIPE)
while True:
    line = s.stdout.readline()
    if not line:
        break

os.kill(proc.pid, 1)

s = subprocess.Popen(['./AnimEncoderRender.py'], stdout=subprocess.PIPE)
while True:
    line = s.stdout.readline()
    if not line:
        break
    if not 'ob = ' in line:
        continue
    filename = line.replace('\n','').replace('ob = ', '').encode('utf-8')

