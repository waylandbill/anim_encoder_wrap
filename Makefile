all:
	python setup.py py2app 
	chmod +x dist/AnimEncoder.app/Contents/Resources/AnimEncoder.py
	chmod +x dist/AnimEncoder.app/Contents/Resources/AnimEncoderCapture.py
	chmod +x dist/AnimEncoder.app/Contents/Resources/AnimEncoderRender.py
	chmod +x dist/AnimEncoder.app/Contents/Resources/anim_encoder/capture.py

clean:
	rm -rf build dist
