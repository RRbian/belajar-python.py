
kata = ["python", "belajar", "coding"]

# Buat List Comprehension untuk mengubah setiap elemen menjadi haruf besar
haruf_besar = [x.upper() for x in kata]
print(haruf_besar)

# Fungsi Lambda
jumlah = lambda x, y, z: x*y*z
hasil = jumlah(2, 4, 6)
print(hasil)


#Try Except
try:
    a = int(input("masukan angka pertama:"))
    b = int(input("masukan angka kedua:"))
    hasil = a /b
    print(f"Hasil dari pembagian: {hasil}")
except ZeroDivisionError:
    print("Pembagi tidak boleh nol.")
