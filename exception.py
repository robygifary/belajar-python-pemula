# Belajar exception
try:
  level = int(input("Level Kamu : "))
  print(level)
except ValueError:
  print("Yang kamu masukan bukan angka")