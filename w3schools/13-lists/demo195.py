# W3Schools, Python Lists, List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [expression if condition == True else expression for item in iterable]
newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)
