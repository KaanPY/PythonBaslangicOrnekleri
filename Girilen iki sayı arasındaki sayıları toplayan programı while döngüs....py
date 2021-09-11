# Girilen iki sayı arasındaki sayıları toplayan programı while döngüsü ile ekrana yazınız.

sayi = int(input("Sayı bir giriniz: "))
sayi2 = int(input("Sayı iki giriniz: "))

toplam = 0

while(sayi <= sayi2):
    toplam = toplam + sayi
    sayi = sayi + 1
print(toplam)
