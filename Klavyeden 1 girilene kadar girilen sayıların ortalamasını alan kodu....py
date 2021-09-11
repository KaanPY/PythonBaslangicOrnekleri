# Klavyeden 1 girilene kadar girilen sayıların ortalamasını alan kodu yazınız.

toplam=0
sayi=1
bolme = 0

while (sayi!=0):
    sayi=int(input("Bir sayı giriniz: "))
    toplam=toplam+sayi
    bolme = bolme + 1
ortalama = toplam/bolme
print("Sonuc=",toplam)
