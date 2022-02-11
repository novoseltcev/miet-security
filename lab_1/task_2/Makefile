SCRIPT=python simple_encrypt.py

generate:
	$(SCRIPT) --generate

example:
	echo "some_text" > example.txt

encrypt: example
	$(SCRIPT) -S example.txt -D encrypted_example.txt --encrypt

decrypt: encrypt
	$(SCRIPT) -S encrypted_example.txt -D decrypted_example.txt --decrypt

run: clean generate decrypt

clean:
	rm -f *.txt > /dev/null