#!/usr/bin/python2.6

#
# USAGE INFORMATION:
# As you can see this text, you obviously have opened the file in a text editor.
# 
# If you would like to *run* this example rather than *read* it, you
# should open Terminal.app, drag this document's icon onto the terminal
# window, bring Terminal.app to the foreground (if necessary) and hit return.
# 

import Pashua
import os.path

conf = """
# Set transparency: 0 is transparent, 1 is opaque
*.transparency=0.95

# Set window title
*.title = Capture Dialog

# Introductory text
txt.type = text
txt.default = Capture Running...
txt.height = 276
txt.width = 310
txt.x = 0
txt.y = 44

b.type = defaultbutton
b.label = Stop Capture

"""

# Set the images' paths relative to this file's path / 
# skip images if they can not be found in this file's path
icon  = os.path.dirname(__file__) + '/.icon.png'
bgimg = os.path.dirname(__file__) + '/.demo.png'
if os.path.exists(icon):
	# Display Pashua's icon
	conf += "img.type = image\nimg.x = 530\nimg.y = 255\nimg.path = %s\n" % (icon)
if os.path.exists(bgimg):
	# Display Pashua's icon
	conf += "bg.type = image\nbg.x = 30\nbg.y = 2\nbg.path = %s\n" % (bgimg)


Result = Pashua.run(conf)

for Key in Result.keys():
    print "%s = %s" % (Key, Result[Key])

