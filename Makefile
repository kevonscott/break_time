clean:
	if exist dist rmdir /S /Q dist
	if exist build rmdir /S /Q build
	if exist breaktime.spec del breaktime.spec
