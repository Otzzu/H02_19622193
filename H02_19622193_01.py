# NIM/Nama  : 19622193/Mesach Harmasendro
# Tanggal   : 4 Oktober 2022
# Deskripsi : Program untuk mengecek apakah suatu bilangan adalah bilangan sempurna atau bukan

# KAMUS
# bilangan, sum, i : integer

bilangan = int(input("Masukan bilangan: "))
sum = 0

for i in range(1, bilangan):
    if bilangan % i == 0:
        sum += i

if bilangan == sum:
    print("Bilangan tersebut adalah bilangan sempurna")
else:
    print("Bilangan tersebut bukan bilangan sempurna")
