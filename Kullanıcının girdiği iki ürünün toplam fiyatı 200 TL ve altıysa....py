# Kullanıcının girdiği iki ürünün toplam fiyatı 200 TL ve altıysa “Ödenecek miktar=…. TL”; 200 TL’yi geçerse
# %25 indirim yaparak “Ödenecek miktar, indirimden sonra ….. TL’dir.” çıktılarını veren kodu yazınız.

urunBir = int(input("1.Ürün fiyatını giriniz: "))
urunİki = int(input("2.Ürün fiyatını giriniz: "))

toplam = urunBir+urunİki

if(toplam <= 200):
    print("Ödeme tutarınız:",str(toplam), "TL")
else:
    indirim = ((100 - 12) / 100)*toplam
    print("Tebrikler!, 200TL Üstü Alışverişinizden %25 İndirim Kazandınız\nToplam Ödeyeceğiniz Miktar:",str(indirim), "TL")
