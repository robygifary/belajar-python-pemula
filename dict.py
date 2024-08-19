# Belajar tipe data dictionary

customer = {
  "Name":"Robby", 
  "Age":"30", 
  "Address":"Bogor"
}

# cara mengakses tipe data dictionary
name = customer["Name"]
age = customer["Age"]
address = customer["Address"]

# Menambahkan data baru dalam dictionary
customer["Company"] = "BYD"

#Menghapus data dalam dictionary
del customer["Address"]

# cara melakukan perulangan
for key, value in customer.items():
  print(f"{key}:{value}")