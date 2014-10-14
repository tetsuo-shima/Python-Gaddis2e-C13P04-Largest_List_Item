__author__ = 'dwight'

# Design a function that accepts a list as an argument, and returns the largest value in the list. The function should
# use recursion to find the largest item.

import random


def main():
    num_list = generate_random_value_list(10)
    print('Number List:', num_list)
    print('Largest Value:', largest_item_in_list(num_list))


def generate_random_value_list(length):
    num_list = []
    for index in range(length):
        value = random.randint(1, 100)
        num_list.append(value)

    return num_list


def largest_item_in_list(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return max(num_list[0], largest_item_in_list(num_list[1:]))


main()

