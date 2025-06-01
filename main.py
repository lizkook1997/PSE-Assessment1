from models.booking import Booking
from models.car import Car
from models.user import User

def main():
    while True:
        print("\n==== CAR RENTAL SYSTEM ====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            role = input("Enter your role (admin/customer): ")
            user = User(name, email, password, role)
            user.register()

        elif choice == '2':
            email = input("Email: ")
            password = input("Password: ")
            user_data = User.login(email, password)

            if user_data:
                user_id, role = user_data
                print(f"\nWelcome! Role: {role}")

                if role.strip().lower() == 'admin':
                    while True:
                        print("\n--- Admin Menu ---")
                        print("1. Add a New Car")
                        print("2. Approve Bookings")
                        print("3. Logout")
                        admin_choice = input("Choose an option: ")

                        if admin_choice == '1':
                            make = input("Make: ")
                            model = input("Model: ")
                            year = int(input("Year: "))
                            mileage = int(input("Mileage: "))
                            min_days = int(input("Minimum rental days: "))
                            max_days = int(input("Maximum rental days: "))
                            car = Car(make, model, year, mileage, min_days, max_days)
                            car.add()

                        elif admin_choice == '2':
                            pending = Booking.list_pending_bookings()
                            if not pending:
                                print("No pending bookings.")
                            else:
                                print("\nPending Bookings:")
                                for b in pending:
                                    print(f"Booking ID: {b[0]}, User: {b[1]}, Car: {b[2]} {b[3]}, "
                                          f"From: {b[4]}, To: {b[5]}, Amount: ${b[6]}")

                                try:
                                    booking_id = int(input("Enter Booking ID to approve/reject: "))
                                    decision = input("Approve or Reject? (A/R): ").strip().lower()
                                    if decision == 'a':
                                        Booking.update_booking_status(booking_id, 'approved')
                                        print("Booking approved!")
                                    elif decision == 'r':
                                        Booking.update_booking_status(booking_id, 'rejected')
                                        print("Booking rejected!")
                                    else:
                                        print("Invalid input.")
                                except ValueError:
                                    print("Invalid Booking ID entered.")

                        elif admin_choice == '3':
                            print("Logging out...")
                            break
                        else:
                            print("Invalid choice. Try again.")

                elif role.strip().lower() == 'customer':
                    while True:
                        print("\n--- Customer Menu ---")
                        print("1. View Available Cars")
                        print("2. Book a Car")
                        print("3. View Booked Cars")
                        print("4. Logout")
                        cust_choice = input("Choose an option: ")

                        if cust_choice == '1':
                            cars = Car.list_available()
                            if not cars:
                                print("No cars available.")
                            else:
                                print("\nAvailable Cars:")
                                for car in cars:
                                    print(f"ID: {car[0]}, {car[1]} {car[2]}, Year: {car[3]}, Mileage: {car[4]} km")

                        elif cust_choice == '2':
                            cars = Car.list_available()
                            if not cars:
                                print("No cars available to book.")
                            else:
                                car_id = int(input("Enter Car ID to book: "))
                                start_date = input("Start Date (YYYY-MM-DD): ")
                                end_date = input("End Date (YYYY-MM-DD): ")
                                booking = Booking(user_id, car_id, start_date, end_date)
                                booking.book()

                        elif cust_choice == '3':
                            approved = Booking.list_approved_bookings_by_user(user_id)
                            if not approved:
                                print("You have no approved bookings.")
                            else:
                                print("\nYour Approved Bookings:")
                                for b in approved:
                                    print(f"Car: {b[0]} {b[1]}, From: {b[2]}, To: {b[3]}, Amount: ${b[4]}")

                        elif cust_choice == '4':
                            print("Logging out...")
                            break
                        else:
                            print("Invalid choice. Try again.")
            else:
                print("Login failed. Please check your credentials.")

        elif choice == '3':
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
