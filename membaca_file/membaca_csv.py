import csv

data = open("user.csv", "r")

users_csv = csv.reader(data, delimiter=",")

for row in users_csv:
  print(f"Name : {row[0]} . Username : {row[1]} . Role : {row[-1]}")

data.close()