#Programmer: Alethea Lo
#Date: 2/13/25
#Title: Movie tix counter
def main():
    total_tickets = 0

    while True:
        movie_name = input("Enter the movie name (or type 'done' to finish): ")
        if movie_name.lower() == 'done':
            break

        try:
            tickets = int(input(f"How many tickets do you want for '{movie_name}'? "))
            if tickets < 0:
                print("Please enter a positive number of tickets.")
                continue
            total_tickets += tickets
        except ValueError:
            print("Invalid input. Please enter a valid number of tickets.")

    print(f"Total number of tickets desired: {total_tickets}")


if __name__ == "__main__":
    main()
