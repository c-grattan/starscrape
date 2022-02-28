import sys
import csv

#Argument passing
shipId = ""
dir = ""
for i, arg in enumerate(sys.argv):
	if arg == "--ship":
		shipId = str(sys.argv[i + 1] or "")
	elif arg == "--dir":
		dir = str(sys.argv[i + 1] or "")

if dir != "":
	print("Game directory:", dir)
else:
	print("Game directory not provided")

if shipId != "":
	print("Ship id:", shipId)
else:
	print("Ship ID not provided")

#Get CSV file data
hullFolder = dir + "\starsector-core\data\hulls"

with open(hullFolder + "\\ship_data.csv") as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if row['id'] == shipId:
			print(row)
			break

#Open hull file
'''
try:
	with open(hullFolder + "\\{}.ship".format(shipId)) as shipFile:
		for row in shipFile:
			print(row, end='')
except FileNotFoundError:
	print("Could not find " + shipId + " ship file")
'''