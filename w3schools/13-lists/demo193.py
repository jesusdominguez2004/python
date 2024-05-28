# W3Schools, Python Lists, List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [expression for item in iterable]
newlist = [x.upper() for x in fruits]

print(newlist)
