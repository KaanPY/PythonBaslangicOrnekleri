# Girilen üç sayıdan en büyüğünü bulan kodu yazınız.

sayi1 = int(input("1. Sayı giriniz: "))
sayi2 = int(input("2. Sayı giriniz: "))
sayi3 = int(input("3. Sayı giriniz: "))

if((sayi1 >= sayi2) and (sayi1 >= sayi3)):
    print(str(sayi1), "En büyük sayı")
elif((sayi2 >= sayi1) and (sayi2 >= sayi3)):
    print(str(sayi2), "En büyük sayı")
else:
     print(str(sayi3), "En büyük sayı")
