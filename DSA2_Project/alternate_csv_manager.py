import csv

# This function will populate the package table with the package information from the csv file
distance_matrix = list(csv.reader(open('csv_files/updated_distances_only.csv')))
address_table = list(csv.reader(open('csv_files/address_table.csv')))

# Create a list containing all of the package addresses
address_list = []
for i in address_table:
    address_list.append(i[0])

