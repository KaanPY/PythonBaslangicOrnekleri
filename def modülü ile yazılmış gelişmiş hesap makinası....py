# def modülü ile yazılmış gelişmiş hesap makinası!

def toplama(sayi1, sayi2):
    return sayi1 + sayi2
def cikarma(sayi1, sayi2):
    return sayi1 - sayi2
def carpma(sayi1, sayi2):
    return sayi1 * sayi2
def bolme(sayi1, sayi2):
    return sayi1 / sayi2

while(True):

    print('1.Toplama | 2.Çıkartma | 3.Çarpma | 4.Bölme | q.Çıkış')
    islemSecim = input('İşlem seçiniz: ')
    
    if(islemSecim == 'q'):
        print('Hesap Makinasından Çıkılıyor...')
        break
    
    sayi1 = int(input('\n1.Sayı giriniz: '))
    sayi2 = int(input('2.Sayı giriniz: '))
    
    if(islemSecim == '1'):
        print(f'\n{sayi1} + {sayi2} = {toplama(sayi1, sayi2)}\n' + '='*30)
    elif(islemSecim == '2'):
        print(f'\n{sayi1} - {sayi2} = {cikarma(sayi1, sayi2)}\n' + '='*30)
    elif(islemSecim == '3'):
        print(f'\n{sayi1} x {sayi2} = {carpma(sayi1, sayi2)}\n' + '='*30)
    elif(islemSecim == '4'):
        print(f'\n{sayi1} / {sayi2} = {bolme(sayi1, sayi2)}\n' + '='*30)
    else:
        print('Hatalı işlem seçtiniz... Tekrar deneyiniz!')
        break
