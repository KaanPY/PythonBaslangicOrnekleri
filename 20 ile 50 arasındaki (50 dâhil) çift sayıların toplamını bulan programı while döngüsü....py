# 20 ile 50 arasındaki (50 dâhil) çift sayıların toplamını bulan programı while döngüsü ile yazınız.

toplam = 0
baslangic = 20

while(baslangic <= 50):
    if(baslangic % 2 ==0):
        toplam = toplam + baslangic
    baslangic = baslangic + 1
print(toplam)
