# Girilen sayı hem 3 hem de 5'e tam bölünüyorsa "15'e tam bölünür."; bölünmüyorsa "15'e tam
# bölünmüyor çıktılarını veren kodu yazınız.

sayi = int(input("Sayı giriniz: "))

if(sayi % 3 == 0 and sayi % 5 == 0):
    print("sayı 15'e tam bölünüyor!")
else:
    print("sayı 15'e tam bölünmüyor!")
