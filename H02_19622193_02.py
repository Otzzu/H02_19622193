# NIM/Nama  : 19622193/Mesach Harmasendro
# Tanggal   : 4 Oktober 2022
# Deskripsi : Program menghitung jumlah nilai membesar

# KAMUS
# angka, angka2, n_tidak_membesar, sum, i : integer

angka = int(input("Angka ke-1: "))
i = 2

n_tidak_membesar = 0 #banyak nilai yang tidak membesar
sum = 0

while n_tidak_membesar < 3:
    angka2 = int(input(f"Angka ke-{i}: "))
    if angka2 > angka:
        sum += angka2
        n_tidak_membesar = 0
    else :
        n_tidak_membesar += 1
        
    angka = angka2
    i += 1

print(f"Jumlah nilai yang membesar adalah {sum}.")