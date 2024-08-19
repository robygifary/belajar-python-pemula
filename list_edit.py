# Membuat list
nama = ["Doni", "Andi", "Deni"]

#menambah data ke list
nama.append("Sandi")

# Mengakses list
nama[0]

# Menghapus data di list
nama.remove("Deni")

# Mengubah data di list
print(nama)
nama[0] = "Robby"
print(nama)

# memasukan element baru ke dalam list
nama.insert(1, "Arya")
print(nama)

numbers = [5, 6, 7, 8, 9]

# menjumlahkan list dengan perulangan for
init_number = 0
for number in numbers:
  init_number = init_number + number

print(init_number)

# menjumlahkan list dengan function sum()
total = sum(numbers)
print(total)

# mencari angka terbesar di list menggunakan function max()
max_number = max(numbers)
print(max_number)

# mencari angka terbesar di list menggunakan for
number_max = numbers[0]
for number in numbers:
  if number > number_max:
    number_max = number
print(number_max)