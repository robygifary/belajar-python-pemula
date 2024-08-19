def say_hello(nama):
  return f"Hello {nama}"

def total(*list_angka):
  hasil = 0
  for data in list_angka:
    hasil = hasil + data
  return hasil

def halo_user(name, level):
  print(f"Hallo user {name} - {level}")
  print("Selamat belajar python")

print("start")
halo_user("Robby", 10)
print("=======================")
halo_user("Xavier", 10)
print("finish")