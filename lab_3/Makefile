decrypt:
	python bmp_decoder.py 7.bmp decoded.msg
	cat decoded.msg

example:
	cp 7.bmp example.bmp
	echo "Здесь был st-a-novoseltcev" > example.msg

encrypt: example
	python bmp_encoder.py example.msg example.bmp

check:
	python bmp_decoder.py example.bmp decoded2.msg
	cat decoded2.msg

run: clean decrypt encrypt

clean:
	clear
	rm -f *.msg > /dev/null
	rm -f example.bmp > /dev/null
