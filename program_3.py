#Programmer: Alethea Lo
#Date: 2/13/25
#Title: Average Rainfall

def main():
    total_rainfall = 0
    total_months = 0

    try:
        years = int(input("Enter the number of years: "))
        if years <= 0:
            print("Please enter a positive number of years.")
            return

        for year in range(1, years + 1):
            print(f"Year {year}")
            for month in range(1, 13):
                while True:
                    try:
                        rainfall = float(input(f"Enter inches of rainfall for month {month}: "))
                        if rainfall < 0:
                            print("Rainfall cannot be negative. Please enter a valid amount.")
                        else:
                            total_rainfall += rainfall
                            break
                    except ValueError:
                        print("Invalid input. Please enter a numerical value.")

                total_months += 1

        average_rainfall = total_rainfall / total_months

        print("\nRainfall Statistics:")
        print(f"Total months: {total_months}")
        print(f"Total inches of rainfall: {total_rainfall:.2f}")
        print(f"Average rainfall per month: {average_rainfall:.2f} inches")

    except ValueError:
        print("Invalid input. Please enter a valid number of years.")


if __name__ == "__main__":
    main()
