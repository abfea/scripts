BIN=${HOME}/.local/bin

install:
	# dirs
	mkdir ${BIN}/assets
	# links	
	ln epush.py ${BIN}/epush
	ln assets/token ${BIN}/assets/token
	ln assets/vocabulary ${BIN}/assets/vocabulary
uninstall:
	# rm links
	rm ${BIN}/epush
	rm ${BIN}/assets/token
	rm ${BIN}/assets/vocabulary
	# rmdir
	rm ${BIN}/assets
