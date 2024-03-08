class DatabaseContext:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

    def __del__(self):
        if self.connection.is_connected():
            self.connection.close()

    def execute_query(self, query, params=None):
        cursor = self.connection.cursor(dictionary=True)
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        return cursor

    def get_customer_by_id(self, customer_id):
        query = "SELECT * FROM Customer WHERE CustomerID = %s"
        cursor = self.execute_query(query, (customer_id,))
        return cursor.fetchone()

    def get_customer_by_username(self, username):
        query = "SELECT * FROM Customer WHERE Username = %s"
        cursor = self.execute_query(query, (username,))
        return cursor.fetchone()

    def register_customer(self, customer_data):
        query = "INSERT INTO Customer (FirstName, LastName, Email, PhoneNumber, Address, Username, Password, RegistrationDate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor = self.execute_query(query, customer_data)
        self.connection.commit()
        return cursor.lastrowid

    def update_customer(self, customer_id, updated_data):
        query = "UPDATE Customer SET FirstName = %s, LastName = %s, Email = %s, PhoneNumber = %s, Address = %s, Username = %s, Password = %s, RegistrationDate = %s WHERE CustomerID = %s"
        updated_data += (customer_id,)
        cursor = self.execute_query(query, updated_data)
        self.connection.commit()
        return cursor.rowcount

    def delete_customer(self, customer_id):
        query = "DELETE FROM Customer WHERE CustomerID = %s"
        cursor = self.execute_query(query, (customer_id,))
        self.connection.commit()
        return cursor.rowcount
    # Vehicle operations
    def get_vehicle_by_id(self, vehicle_id):
        query = "SELECT * FROM Vehicle WHERE VehicleID = %s"
        cursor = self.execute_query(query, (vehicle_id,))
        return cursor.fetchone()

    def get_available_vehicles(self):
        query = "SELECT * FROM Vehicle WHERE Availability = 1"
        cursor = self.execute_query(query)
        return cursor.fetchall()

    def add_vehicle(self, vehicle_data):
        query = "INSERT INTO Vehicle (Model, Make, Year, Color, RegistrationNumber, Availability, DailyRate) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor = self.execute_query(query, vehicle_data)
        self.connection.commit()
        return cursor.lastrowid

    def update_vehicle(self, vehicle_id, updated_vehicle_data):
        query = "UPDATE Vehicle SET Model = %s, Make = %s, Year = %s, Color = %s, RegistrationNumber = %s, Availability = %s, DailyRate = %s WHERE VehicleID = %s"
        updated_vehicle_data += (vehicle_id,)
        cursor = self.execute_query(query, updated_vehicle_data)
        self.connection.commit()
        return cursor.rowcount

    def remove_vehicle(self, vehicle_id):
        query = "DELETE FROM Vehicle WHERE VehicleID = %s"
        cursor = self.execute_query(query, (vehicle_id,))
        self.connection.commit()
        return cursor.rowcount

    # Reservation operations
    def get_reservation_by_id(self, reservation_id):
        query = "SELECT * FROM Reservation WHERE ReservationID = %s"
        cursor = self.execute_query(query, (reservation_id,))
        return cursor.fetchone()

    def get_reservations_by_customer_id(self, customer_id):
        query = "SELECT * FROM Reservation WHERE CustomerID = %s"
        cursor = self.execute_query(query, (customer_id,))
        return cursor.fetchall()

    def create_reservation(self, reservation_data):
        query = "INSERT INTO Reservation (CustomerID, VehicleID, StartDate, EndDate, TotalCost, Status) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor = self.execute_query(query, reservation_data)
        self.connection.commit()
        return cursor.lastrowid

    def update_reservation(self, reservation_id, updated_reservation_data):
        query = "UPDATE Reservation SET CustomerID = %s, VehicleID = %s, StartDate = %s, EndDate = %s, TotalCost = %s, Status = %s WHERE ReservationID = %s"
        updated_reservation_data += (reservation_id,)
        cursor = self.execute_query(query, updated_reservation_data)
        self.connection.commit()
        return cursor.rowcount

    def cancel_reservation(self, reservation_id):
        query = "DELETE FROM Reservation WHERE ReservationID = %s"
        cursor = self.execute_query(query, (reservation_id,))
        self.connection.commit()
        return cursor.rowcount

    # Admin operations
    def get_admin_by_id(self, admin_id):
        query = "SELECT * FROM Admin WHERE AdminID = %s"
        cursor = self.execute_query(query, (admin_id,))
        return cursor.fetchone()

    def get_admin_by_username(self, username):
        query = "SELECT * FROM Admin WHERE Username = %s"
        cursor = self.execute_query(query, (username,))
        return cursor.fetchone()

    def register_admin(self, admin_data):
        query = "INSERT INTO Admin (FirstName, LastName, Email, PhoneNumber, Username, Password, Role, JoinDate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor = self.execute_query(query, admin_data)
        self.connection.commit()
        return cursor.lastrowid

    def update_admin(self, admin_id, updated_admin_data):
        query = "UPDATE Admin SET FirstName = %s, LastName = %s, Email = %s, PhoneNumber = %s, Username = %s, Password = %s, Role = %s, JoinDate = %s WHERE AdminID = %s"
        updated_admin_data += (admin_id,)
        cursor = self.execute_query(query, updated_admin_data)
        self.connection.commit()
        return cursor.rowcount

    def delete_admin(self, admin_id):
        query = "DELETE FROM Admin WHERE AdminID = %s"
        cursor = self.execute_query(query, (admin_id,))
        self.connection.commit()
        return cursor.rowcount
class CustomerService(ICustomerService):
    def __init__(self, database_context):
        self.database_context = database_context

    def get_customer_by_id(self, customer_id):
        return self.database_context.get_customer_by_id(customer_id)

    def get_customer_by_username(self, username):
        return self.database_context.get_customer_by_username(username)

    def register_customer(self, customer_data):
        return self.database_context.register_customer(customer_data)

    def update_customer(self, customer_id, updated_data):
        return self.database_context.update_customer(customer_id, updated_data)

    def delete_customer(self, customer_id):
        return self.database_context.delete_customer(customer_id)
class VehicleService(IVehicleService):
    def __init__(self, database_context):
        self.database_context = database_context

    def get_vehicle_by_id(self, vehicle_id):
        return self.database_context.get_vehicle_by_id(vehicle_id)

    def get_available_vehicles(self):
        return self.database_context.get_available_vehicles()

    def add_vehicle(self, vehicle_data):
        return self.database_context.add_vehicle(vehicle_data)

    def update_vehicle(self, vehicle_id, updated_vehicle_data):
        return self.database_context.update_vehicle(vehicle_id, updated_vehicle_data)

    def remove_vehicle(self, vehicle_id):
        return self.database_context.remove_vehicle(vehicle_id)

class ReservationService(IReservationService):
    def __init__(self, database_context):
        self.database_context = database_context

    def get_reservation_by_id(self, reservation_id):
        return self.database_context.get_reservation_by_id(reservation_id)

    def get_reservations_by_customer_id(self, customer_id):
        return self.database_context.get_reservations_by_customer_id(customer_id)

    def create_reservation(self, reservation_data):
        return self.database_context.create_reservation(reservation_data)

    def update_reservation(self, reservation_id, updated_reservation_data):
        return self.database_context.update_reservation(reservation_id, updated_reservation_data)

    def cancel_reservation(self, reservation_id):
        return self.database_context.cancel_reservation(reservation_id)

class AdminService(IAdminService):
    def __init__(self, database_context):
        self.database_context = database_context

    def get_admin_by_id(self, admin_id):
        return self.database_context.get_admin_by_id(admin_id)

    def get_admin_by_username(self, username):
        return self.database_context.get_admin_by_username(username)

    def register_admin(self, admin_data):
        return self.database_context.register_admin(admin_data)

    def update_admin(self, admin_id, updated_admin_data):
        return self.database_context.update_admin(admin_id, updated_admin_data)

    def delete_admin(self, admin_id):
        return self.database_context.delete_admin(admin_id)

