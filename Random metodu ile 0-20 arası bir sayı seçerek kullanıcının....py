# Random metodu ile 0-20 arası bir sayı seçerek kullanıcının bu sayıyı tahmin etmesini isteyiniz. Kullanıcının
# tahminine göre arttır ve azalt şeklinde uyarılar verdirerek doğru sonuca ulaşılmasını sağlayınız.

import random

sayi = random.randint(0, 20)

tahmin = 123

print("="*5, "0 - 20 Arası Bir Sayı Seçildi!", "="*5)

while(tahmin != sayi):
    tahmin = int(input("Tahmininiz?: "))

    if(tahmin < sayi ):
        print("> Tahmini Arttır")
    elif(tahmin > sayi):
       print("> Tahmini Azalt")
    else:
        print("Tebrikler!, tahmininiz doğru!:", sayi)

"""
> Gelişmiş

import random

randomSayi = random.randint(1,10)
userHak = 5
userTahmin = 123
playLoop = 12

while(True):
    userTahmin = int(input(f'Kalan hakkınız: {userHak} | Tahmininiz: '))
    userHak -= 1
    if(userHak < 1):
        playLoop = input(f'Hakkınız bitti! Tutulan sayı: {randomSayi}, tekrar oynamak ister misiniz? (E/H): ')
        if(playLoop == 'E'):
            randomSayi = random.randint(1,100)
            userHak = 5
            userTahmin = 123
        elif(playLoop == 'H'):
            print('Oyundan çıkılıyor...')
            break       
    elif(userTahmin > randomSayi):
        print('Azalt')
    elif(userTahmin < randomSayi):
        print('Arttır')
    else:
        playLoop = input(f'Kazandınız! | Puanınız: {(userHak*20)+20}, tekrar oynamak ister misiniz? (E/H): ')
        if(playLoop == 'E'):
            randomSayi = random.randint(1,100)
            userHak = 5
            userTahmin = 123
        elif(playLoop == 'H'):
            print('Oyundan çıkılıyor...')
            break

"""
