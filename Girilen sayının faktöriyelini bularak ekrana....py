# Girilen sayının faktöriyelini bularak ekrana yazdırınız.

sayi = int(input("Faktöriyeli hesaplanacak sayı: "))

faktoriyel = 1

for sayilar in range(1, sayi+1):
    faktoriyel = faktoriyel*sayilar
print("Faktoriyel:", str(faktoriyel))
