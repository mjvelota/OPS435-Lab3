#!/usr/bin/env python3

# Author ID: mjvelota

def operate(number1, number2, operator):
	if operator == 'add':
		number3 = number1 + number2
		return int(number3)
	elif operator == 'subtract':
		number3 = number1 - number2
		return int(number3)
	elif operator == 'multiply':
		number3 = number1 * number2
		return int(number3)
	else:
		return 'Error: function operator can be "add", "subtract", or "multiply"'

if __name__ == '__main__':
	print(operate(10, 5, 'add'))
	print(operate(10, 5, 'subtract'))
	print(operate(10, 5, 'multiply'))
	print(operate(10, 5, 'divide'))
