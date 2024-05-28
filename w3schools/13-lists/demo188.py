# W3Schools, Python Lists, List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [expression for item in iterable if condition == True]
newlist = [x for x in fruits if "a" in x]

print(newlist)
