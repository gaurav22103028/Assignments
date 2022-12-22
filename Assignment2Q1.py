# a. Find the length of the input string.
text = 'Python is a case sensitive language'
print ("The length of the input string:", len(text))

# b. Reverse the order of the string in one line code.
reverse = text[::-1]
print("String in Reverse Order: ", reverse)

# c. Using Slice function store “a case sensitive” in new string.
slice_obj = slice(10,26)
print(text[slice_obj])

#d. Replace “a case sensitive” with “object oriented”.
print(text.replace('a case sensitive','object oriented'))

#e. Find index of substring “a” in the given input string.
print("Index of substring a in the given input string", text.index("a"))

#f. Remove the white spaces from the given input string.
removeSpace=text.replace(" ", "")
print(removeSpace)