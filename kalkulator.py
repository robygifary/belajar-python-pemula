# Kalkulator sederhana (+, -, *, /, exit)
command = ""

while command != "exit":
  command = input("Masukan Perintah : ")

  if command == "exit":
    break

  if command != "+" and command != "-" and command != "*" and command != "/":
    print("Perintah tidak dikenali")
    continue

  a = int(input("Masukan angka pertama : "))
  b = int(input("Masukan angka kedua : "))

  if command == "+":
    result = a + b
  elif command == "-":
    result = a - b
  elif command == "*":
    result = a * b
  elif command == "/":
    result = a / b

  print(f"Hasil : {result}")

print("Terima kasih sudah menggunakan aplikasi ini")

