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
txt.default = Capture in Progress
txt.height = 50
txt.width = 310
txt.x = 5
txt.y = 44

# Add a text field
#tf.type = textfield
#tf.label = Save Filename
#tf.default = capture.out
#tf.width = 310

b.type = defaultbutton
b.label = Stop Capture

# Add a filesystem browser
#ob.type = openbrowser
#ob.label = Capture Directory
#ob.filetype = directory
#ob.width=310
#ob.tooltip = Capture Directory

# Define radiobuttons
#rb.type = radiobutton
#rb.label = Example radiobuttons
#rb.option = Radiobutton item #1
#rb.option = Radiobutton item #2
#rb.option = Radiobutton item #3
#rb.option = Radiobutton item #4
#rb.default = Radiobutton item #2

# Add a popup menu
#pop.type = popup
#pop.label = Example popup menu
#pop.width = 310
#pop.option = Popup menu item #1
#pop.option = Popup menu item #2
#pop.option = Popup menu item #3
#pop.default = Popup menu item #2

# Add a checkbox
#chk1.type = checkbox
#chk1.label = Pashua offers checkboxes, too
#chk1.rely = -18
#chk1.default = 1

# Add another one
#chk2.type = checkbox
#chk2.label = But this one is disabled
#chk2.disabled = 1

# Add a cancel button with default label
#cb.type=cancelbutton

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

print "Pashua returned the following dictionary keys and values:"

for Key in Result.keys():
    print "%s = %s" % (Key, Result[Key])

print
