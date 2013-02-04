#!/usr/bin/env python
import sys
import subprocess

import os
import os.path

directory = None
s = subprocess.Popen(['./AnimEncoderCapture.py'], stdout=subprocess.PIPE)
while True:
    line = s.stdout.readline()
    if not line:
        break
    if not 'ob = ' in line:
        continue
    directory = line.replace('\n','').replace('ob = ', '').encode('utf-8')

s = subprocess.Popen([u'python', u'anim_encoder/capture.py', 'directory'], stdout=subprocess.PIPE)
while True:
    line = s.stdout.readline()
    if not line:
        break
    print line
