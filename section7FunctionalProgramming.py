
#Example of a pure function. No outside interaction and no side effects.
#map, filter, zip and reduce
from functools import reduce
"""my_list = [1,2,3]

def multiply_by2(item):
    return item*2

def only_odd(item):
    return item % 2 != 0

def accumulator(acc, item):
    print(acc, item)
    return acc + item

print(reduce(accumulator, my_list, 0))
print(list(filter(only_odd, my_list)))
print(my_list)
"""
"""# 145. Exercise
#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']
def capitalize(item):
    return item.upper()

print(list(map(capitalize, my_pets)))

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

print(list(zip(my_strings, sorted(my_numbers))))

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]
def passed(item):
    return item > 50

print(list(filter(passed, scores)))

#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
def accumulate(acc, item1):
    return acc + item1

print(reduce(accumulate, (my_numbers + scores)))"""

"""#146. Lambda expressions
#lambda param: action(param)

my_list = [1,2,3]

print(list(map(lambda item: item*2, my_list)))
print(list(filter(lambda item: item % 2 != 0, my_list)))
print(reduce(lambda acc, item: acc + item, my_list))
print(my_list)"""

"""# 147. Exercise, Lambda expressions.
my_list = [5,4,3]
#Square
print(list(map(lambda item: item**2, my_list)))

#List sorting
a = [(0,2), (4,3), (9,9), (10,-1)]
a.sort(key = lambda item: item[-1])
print(a)"""

"""# 149 Dict and set comprehension
my_dict = {num:num*2 for num in [1,2,3]}
print(my_dict)"""

# 150. Exercise Comprehensions
some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]

duplicates = list({item for item in some_list if some_list.count(item) > 1})
print(duplicates)