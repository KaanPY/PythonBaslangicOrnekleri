# liste ile sayilar2=[21,22,23,24,25] listesini birleştirerek 4’e tam bölünen sayıları ekrana yazdırınız.

sayilar=[10,11,12,13,14,15,16,17,18,19,20]
sayilar2=[21,22,23,24,25]

sayilar.extend(sayilar2)

for sayi in(sayilar):
    if(sayi % 4 == 0):
        print(sayi)
