from dao import CustomerService, VehicleService, ReservationService, AdminService
from exception import AuthenticationException, ReservationException, VehicleNotFoundException, AdminNotFoundException, InvalidInputException, DatabaseConnectionException

class CarConnect:
    def __init__(self):
        self.db_context = DatabaseContext("localhost", "root", "HARSHA1@singh", "carrental")

    def display_menu(self):
        print("\nWelcome to CarConnect Management System")
        print("1. Customer Management")
        print("2. Vehicle Management")
        print("3. Reservation Management")
        print("4. Admin Management")
        print("5. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                self.customer_management()
            elif choice == "2":
                self.vehicle_management()
            elif choice == "3":
                self.reservation_management()
            elif choice == "4":
                self.admin_management()
            elif choice == "5":
                print("Exiting CarConnect Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def customer_management(self):
        customer_service = CustomerService(self.db_context)
        while True:
            print("\nCustomer Management:")
            print("1. Register Customer")
            print("2. Update Customer")
            print("3. Delete Customer")
            print("4. Show customer by id:")
            print("5. Go back")
            choice = input("Enter your choice: ")

            if choice == "1":
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                email = input("Enter email: ")
                phone_number = input("Enter phone number: ")
                address = input("Enter address: ")
                username = input("Enter username: ")
                password = input("Enter password: ")
                registration_date = input("Enter registration date (YYYY-MM-DD): ")
                customer_data = (first_name, last_name, email, phone_number, address, username, password, registration_date)
                customer_service.register_customer(customer_data)
                print("Customer registered successfully")
            elif choice == "2":
                customer_id = input("Enter customer ID: ")
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                email = input("Enter email: ")
                phone_number = input("Enter phone number: ")
                address = input("Enter address: ")
                username = input("Enter username: ")
                password = input("Enter password: ")
                customer_data = (first_name, last_name, email, phone_number, address, username, password, customer_id)
                customer_service.update_customer(customer_data)
            elif choice == "3":
                customer_id = input("Enter customer ID: ")
                customer_service.delete_customer(customer_id)
            elif choice == "4":
                customer_id = input("Enter Customer ID: ")
                customer_data = customer_service.get_customer_by_id(customer_id)
                if customer_data:
                    print("Customer Details:")
                    print(customer_data)
                else:
                    print("Customer not found.")


            elif choice == "5":
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def vehicle_management(self):
        vehicle_service = VehicleService(self.db_context)
        while True:
            print("\nVehicle Management:")
            print("1. Add Vehicle")
            print("2. Update Vehicle")
            print("3. Remove Vehicle")
            print("4. Get vehicle by ID")
            print("5. Go back")
            choice = input("Enter your choice: ")

            if choice == "1":
                model = input("Enter vehicle model: ")
                make = input("Enter vehicle make: ")
                year = input("Enter manufacturing year: ")
                color = input("Enter vehicle color: ")
                registration_number = input("Enter registration number: ")
                availability = input("Is the vehicle available? (True/False): ")
                daily_rate = input("Enter daily rental rate: ")
                vehicle_data = (model, make, year, color, registration_number, availability, daily_rate)
                vehicle_service.add_vehicle(vehicle_data)

            elif choice == "2":
                vehicle_id = input("Enter vehicle ID: ")
                model = input("Enter vehicle model: ")
                make = input("Enter vehicle make: ")
                year = input("Enter manufacturing year: ")
                color = input("Enter vehicle color: ")
                registration_number = input("Enter registration number: ")
                availability = input("Is the vehicle available? (True/False): ")
                daily_rate = input("Enter daily rental rate: ")
                vehicle_data = (model, make, year, color, registration_number, availability, daily_rate, vehicle_id)
                vehicle_service.update_vehicle(vehicle_data)
            elif choice == "3":
                vehicle_id = input("Enter vehicle ID: ")
                vehicle_service.remove_vehicle(vehicle_id)
            elif choice == "4":
                vehicle_id = input("Enter Vehicle ID: ")
                vehicle_data = vehicle_service.get_vehicle_by_id(vehicle_id)
                if vehicle_data:
                    print("Vehicle Details:")
                    print(vehicle_data)
                else:
                    print("Vehicle not found.")
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def reservation_management(self):
        reservation_service = ReservationService(self.db_context)
        while True:
            print("\nReservation Management:")
            print("1. Create Reservation")
            print("2. Update Reservation")
            print("3. Cancel Reservation")
            print("4. Go back")
            choice = input("Enter your choice: ")

            if choice == "1":
                customer_id = input("Enter customer ID: ")
                vehicle_id = input("Enter vehicle ID: ")
                start_date = input("Enter start date (YYYY-MM-DD): ")
                end_date = input("Enter end date (YYYY-MM-DD): ")
                total_cost = input("Enter total cost: ")
                status = input("Enter status(A/N): ")
                reservation_data = (customer_id, vehicle_id, start_date, end_date, total_cost, status)
                reservation_service.create_reservation(reservation_data)
                print("Reservation Created" if status == "A" else "Car not available")
            elif choice == "2":
                reservation_id = input("Enter reservation ID: ")
                customer_id = input("Enter customer ID: ")
                vehicle_id = input("Enter vehicle ID: ")
                start_date = input("Enter start date (YYYY-MM-DD): ")
                end_date = input("Enter end date (YYYY-MM-DD): ")
                total_cost = input("Enter total cost: ")
                status = input("Enter status: ")
                reservation_data = (customer_id, vehicle_id, start_date, end_date, total_cost, status, reservation_id)
                reservation_service.update_reservation(reservation_data)
            elif choice == "3":
                reservation_id = input("Enter reservation ID: ")
                reservation_service.cancel_reservation(reservation_id)
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def admin_management(self):
        admin_service = AdminService(self.db_context)
        while True:
            print("\nAdmin Management:")
            print("1. Register Admin")
            print("2. Update Admin")
            print("3. Delete Admin")
            print("4. Go back")
            choice = input("Enter your choice: ")

            if choice == "1":
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                email = input("Enter email: ")
                phone_number = input("Enter phone number: ")
                username = input("Enter username: ")
                password = input("Enter password: ")
                role = input("Enter role: ")
                join_date = input("Enter join date (YYYY-MM-DD): ")
                admin_data = (first_name, last_name, email, phone_number, username, password, role, join_date)
                admin_service.register_admin(admin_data)
            elif choice == "2":
                admin_id = input("Enter admin ID: ")
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                email = input("Enter email: ")
                phone_number = input("Enter phone number: ")
                username = input("Enter username: ")
                password = input("Enter password: ")
                role = input("Enter role: ")
                admin_data = (first_name, last_name, email, phone_number, username, password, role, admin_id)
                admin_service.update_admin(admin_data)
            elif choice == "3":
                admin_id = input("Enter admin ID: ")
                admin_service.delete_admin(admin_id)
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    car_connect = CarConnect()
    car_connect.run()
