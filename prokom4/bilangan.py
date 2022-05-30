print("==============================================================================================================")
print("                                         Program Bilangan Ganjil Genap                                        ")
print("==============================================================================================================")

even_count, odd_count = 0, 0
even_list = []
odd_list = []
n = int(input("Masukan nilai awal : "))
m = int(input("Masukan nilai akhir : "))

for i in range(n,m+1):
    if i % 2 == 0:
        even_count += 1
        even_list.append(i)
    else:
        odd_count += 1
        odd_list.append(i)

print("Jumlah bilangan genap dari {0} sampai {1} adalah {2}".format(n, m,even_count), "dan angkanya adalah", even_list)
print("Jumlah bilangan ganjil adalah {0} sampai {1} adalah {2}".format(n,m,odd_count), "dan angkanya adalah", odd_list)
print("==============================================================================================================")

