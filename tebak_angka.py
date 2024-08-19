coba_angka = 0
limit_angka = 3
rahasia_angka = 7

while coba_angka < limit_angka:
  tebak_angka = input("Masukan angka (1-10)")
  tebak_angka = int(tebak_angka)

  if(tebak_angka == rahasia_angka):
    print("Selamat, tebakan anda benar")
    break

  coba_angka += 1