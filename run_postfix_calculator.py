from calculate import *

while True:
	tokens = []
	tokens = input_and_tokenise(tokens)
	stack = []
	
	if "q" in tokens:
		break
	else:
		print_answer(tokens, stack)
