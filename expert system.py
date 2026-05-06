# Information Management Expert System

database = {}

def add_information():
    key = input("Enter Name: ")
    value = input("Enter Information: ")

    database[key] = value

    print("Information Added Successfully!\n")


def search_information():
    key = input("Enter Name to Search: ")

    if key in database:
        print("Information Found:")
        print(key, ":", database[key])
    else:
        print("No Record Found!")

    print()


def display_information():

    if len(database) == 0:
        print("Database is Empty!\n")
        return

    print("\nStored Information:")

    for key, value in database.items():
        print(key, ":", value)

    print()


def delete_information():
    key = input("Enter Name to Delete: ")

    if key in database:
        del database[key]
        print("Record Deleted Successfully!")
    else:
        print("Record Not Found!")

    print()


while True:

    print("===== Information Management Expert System =====")
    print("1. Add Information")
    print("2. Search Information")
    print("3. Display All Information")
    print("4. Delete Information")
    print("5. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        add_information()

    elif choice == 2:
        search_information()

    elif choice == 3:
        display_information()

    elif choice == 4:
        delete_information()

    elif choice == 5:
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!\n")



# Airline Scheduling and Cargo Expert System

# Flight database
flights = [
    {
        "flight_no": "AI101",
        "destination": "Delhi",
        "capacity": 1000,   # in kg
        "departure": "10:00 AM"
    },
    {
        "flight_no": "AI202",
        "destination": "Mumbai",
        "capacity": 1500,
        "departure": "01:00 PM"
    },
    {
        "flight_no": "AI303",
        "destination": "Bangalore",
        "capacity": 1200,
        "departure": "06:00 PM"
    }
]

# Function to find suitable flight
def allocate_cargo(destination, cargo_weight):

    suitable_flights = []

    for flight in flights:

        # Rule 1: Destination must match
        if flight["destination"].lower() == destination.lower():

            # Rule 2: Capacity should be enough
            if flight["capacity"] >= cargo_weight:
                suitable_flights.append(flight)

    # Inference Engine Decision
    if suitable_flights:

        print("\nSuitable Flight Found:\n")

        for flight in suitable_flights:
            print("Flight No :", flight["flight_no"])
            print("Destination :", flight["destination"])
            print("Departure :", flight["departure"])
            print("Available Capacity :", flight["capacity"], "kg")
            print("-" * 30)

    else:
        print("\nNo suitable flight available for the cargo.")


# Main Program
print("=== Airline Scheduling and Cargo Expert System ===")

destination = input("Enter Cargo Destination: ")
cargo_weight = int(input("Enter Cargo Weight (kg): "))

allocate_cargo(destination, cargo_weight)








