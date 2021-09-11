#Kullanıcıdan iki sınav ve bir performans notu girmesini isyetiniz.
#Girilen 3 notun ortalaması 50 ve daha büyükse "Başarılı"; değilse "başarısız" çıktıları
#veren kodu yazınız...

sinav1 = int(input("1.Not giriniz: "))
sinav2 = int(input("2.Not giriniz: "))
performans = int(input("Performans giriniz: "))

sonuc = (sinav1 + sinav2 + performans)/3

if(sonuc >= 50):
    print("Geçtiniz "+ str(sonuc))

else:
    print("Kaldınız "+ str(sonuc))
