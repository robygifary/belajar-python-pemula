# Program mangement kontak
import function

# List  of dictionary
daftar_kontak = []
daftar_kontak.append({
  "nama" : "Robby",
  "email" : "gifaryroby@gmail.com",
  "telepon" : "0892318333",
  "alamat" : "Bogor"
})

# Menu program
while True:
  print("# Menu")
  print("1. Daftar Kontak")
  print("2. Tambah Kontak")
  print("3. Hapus Kontak")
  print("4. Cari Kontak")
  print("5. alamat")

  menu = input("Pilih Menu : ")

  if menu == "0":
    break
  elif menu == "1":
    function.display_kontak(daftar_kontak)
  elif menu == "2":
    kontak = function.new_kontak()
    daftar_kontak.append(kontak)
  elif menu == "3":
    function.hapus_kontak(daftar_kontak)
  elif menu == "4":
    function.cari_kontak(daftar_kontak)
  elif menu == "5":
    function.new_alamat(daftar_kontak)

print("Program Selesai Berjalan, Sampai Jumpa ...")