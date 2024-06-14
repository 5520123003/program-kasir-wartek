print("\n------- Program Kasir Sederhana Rozi ------")
pembeli = input("\nMasukan nama pembeli : ")
print("Nama pembeli :",pembeli)

def fungsimakanan():
    global totalmakn
    global porsi
    global mkn
    print("\n----------MENU MAKANAN----------\n")

    print("1. Bakso--------Rp. 10000")
    print("2. Mie Ayam-----Rp. 13000")
    print("3. Soto---------Rp. 12000")
    print("4. Nasi Goreng--Rp. 15000")
    print("5. Kwetiau------Rp. 12000")
    nomor = int(input("\nMasukkan Pilihan: "))
    porsi = int(input("Berapa Porsi:"))

    if nomor == 1:
        totalmakn = porsi * 10000
        print(porsi,"porsi Bakso = Rp",totalmakn)
        mkn = ("Bakso")

    elif nomor == 2:
        totalmakn = porsi * 13000
        print(porsi,"porsi Mie Ayam = Rp",totalmakn)
        mkn = ("Mie Ayam")

    elif nomor == 3:
        totalmakn = porsi * 12000
        print(porsi,"Soto = Rp",totalmakn)
        mkn = ("Soto")

    elif nomor == 4:
        totalmakn = porsi * 15000
        print(porsi,"Nasi Goreng = Rp",totalmakn)
        mkn = ("Nasi Goreng")

    elif nomor == 5:
        totalmakn = porsi * 12000
        print(porsi,"kwetiau = Rp",totalmakn)
        mkn = ("kwetiau")

    else:
        print("Pilihan tidak ada, silahkan masukkan lagi!!")
        fungsimakanan()
def fungsiminuman():
    global totalmnm
    global mnm
    global gelas

    print("\n----------MENU MINUMAN----------\n")

    print("1. Air Mineral---Rp. 3000")
    print("2. Es Teh Manis--Rp. 4000")
    print("3. Es Jeruk------Rp. 7000")
    print("4. Es Kopi-------Rp. 8000")
    print("5. Es Capuccino--Rp. 7000")
    nomor = int(input("\nMasukkan Pilihan: "))
    gelas = int(input("Berapa Gelas:"))

    if nomor == 1:
        totalmnm = gelas * 3000
        print(gelas, "Air Mineral = Rp", totalmnm)
        mnm = ("Air Mineral")

    elif nomor == 2:
        totalmnm = gelas * 4000
        print(gelas, "Es Teh ManisEs = Rp", totalmnm)
        mnm = ("Es Teh Manis")

    elif nomor == 3:
        totalmnm = gelas * 7000
        print(gelas, "Es Jeruk = Rp", totalmnm)
        mnm = ("Es Jeruk")

    elif nomor == 4:
        totalmnm = gelas * 8000
        print(gelas, "Es Kopi = Rp", totalmnm)
        mnm = ("Es Kopi")

    elif nomor == 5:
        totalmnm = gelas * 12000
        print(gelas, "Es Capuccino = Rp", totalmnm)
        mnm = ("Es Capuccino")

    else:
        print("Pilihan tidak ada, silahkan masukkan lagi!!")


        fungsiminuman()

fungsimakanan()
fungsiminuman()
totalsemua = totalmakn + totalmnm

print("\nTotal harus Dibayar: Rp",totalsemua)
uang = int(input("Uang tunai Pembeli: Rp"))
kembalian = int(uang - totalsemua)
print("Kembalian:",kembalian)

print("\n========================================")
print("===============STRUK BELI===============")
print("========================================")

print("Nama\t\t:",pembeli)
print("beli\t\t:",porsi,mkn,"(Rp",totalmakn,")")
print("\t\t\t:",gelas,mnm,"(Rp",totalmnm,")")
print("Tagihan\t\t: Rp",totalsemua)
print("Bayar\t\t: Rp",uang)
print("kembalian\t: Rp",kembalian)
print("========================================")
print("========================================")








