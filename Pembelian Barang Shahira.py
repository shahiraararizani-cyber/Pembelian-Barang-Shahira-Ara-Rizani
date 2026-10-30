# Program pembelian barang

nama = input("Masukkan nama pembeli: ")

print(" DAFTAR BARANG ")
print("1. Buku = Rp10.000")
print("2. Pensil = Rp5.000")
print("3. Pulpen = Rp7.000")
print("4. Penggaris = Rp8.000")
print("5. Tas = Rp50.000")

barang = int(input(" Pilih nomor barang (1-5): "))
jumlah = int(input("Masukkan jumlah barang: "))

if barang == 1:
    harga = 10000
elif barang == 2:
    harga = 5000
elif barang == 3:
    harga = 7000
elif barang == 4:
    harga = 8000
elif barang == 5:
    harga = 50000
else:
    harga = 0

total = harga * jumlah

diskon = total >= 100000 or jumlah >= 10

print(" HASIL PEMBELIAN ")
print("Nama pembeli:", nama)
print("Total harga: Rp", total)
print("Mendapat diskon:", diskon)

if diskon:
    print("Selamat! Anda mendapat diskon.")
else:
    print("Maaf, Anda tidak mendapat diskon.")
