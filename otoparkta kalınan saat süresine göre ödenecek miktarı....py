kalmaSaat = int(input("Oto parkta kaç saat kaldınız: "))

if(kalmaSaat > 5):
    islem = (kalmaSaat - 5)*4
    print("Ödenecek tutar;", str(islem))
elif(kalmaSaat > 1):
    islem2 = kalmaSaat*3
    print("Ödenecek tutar;", str(islem2))
else:
    print("Ödenecek tutar; 5")
