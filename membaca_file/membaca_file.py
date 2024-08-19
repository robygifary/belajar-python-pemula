users = open("user.txt", "r")

list = users.readlines()
index = 1
for user in list:
  print(f"{index} - {user}")
  index += 1

users.close()