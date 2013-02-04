"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['AnimEncoder.py']
DATA_FILES = ['anim_encoder','AnimEncoderCapture.py','AnimEncoderRender.py','Pashua.py','Pashua.app']
OPTIONS = {'argv_emulation': False }

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
