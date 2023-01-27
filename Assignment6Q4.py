string=str(input("Enter the string:"))
string=string.lower()
count=0
for i in range(26):
    if (chr(97+i) in string):
        count=count+1
if count==26:
    print("Entered string is a pangram.")
else:
    print("Entered string is not a pangram.")
