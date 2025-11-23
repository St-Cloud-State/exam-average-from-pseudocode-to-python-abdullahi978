"""
Full Name: Abdullahi Ahmed
Class-Section: IS 250-01
Assignment Title: Calculate Average of Three Scores
Submission Date: 11/23/2025
"""
"""
START
ASK THE USER FOR THE FIRST EXAM SCORE
STORE SCORE IN VARIABLE 

ASK THE USER FOR THE SECOND EXAM SCORE
STORE SCORE IN VARIABLE 

ASK THE USER FOR THE THIRD EXAM SCORE
STORE SCORE IN VARIABLE 

DEFINE FUNCTION calculate_average(s1,s2,s3)
    CALCULATE AVG: (s1 + s2 + s3) / 3
    RETURN result 
END FUNCTION 

CALL calculate_average(s1,s2,s3)
STORE result in average variable 

PRINT the string: "First score: ..." and score1
PRINT the string: "Second score: ..." and score2
PRINT the string: "Third score: ..." and score3
PRINT the string: "The average score: ..." and average
"""

# Your Python code begins below this line.
# Get the first score
score1 = float(input("Enter first score: "))
# Get the second score
score2 = float(input("Enter second score: "))
# Get the third score
score3 = float(input("Enter third score: "))

#Define the function
def calculate_average(s1,s2,s3):
    #return the average
    return (s1 + s2 + s3) / 3
# assign the average variable to the function
average = calculate_average(score1,score2,score3)
#Print the first score
print("First score: ", score1)
#Print the second score
print("Second score: ", score2)
#Print the third score
print("Third score: ", score3)
#Print the average
print(f"The average score is: {average:.2f}")
# Every line you write must have a comment directly above it.

# Call your function when your program is ready
#call the function using keyword parameters to connect the parameters to the variables
calculate_average(s1=score1,s2=score2,s3=score3)

