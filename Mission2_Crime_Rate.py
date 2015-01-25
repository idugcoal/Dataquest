
# assigns the file object to the variable f
f = open("crime_rates.csv", "r")
# stores the contents of the file as a string stored in the variable data
data = f.read()
# split the file into rows at the newline character
rows = data.split('\n')

full_data = []

for row in rows:
    split_row = row.split(",")
    split_row[1] = int(split_row[1])
    full_data.append(split_row)

lowest_crime_rate = 10000

for item in full_data:
	if item[1] < lowest_crime_rate:
		lowest_crime_rate = item[1]

city = ""
for item in full_data:
	if item[1] == lowest_crime_rate:
		city = item[0]

