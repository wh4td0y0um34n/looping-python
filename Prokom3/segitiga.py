print("============================================================================")
print("                     Program Menentukan Jenis Segitiga                      ")
print("============================================================================")

sisiX = int(input("Masukan sisi X : "))
sisiY = int(input("Masukan sisi Y : "))
sisiZ = int(input("Masukan sisi Z : "))

if ((sisiX == 0) | (sisiY == 0) | (sisiZ == 0)):
    print("Jika sisi x,y,z = ",sisiX,",",sisiY,",",sisiZ,"adalah bukan segitiga")
elif ((sisiX == sisiY) & (sisiZ == sisiX)):
    print("Jika sisi x,y,z = ",sisiX,",",sisiY,",",sisiZ,"adalah segitiga sama sisi")
elif((sisiX == sisiY) | (sisiX == sisiZ) | (sisiY == sisiZ)):
    print("Jika sisi x,y,z = ",sisiX,",",sisiY,",",sisiZ,"adalah segitiga sama kaki")
else:
    print("Jika sisi x = ",sisiX,",",sisiY,",",sisiZ,"adalah segitiga sembarang")

print("============================================================================")