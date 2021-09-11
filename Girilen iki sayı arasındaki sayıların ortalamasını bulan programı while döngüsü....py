# Girilen iki sayı arasındaki sayıların ortalamasını bulan programı while döngüsü ile yazınız.

sayi = int(input("Sayı bir giriniz: "))
sayi2 = int(input("Sayı iki giriniz: "))

toplama = 0

i = sayi

while(i <= sayi2):
    toplama = toplama + i
    i = i + 1

islem = toplama/(sayi2-sayi+1)
print(islem)
