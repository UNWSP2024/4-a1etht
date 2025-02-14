#Programmer: Alethea Lo
#Date: 2/13/25
#Title: Pseudocode for Budget Analysis

#BEGIN OF PROGRAM
DISPLAY "Enter your budget for the month:"
INPUT budget

IF budget < 0 THEN
    DISPLAY "Budget cannot be negative."
    EXIT PROGRAM
ENDIF

SET total_expenses=0

#If true
DISPLAY "Enter an expense amount (or type 'done' to finish):"
INPUT expense

IF expense == "done" THEN
    BREAK

#CONVERT expense TO FLOAT

IF expense <0 THEN
    DISPLAY "Expense cannot be negative. Please enter a valid amount."
ELSE
    total_expense=total_expenses+expense


#Endwhile
SET difference = budget = total_expenses

DISPLAY "Budget Summary:"
DISPLAY "Total budget: $", budget
DISPLAY "Total expenses: $", total_expenses

IF difference > 0 THEN
    DISPLAY "You are under budget by $", difference
ELSE IF difference < 0 THEN
  DISPLAY "You are over budget by $", -difference
    ELSE
        DISPLAY "You have exactly met your budget."
    ENDIF
#END OF PROGRAM