def Is_Pangram(string):
    count = 0
    for i in range(26):
        if (chr(97 + i) in string):
            count = count + 1
    return(count)
string = str(input("Enter the string:"))
string = string.lower()
string = string.replace(" ","")
count=Is_Pangram(string)
if count == 26:
    print("Entered string is a pangram.")
else:
    print("Entered string is not a pangram.")
