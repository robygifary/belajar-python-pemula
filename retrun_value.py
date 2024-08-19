# Belajar method retrun value

def jumlahkan(*list_angka):
  total = 0
  for angka in list_angka:
   total += angka
  return (list_angka, total)

list_angka, total = jumlahkan(10, 5)

# Mengambil data total
print(f"Total {list_angka} {total}")
print(f"Total {list_angka} {total}")
print(f"Total {list_angka} {total}")
