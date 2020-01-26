from os import path
from operator import mul
import csv


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        return path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)
        self.car_type = "car"


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.body_length, self.body_width, self.body_height = Truck.parse_whl(body_whl)
        self.car_type = "truck"

    @staticmethod
    def parse_whl(whl):
        parsed_whl = whl.strip().split("x")

        if len(parsed_whl) != 3:
            return [0.0, 0.0, 0.0]
        else:
            return list(map(float, parsed_whl))

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra
        self.car_type = "spec_machine"


def get_car_list(csv_filename):
    car_types = {"car", "truck", "spec_machine", "Car", "Truck", "Spec_machine"}
    cars_list = []

    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        for row in reader:
            try:
                car_type, brand, photo_file_name, carrying = row[0], row[1], row[3], row[5]
                carrying = float(carrying)
                if car_type not in car_types or not brand or not photo_file_name or not carrying:
                    continue
                if "." not in photo_file_name:
                    continue
                else:
                    if car_type == "car" or car_type == "Car":
                        cars_list.append(Car(brand, photo_file_name, carrying, int(row[2])))
                    elif car_type == "truck" or car_type == "Truck":
                        cars_list.append(Truck(brand, photo_file_name, carrying, row[4]))
                    elif car_type == "spec_machine" or car_type == "Spec_machine":
                        if bool(row[6]):
                            cars_list.append(SpecMachine(brand, photo_file_name, carrying, row[6]))
                    else:
                        continue
            except:
                continue
    return cars_list