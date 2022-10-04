# NIM/Nama  : 19622193/Mesach Harmasendro
# Tanggal   : 4 Oktober 2022
# Deskripsi : Program mencari faktor prima pada suatu bilangan yanag diinputkan

# KAMUS
# N, i, j : integer
# faktor_pertama, prima : boolean

# ALGORITMA
N = int(input("Masukkan N: "))
faktor_pertama = True

print("Faktor primanya adalah ", end="")
for i in range(2, N+1):
    # pengecekan bilangan prima
    prima = True
    for j in range(2, i):
        if i % j == 0:
            prima = False
            break
    
    # pengecekan faktor bilangan N atau bukan
    if prima == True:
        if N % i == 0:
            if faktor_pertama == True:
                print(str(i), end= "")
                faktor_pertama = False
            else:
                print(f", {i}", end= "") 
print(".")