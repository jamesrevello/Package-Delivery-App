from CSV_Manager import *
from alternate_csv_manager import *
import datetime


class Truck:
    SPEED_IN_MILES_PER_HOUR = 18     # Using variables to abstract away magic numbers which might
    TRUCK_CAPACITY = 16              # make our code illegible and may change later


    def __init__(self, departure_time, truck_name=None):
        self.packages_on_truck = []
        self.current_location = '4001 South 700 East'
        self.next_location = None
        self.total_mileage_traveled = float(0.0)
        self.departure_time = departure_time
        self.destinations_list = []
        self.delivered_packages = []
        self.time_packages_delivered = None
        self.truck_timer = departure_time
        self.name = truck_name

    def __str__(self):                                         # String method so we can check truck status
        return (f"Truck: {self.packages_on_truck}, "
                f"Location: {self.current_location}, "
                f"Mileage: {self.total_mileage_traveled}")

    def load_truck(self, packages):                    # Loading the truck here, with hand-picked packages as parameters
        loaded_packages_list = []
        for i in range(len(packages)):
            loaded_packages_list.insert(packages[i], package_table.search(packages[i]))
        self.packages_on_truck = loaded_packages_list
        for i in self.packages_on_truck:
            i.left_hub_at = self.departure_time

    def label_packages_on_truck(self):
        for package in self.packages_on_truck:
            package.truck_loaded_on = self.name

    def populate_destinations_list(self, packages_on_truck):          # Creating a 'deliver to' list based on loaded packages
        for i in range(len(packages_on_truck)):
            self.destinations_list.append(self.packages_on_truck[i].address)
        self.destinations_list.append("HUB")
        return self.destinations_list

    def find_min_distance(self):          # Here we find our nearest neighbor for our delivery function
        nearest_neighbor = 1000             # Arbitrary large number to start
        for i in self.packages_on_truck:
            distance_between_addresses(self.current_location, i.address)
            if distance_between_addresses(self.current_location, i.address) < nearest_neighbor:
                nearest_neighbor = distance_between_addresses(self.current_location, i.address)
                self.next_location = i.address
        return self.next_location

    def set_next_location(self):
        self.next_location = self.find_min_distance()

    def deliver_packages_on_truck(self):
        # Self-explanatory based on naming convention... while we have packages on
        while self.packages_on_truck:       # our truck, we'll move to the nearest neighbor recursively and update
            if self.truck_timer > datetime.timedelta(hours=10, minutes=20):
                for package in self.packages_on_truck:
                    if package.Id == 9:
                        package.address = "410 S State St"
            self.find_min_distance()        # statuses (time, mileage, etc) with each delivery.
            self.set_next_location()
            self.total_mileage_traveled += distance_between_addresses(self.current_location, self.next_location)
            self.delivered_packages = [x for x in self.packages_on_truck if x.address == self.next_location]
            self.packages_on_truck = [x for x in self.packages_on_truck if x.address != self.next_location]
            self.current_location = self.next_location
            self.truck_timer = self.departure_time + datetime.timedelta(
                hours=(self.total_mileage_traveled / self.SPEED_IN_MILES_PER_HOUR))
            for package in self.delivered_packages:
                package.delivery_time = self.truck_timer
                package.status = "Delivered at " + str(self.truck_timer)
            # print statements to test the function
            # print(self.packages_on_truck)
            # print(self.current_location)
            # print(self.total_mileage_traveled)
            # print(self.truck_timer)
            # print(self.time_packages_delivered)

        self.next_location = '4001 South 700 East'
        self.total_mileage_traveled += distance_between_addresses(self.current_location, self.next_location)
        self.truck_timer = self.departure_time + datetime.timedelta(hours=(self.total_mileage_traveled / self.SPEED_IN_MILES_PER_HOUR))
        self.current_location = self.next_location

    ### use address_list index for each item in destinations list to find row in distance_table

def distance_between_addresses(address_string_1, address_string_2):    # Checks two address indexes from table and returns distance as a float
    return float(distance_matrix[address_list.index(address_string_1)][address_list.index(address_string_2)])



# ********************** Package loading logic START********************************

# TODO: Implement automatic truck loading based on notes and Zip Code. For now, loading trucks manually.
'''
    Delivery Time Order, after special cases loaded:
    1030 - 1, 29, 30, 31, 34, 37, 40
    EOD  - 2, 4, 5, 7, 8, , 10, 11, 12, 17, 21, 22, 23, 24, 26, 27, 33, 35, 39
'''


# ********************** Package loading logic END ********************************





# Now we'll create destination lists for each truck
# for package in truck_1.packages_on_truck:
#     truck_1.destinations_list.append(package.address)
# for package in truck_2.packages_on_truck:   # Truck 2 has a special address
#     truck_2.destinations_list.append(package.address)
# for package in truck_3.packages_on_truck:
#     truck_3.destinations_list.append(package.address)



# ******************************** TESTING ZONE ********************************
# Print the packages on each truck
# print("Truck 1:")
# for package in truck_1.packages_on_truck:
#     print(package.Id)
#     print(package.address)
# print("\nTruck 2:")
# for package in truck_2.packages_on_truck:
#     print(package.Id)
#     print(package.address)
# print("\nTruck 3:")
# for package in truck_3.packages_on_truck:
#     print(package.Id)
#     print(package.address)

#
# # Print the destinations for each truck
# print("Truck 1 Destinations:")
# for destination in truck_1.destinations_list:
#     print(destination)
# print("\nTruck 2 Destinations:")
# for destination in truck_2.destinations_list:
#     print(destination)
# print("\nTruck 3 Destinations:")
# for destination in truck_3.destinations_list:
#     print(destination)

# ***********************************************************************************
#
# def return_address_index(address):
#     index = address_list.index(address)
#     return index




#
# print(address_list)
# print(return_address_index('4001 South 700 East'))


#
# x = distance_between_addresses('4001 South 700 East', '1060 Dalton Ave S')
# print(x)

# Insert address1.index, address2.index as parameters into "distance_between" and get the
# x_y coordinate distance as a float
#
# print(truck_1.find_min_distance())
# print(truck_2.find_min_distance())
# print(truck_3.find_min_distance())
