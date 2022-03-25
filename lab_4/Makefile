example:
	echo "xsdfhkj.ghmserdnjvcdfyk" > .key
	echo "Hello world!!!" > example.msg

encrypt:
	python app.py -K .key -M example.msg -O encrypt.msg -E

decrypt:
	python app.py -K .key -M encrypt.msg -O decrypt.msg -D

run: clean encrypt decrypt encrypt

clean:
	clear
	rm -f .key > /dev/null
	rm -f *.msg > /dev/null