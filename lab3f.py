#!/usr/bin/env python3

# Author ID: mjvelota

my_list = [1, 2, 3, 4, 5]

def add_item_to_list(ordered_list):
	LastNum = ordered_list[-1]
	ordered_list.append(LastNum + 1)

def remove_items_from_list(ordered_list, items_to_remove):
	for item in items_to_remove:
		ordered_list.remove(item)
if __name__ == '__main__':
    print(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    print(my_list)
    remove_items_from_list(my_list, [1,5,6])
    print(my_list)

