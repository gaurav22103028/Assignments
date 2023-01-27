string=str(input("Enter a string:"))
string=string.lower()
if(string==string[::-1]):
    print("Number is a palindrome")
else:
    print("Number is not a palindrome.")