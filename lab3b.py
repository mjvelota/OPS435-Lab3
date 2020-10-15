#!/usr/bin/env python3

# Author ID: mjvelota

def sum_numbers(number1, number2):
	number3 = number1 + number2
	return int(number3)

def subtract_numbers(number1, number2):
	number3 = number1 - number2
	return int(number3)

def multiply_numbers(number1, number2):
	number3 = number1 * number2
	return int(number3)
	
if __name__ == '__main__':
	print(sum_numbers(10, 5))
	print(subtract_numbers(10, 5))
	print(multiply_numbers(10, 5)) 
