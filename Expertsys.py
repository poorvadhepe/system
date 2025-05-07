def handle_request(service_type):
    if service_type == 'FLIGHT_BOOKING':
        source = input("Enter source city: ")
        destination = input("Enter destination city: ")
        tickets = int(input("How many tickets would you like to book? "))
        print(f"Your flight from {source} to {destination} has been booked for {tickets} ticket(s).")
        print("Check your email for the booking confirmation.\n")

    elif service_type == 'FLIGHT_STATUS':
        print("Please visit this link to track your flight: https://www.example.com/track-flight-status\n")

    elif service_type == 'BAGGAGE_INQUIRY':
        baggage_claim_no = int(input("Enter your baggage claim number: "))
        counter = 2 if baggage_claim_no % 2 == 0 else 3
        print(f"Please go to counter {counter} for baggage pickup.\n")

    elif service_type == 'CUSTOMER_FEEDBACK':
        feedback = input("Please enter your feedback: ")
        print("Thank you for your feedback! It helps us improve our services.\n")

    elif service_type == 'AIRLINE_SCHEDULE':
        flight_number = input("Enter the flight number to check the schedule: ")
        print(f"Flight {flight_number} is scheduled for 3 PM today.\n")

    elif service_type == 'CARGO_SCHEDULE':
        cargo_id = input("Enter the cargo ID to check the schedule: ")
        print(f"Cargo with ID {cargo_id} is scheduled for pickup at 5 PM today.\n")


def get_service_type_from_user():
    print("\nSelect a service:")
    print("1. Flight Booking")
    print("2. Flight Status")
    print("3. Baggage Inquiry")
    print("4. Customer Feedback")
    print("5. Airline Schedule")
    print("6. Cargo Schedule")

    try:
        choice = int(input("Choice: "))
    except ValueError:
        choice = 1

    service_map = {
        1: 'FLIGHT_BOOKING',
        2: 'FLIGHT_STATUS',
        3: 'BAGGAGE_INQUIRY',
        4: 'CUSTOMER_FEEDBACK',
        5: 'AIRLINE_SCHEDULE',
        6: 'CARGO_SCHEDULE'
    }

    return service_map.get(choice, 'FLIGHT_BOOKING')


def main():
    while True:
        print("\n-----------------------------------------------------")
        print("Welcome to the Airline Helpdesk!")
        print("-----------------------------------------------------")

        name = input("Enter your name: ")

        service_type = get_service_type_from_user()
        handle_request(service_type)

        choice = input("\nDo you want to continue? (y/n): ").strip().lower()
        if choice == 'n':
            print("Thank you for using the Airline Helpdesk. Goodbye!")
            break


if __name__ == "__main__":
    main()
