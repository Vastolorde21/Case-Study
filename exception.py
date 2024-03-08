class AuthenticationException(Exception):

    def __init__(self, message="Authentication failed. Incorrect username or password."):
        self.message = message
        super().__init__(self.message)


class ReservationException(Exception):

    def __init__(self, message="Reservation failed."):
        self.message = message
        super().__init__(self.message)


class VehicleNotFoundException(Exception):

    def __init__(self, message="Vehicle not found."):
        self.message = message
        super().__init__(self.message)


class AdminNotFoundException(Exception):

    def __init__(self, message="Admin not found."):
        self.message = message
        super().__init__(self.message)


class InvalidInputException(Exception):

    def __init__(self, message="Invalid input data."):
        self.message = message
        super().__init__(self.message)


class DatabaseConnectionException(Exception):

    def __init__(self, message="Database connection failed."):
        self.message = message
        super().__init__(self.message)

def login(username, password):
    if not is_valid_credentials(username, password):
        raise AuthenticationException()

def make_reservation(vehicle_id):
    if not is_vehicle_available(vehicle_id):
        raise ReservationException()

def get_vehicle_details(vehicle_id):
    vehicle = find_vehicle(vehicle_id)
    if not vehicle:
        raise VehicleNotFoundException()

def get_admin_details(admin_id):
    admin = find_admin(admin_id)
    if not admin:
        raise AdminNotFoundException()

def validate_input(data):
    if not is_valid(data):
        raise InvalidInputException()

def connect_to_database():
    if not is_database_connected():
        raise DatabaseConnectionException()
