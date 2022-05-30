print("===============================================")
print("           Pengecekan Tahun Kabisat            ")
print("===============================================")

tahun = int (input("Masukan Tahun yang akan di cek : "))

if (tahun % 4) == 0:
    if (tahun % 100) == 0:
        if (tahun % 400) == 0:
            print (tahun,"Merupakan tahun kabisat")
        else :
            print (tahun,"Merupakan bukan tahun kabisat")
    else : 
        print (tahun,"Merupakan tahun kabisat")
else :
    print (tahun,"Merupakan bukan tahun kabisat")      
print("===============================================") 