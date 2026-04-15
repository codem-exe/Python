# List Comprehension = A concise way to create lists in Python
#                      Compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]

# doubles = []
# for x in range(1,11):
#     doubles.append(x * 2)
#
# print(doubles)


##### [expression for value in iterable if condition]

doubles = [x * 2 for x in range(1,11)]
triples = [x * 3 for x in range(1,11)]
squares = [x * x for x in range(1,11)]
print(doubles)
print(triples)
print(squares)


# ///Strings
fruits = ["apple","orange","banana","coconut"]
fruits = [fruit.upper() for fruit in fruits]
print(fruits)

# ///Conditional Statement
numbers = [1, -2, 3, -4, 5, -6]
positive_nums = [ num for num in numbers if num>= 0]
negative_nums = [ num for num in numbers if num<= 0]
print(positive_nums)
print(negative_nums)


nums = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
even_num = [num for num in nums if num % 2 == 0]
odd_num = [num for num in nums if num % 2 != 0]
print(even_num)
print(odd_num)
