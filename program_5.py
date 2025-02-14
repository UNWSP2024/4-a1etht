#Programmer: Alethea Lo
#Date: 2/13/25
#Title: Bank Balance
def main():
    try:
        budget = float(input("Enter your budget for the month: "))
        if budget < 0:
            print("Budget cannot be negative.")
            return

        total_expenses = 0
        while True:
            try:
                expense = input("Enter an expense amount (or type 'done' to finish): ")
                if expense.lower() == 'done':
                    break

                expense = float(expense)
                if expense < 0:
                    print("Expense cannot be negative. Please enter a valid amount.")
                else:
                    total_expenses += expense
            except ValueError:
                print("Invalid input. Please enter a numerical value.")

        difference = budget - total_expenses

        print("\nBudget Summary:")
        print(f"Total budget: ${budget:.2f}")
        print(f"Total expenses: ${total_expenses:.2f}")
        if difference > 0:
            print(f"You are under budget by ${difference:.2f}.")
        elif difference < 0:
            print(f"You are over budget by ${-difference:.2f}.")
        else:
            print("You have exactly met your budget.")

    except ValueError:
        print("Invalid input. Please enter a numerical value for the budget.")


if __name__ == "__main__":
    main()
