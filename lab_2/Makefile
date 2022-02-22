generate:
	python rsa_genkey.py 13 101

example:
	echo "SECRET MESSAGE TO WORLD!!!" > example.msg

encrypt: example
	python rsa_encoder.py example.msg --output encoded.msg

decrypt:
	python rsa_decoder.py encoded.msg --output decoded.msg

run: clean generate example encrypt decrypt

clean:
	rm -f *.msg > /dev/null
	rm -f *.key > /dev/null
