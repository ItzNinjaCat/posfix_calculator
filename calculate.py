from Validate import *

def number_check(num):
	try:
		int(num)
		return True
	except:
		return False

def populate_stack_and_calculate(stack, tokens):
	try:
		for i in tokens:
			if i in operations:
				if len(inspect.signature(operations[i]).parameters) == 1:
					stack.append(operations[i](stack.pop(-1)))
				elif len(inspect.signature(operations[i]).parameters) == 2:
					stack.append(operations[i](stack.pop(-1), stack.pop(-1)))
			elif number_check(i):
				stack.append(i)
			elif i in variables:
				stack.append(variables[i])
		return stack.pop()
	except:
		print("ERROR: Math error")
		return False

def print_answer(tokens, stack):
	if not validate(tokens):
		return
	answer = populate_stack_and_calculate(stack, tokens)
	if type(answer) != bool:
		print(answer) if answer != int(answer) else print(int(answer))