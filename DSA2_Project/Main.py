from Truck import *

if __name__ == '__main__':

    # WGU C950 Assignment
    # Student: James Revello, Student ID: 010649181

    class Main:

        # Our hub currently has 3 functioning trucks with set departure times.
        truck_1 = Truck(datetime.timedelta(hours=8), "Truck 1")
        truck_2 = Truck(datetime.timedelta(hours=9, minutes=5), "Truck 2")
        truck_3 = Truck(datetime.timedelta(hours=10, minutes=20), "Truck 3")

        # After special cases, all packages will be loaded based on delivery deadline
        # package 15 due by 9        Package 13, 14, 15, 16, 19, 20 = delivered together
        early_delivery_group = [13, 14, 15, 16, 19, 20, 1, 29, 30, 31, 34, 37, 40, 2, 4, 5]

        # Package 6, 25, 28, 32 = can't be loaded until 9:05
        # Package 3, 18, 36, 38 = can only be on truck 2
        truck2_delivery_group = [22, 10, 28, 32, 3, 18, 36, 38, 7, 8, 6, 25]

        # Package 9 = Wrong address updated at 10:20
        late_package_group = [9, 23, 24, 26, 27, 33, 35, 39, 11, 12, 17, 21]

        # Which will be loaded with the manual delivery groups (for now)
        truck_1.load_truck(early_delivery_group)
        truck_2.load_truck(truck2_delivery_group)
        truck_3.load_truck(late_package_group)

        # Update Package Status
        for packageID in range(1, 41):
            package = package_table.search(packageID)
            if packageID in early_delivery_group:
                package.status = "En Route"
            elif packageID in truck2_delivery_group:
                package.status = "En Route"
            elif packageID in late_package_group:
                package.status = "En Route"

        # Now we'll create destination lists for each truck
        truck_1.populate_destinations_list(early_delivery_group)
        truck_2.populate_destinations_list(truck2_delivery_group)
        truck_3.populate_destinations_list(late_package_group)

        # We'll label all packages on the truck:
        truck_1.label_packages_on_truck()
        truck_2.label_packages_on_truck()
        truck_3.label_packages_on_truck()

        # And finally, we'll deliver the packages for each truck
        truck_1.deliver_packages_on_truck()
        truck_2.deliver_packages_on_truck()
        truck_3.deliver_packages_on_truck()

        # The User Interface starts here
        print("Welcome to the WGUPS Package Delivery System.")
        print("Please select an option from the menu below.")
        print("1. View the status of all packages and the total distance traveled by all trucks.")
        print("2. View a specific package at a specific time.")
        print("3. View all packages at a specific time.")
        print("4. Exit the program.")

        # If-then logic for each of the selections offered above
        try:
            user_entered_int = int(input("Enter your single integer selection: "))
            if user_entered_int == 1:
                total_distance_traveled = truck_1.total_mileage_traveled + truck_2.total_mileage_traveled + truck_3.total_mileage_traveled
                print('Total mileage traveled by all three trucks is:', total_distance_traveled)
                for packageID in range(1, 41):
                    package = package_table.search(packageID)
                    print(str(package))
            elif user_entered_int == 2:
                package_id = int(input("Enter the package ID: "))
                time_str = input("Enter the time (HH:MM:SS): ")
                h, m, s = map(int, time_str.split(':'))
                time = datetime.timedelta(hours=h, minutes=m, seconds=s)
                package = package_table.search(package_id)
                # Assuming the package status is updated based on the time
                package.set_package_status(time)
                if package_id == 9:
                    package.address = "410 S State St"
                package.set_package_status(time)
                print(f"Status of package {package_id} at {time_str}: {package.status}")
            elif user_entered_int == 3:
                time_str = input("Enter the time (HH:MM:SS): ")
                h, m, s = map(int, time_str.split(':'))
                time = datetime.timedelta(hours=h, minutes=m, seconds=s)
                for packageID in range(1, 41):
                    package = package_table.search(packageID)
                    # Assuming the package status is updated based on the time
                    package.set_package_status(time)
                    print(f"Status of package {packageID} at {time_str}: {str(package)}")
            elif user_entered_int == 4:
                print("Thank you for using the delivery service.")
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

