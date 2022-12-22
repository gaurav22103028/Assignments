grade = int (input("Enter a grade between 4 and 10: "))
if grade < 4 or grade > 10:
    print("Bad grade. Enter a grade between 4 and 10")
else:
    if grade == 10:
        Letter_Grade = 'A+'
        Performance = 'Outstanding'
    elif grade == 9:
        Letter_Grade = 'A'
        Performance = 'Excellent'
    elif grade == 8:
        Letter_Grade = 'B+'
        Performance = 'Very Good'
    elif grade == 7:
        Letter_Grade = 'B'
        Performance = 'Good'
    elif grade == 6:
        Letter_Grade = 'C+'
        Performance = 'Average'
    elif grade == 5:
        Letter_Grade = 'C'
        Performance = 'Below Average'
    elif grade == 4:
        Letter_Grade = 'D'
        Performance = 'Poor'
print("Your Grade is {} and {} Performance.".format(Letter_Grade, Performance))