
# assigns the file object to the variable f
f = open("crime_rates.csv", "r")
# stores the contents of the file as a string stored in the variable b
b = f.read()
# split the file into rows at the newline character
rows = b.split('\n')
