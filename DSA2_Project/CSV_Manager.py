import csv
from Package import Package
from HashTable import HashTable

package_table = HashTable()
def populate_package_table(csv_file, p_table):
    with open(csv_file) as packages:
        package_info = csv.reader(packages, delimiter=',')
        for info in package_info:
            pId = int(info[0])
            pAddr = info[1]
            pCit = info[2]
            pSt = info[3]
            pZip = int(info[4])
            pDead = info[5]
            pWt = int(info[6])
            pStat = "Loaded"

            p = Package(pId, pAddr, pCit, pSt, pZip, pDead, pWt, pStat)
            package_table.insert(pId, p)

    return p_table

# Here, we are returning the package table and assigning it to 'packages', due to our hash table implementation
package_table = populate_package_table('csv_files/packages.csv', package_table)




# ******************************** TESTING ZONE ********************************

# print("Importing distances...")
# print(distance_matrix)
#
#
# print("Importing addresses...")
# print(address_list)
#
#
# print("Populating package table...")
# print(package_table)

# ******************************** END TESTING ZONE *************************