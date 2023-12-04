# luas persegi
print("ini menghitung luas dan keliling persegi")
str_sisi = input("sisi : ") # ini untuk mengambil inputan sisinya
int_sisi = int(str_sisi) #mengubah tipe data dari string("") ke integer(angka)
luas_persegi = int_sisi*int_sisi #ini untuk menghitung luas perseginya yang mana variable int_sisi dikali int_sisi
print("Luas perseginya adalah " + str(luas_persegi)) #ini untuk menampilkan output luas nya

# keliling persegi
keliling_persegi = 4 * int_sisi #ini untuk menghitung keliling perseginya yang mana variable int_sisi dikali 4 sesuai dengan rumus keliling persegi yaitu 4 dikali sisi
print("keliling perseginya adalah " + str(keliling_persegi)) #ini untuk menampilkan output keliling persegi nya

# luas segitiga
str_alas = input("alas : ")  #ini untuk mengambil inputan alas segitiga
int_alas = int(str_alas) # mengubah tipe data dari string("") ke integer(angka)
str_tinggi = input("tinggi : ")  #ini untuk mengambil inputan tinggi segitiga
int_tinggi = int(str_tinggi) # mengubah tipe data dari string("") ke integer(angka)
luas_segitiga = 1/2 * int_alas * int_tinggi #ini untuk menghitung luas segitiganya yang mana variable int_alas dikali int_tinggi dan dikali 1/2 
print("luas segitiganya adalah " + str(luas_segitiga))   #ini untuk menampilkan output luas segitiga nya

# keliling segitiga
str_sisi_segitiga = input("sisi: ") #ini untuk mengambil inputan sisi segitiga
int_sisi_segitiga = int(str_sisi_segitiga) # mengubah tipe data dari string("") ke integer(angka)
keliling_segitiga = int_sisi_segitiga + int_sisi_segitiga + int_sisi_segitiga #ini untuk menghitung keliling segitiganya yang mana variable int_sisi + int_sisi +int_sisi 
print("keliling segitiganya adalah " + str(keliling_segitiga))   #ini untuk menampilkan output keliling segitiga nya