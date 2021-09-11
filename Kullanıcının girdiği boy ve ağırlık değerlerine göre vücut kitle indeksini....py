# Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ=ağırlık/(boy*boy), boy
# metre cinsinden verilmeli) hesaplayınız.

kilo = float(input('Kilonuzu giriniz: '))
boy = float(input('Boyunuzu giriniz: '))

hesap = (kilo) / (boy**2)

if((hesap >= 0) and (hesap <= 18.4)):
    print(f'Vücut kitle indeksiniz: {hesap:1.5} Zayıf!')
elif((hesap >= 18.5) and (hesap <= 24.9)):
    print(f'Vücut kitle indeksiniz: {hesap:1.5} Normal!')
elif((hesap >= 25) and (hesap <= 29.9)):
    print(f'Vücut kitle indeksiniz: {hesap:1.5} Fazla Kilolu!')
elif((hesap >= 30) and (hesap <= 39.9)):
    print(f'Vücut kitle indeksiniz: {hesap:1.5} Obez!')
elif(hesap >= 40):
    print(f'Vücut kitle indeksiniz: {hesap:1.5} İleri Derecede Obez (MORBİD)!')
else:
    print('Hatalı değer')
