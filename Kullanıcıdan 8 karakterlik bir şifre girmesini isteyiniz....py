# Kullanıcıdan 8 karakterlik bir şifre girmesini isteyiniz. Kullanıcı 8’den az ya da daha fazla karakter içeren bir
# şifre girdiğinde “Şifreniz 8 karakter olmalıdır.” şeklinde uyarı verdiriniz. Kullanıcı şartlara uygun bir şifre
# girdiğinde de “Şifreniz kaydedildi.” uyarısı verdiriniz.

sifre = input("Şifre giriniz: ")

while(True):
    if(len(sifre) == 8):
        print("Şifreniz kaydedildi")
        break
    sifre = input("Şifreniz 8 karakter olmalıdır: ")
