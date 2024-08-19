# Belajar Argument List

def tambah(*list_angka):
  total = 0
  for angka in list_angka:
    total = total + angka
    print(f"Total {list_angka} = {total}")

tambah(10, 10, 10, 10, 10)