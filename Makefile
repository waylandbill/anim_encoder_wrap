all:
	/usr/bin/python2.6 setup.py py2app 
	chmod +x dist/AnimEncoder.app/Contents/Resources/AnimEncoder.py
	chmod +x dist/AnimEncoder.app/Contents/Resources/AnimEncoderCapture.py
	chmod +x dist/AnimEncoder.app/Contents/Resources/AnimEncoderRender.py
	chmod +x dist/AnimEncoder.app/Contents/Resources/anim_encoder/capture.py
	#cp -R /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/ dist/AnimEncoder.app/Contents/Resources/
	#rm -r dist/AnimEncoder.app/Contents/Resources/*.pyc
clean:
	rm -rf build dist
