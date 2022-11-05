print("Program mengurutkan data")
def angka_terbesar(a, b, c):
    if a > b or b > c:
        return a
    elif b > a or b > c:
        return b
    return c  
def angka_terkecil(a, b, c):
    if a < b or b < c:
        return a
    elif b < a or b < c:
        return b
    return c  
def nilai_tengah(a, b, c):
    if(b > a > c) or (c > b > a):
        return a
    elif (a > b > c) or (c > b > a):
        return b
    return c 
a, b, c = (
    int(input("Masukkan bilangan :")),
    int(input("Masukkan Bilangan :")),
    int(input("Masukkan Bilangan :"))
)
i1 = angka_terkecil(a, b, c)
i2 = nilai_tengah(a, b, c)
i3 = angka_terbesar(a, b, c)
print(f'Urutan bilangan: {i1}, {i2}, {i3}')