from abc import ABC, abstractmethod
from datetime import datetime


class Customer:
    def __init__(self, customer_id, first_name, last_name, email, phone_number, address, username, password,
                 registration_date):
        self.__customer_id = customer_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__phone_number = phone_number
        self.__address = address
        self.__username = username
        self.__password = password
        self.__registration_date = registration_date

    # Getters
    def get_customer_id(self):
        return self.__customer_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_email(self):
        return self.__email

    def get_phone_number(self):
        return self.__phone_number

    def get_address(self):
        return self.__address

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def get_registration_date(self):
        return self.__registration_date

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_email(self, email):
        self.__email = email

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def set_address(self, address):
        self.__address = address

    def set_username(self, username):
        self.__username = username

    def set_password(self, password):
        self.__password = password


class Vehicle:
    def __init__(self, vehicle_id, model, make, year, color, registration_number, availability, daily_rate):
        self.__vehicle_id = vehicle_id
        self.__model = model
        self.__make = make
        self.__year = year
        self.__color = color
        self.__registration_number = registration_number
        self.__availability = availability
        self.__daily_rate = daily_rate

    # Getters
    def get_vehicle_id(self):
        return self.__vehicle_id

    def get_model(self):
        return self.__model

    def get_make(self):
        return self.__make

    def get_year(self):
        return self.__year

    def get_color(self):
        return self.__color

    def get_registration_number(self):
        return self.__registration_number

    def is_available(self):
        return self.__availability

    def get_daily_rate(self):
        return self.__daily_rate

    # Setters
    def set_model(self, model):
        self.__model = model

    def set_make(self, make):
        self.__make = make

    def set_year(self, year):
        self.__year = year

    def set_color(self, color):
        self.__color = color

    def set_registration_number(self, registration_number):
        self.__registration_number = registration_number

    def set_availability(self, availability):
        self.__availability = availability

    def set_daily_rate(self, daily_rate):
        self.__daily_rate = daily_rate


class Reservation:
    def __init__(self, reservation_id, customer_id, vehicle_id, start_date, end_date, total_cost, status):
        self.__reservation_id = reservation_id
        self.__customer_id = customer_id
        self.__vehicle_id = vehicle_id
        self.__start_date = start_date
        self.__end_date = end_date
        self.__total_cost = total_cost
        self.__status = status

    # Getters
    def get_reservation_id(self):
        return self.__reservation_id

    def get_customer_id(self):
        return self.__customer_id

    def get_vehicle_id(self):
        return self.__vehicle_id

    def get_start_date(self):
        return self.__start_date

    def get_end_date(self):
        return self.__end_date

    def get_total_cost(self):
        return self.__total_cost

    def get_status(self):
        return self.__status

    # Setters
    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def set_vehicle_id(self, vehicle_id):
        self.__vehicle_id = vehicle_id

    def set_start_date(self, start_date):
        self.__start_date = start_date

    def set_end_date(self, end_date):
        self.__end_date = end_date

    def set_total_cost(self, total_cost):
        self.__total_cost = total_cost

    def set_status(self, status):
        self.__status = status


class Admin:
    def __init__(self, admin_id, first_name, last_name, email, phone_number, username, password, role, join_date):
        self.__admin_id = admin_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__phone_number = phone_number
        self.__username = username
        self.__password = password
        self.__role = role
        self.__join_date = join_date

    # Getters
    def get_admin_id(self):
        return self.__admin_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_email(self):
        return self.__email

    def get_phone_number(self):
        return self.__phone_number

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def get_role(self):
        return self.__role

    def get_join_date(self):
        return self.__join_date

    # Setters
    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_email(self, email):
        self.__email = email

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def set_username(self, username):
        self.__username = username

    def set_password(self, password):
        self.__password = password

    def set_role(self, role):
        self.__role = role


class ICustomerService(ABC):
    @abstractmethod
    def get_customer_by_id(self, customer_id):
        pass

    @abstractmethod
    def get_customer_by_username(self, username):
        pass

    @abstractmethod
    def register_customer(self, customer_data):
        pass

    @abstractmethod
    def update_customer(self, customer_id, updated_data):
        pass

    @abstractmethod
    def delete_customer(self, customer_id):
        pass


class IVehicleService(ABC):
    @abstractmethod
    def get_vehicle_by_id(self, vehicle_id):
        pass

    @abstractmethod
    def get_available_vehicles(self):
        pass

    @abstractmethod
    def add_vehicle(self, vehicle_data):
        pass

    @abstractmethod
    def update_vehicle(self, vehicle_id, updated_vehicle_data):
        pass

    @abstractmethod
    def remove_vehicle(self, vehicle_id):
        pass


class IReservationService(ABC):
    @abstractmethod
    def get_reservation_by_id(self, reservation_id):
        pass

    @abstractmethod
    def get_reservations_by_customer_id(self, customer_id):
        pass

    @abstractmethod
    def create_reservation(self, reservation_data):
        pass

    @abstractmethod
    def update_reservation(self, reservation_id, updated_reservation_data):
        pass

    @abstractmethod
    def cancel_reservation(self, reservation_id):
        pass


class IAdminService(ABC):
    @abstractmethod
    def get_admin_by_id(self, admin_id):
        pass

    @abstractmethod
    def get_admin_by_username(self, username):
        pass

    @abstractmethod
    def register_admin(self, admin_data):
        pass

    @abstractmethod
    def update_admin(self, admin_id, updated_admin_data):
        pass

    @abstractmethod
    def delete_admin(self, admin_id):
        pass
