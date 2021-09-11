# Kullanıcıdan kullanıcı adı ve şifre girilmesi istensin. Kullanıcı adı “Türkiye”; şifre 1923 ise “Giriş başarılı”;
# değilse “Kullanıcı adı ya da şifre yanlış” çıktıları veren kodu yazınız.

kullaniciAdi = input("Kullanıcı adını giriniz: ")
sifre = input("Şifrenizi giriniz: ")

if((kullaniciAdi == "Türkiye") and (sifre == "1923")):
    print("Giriş başarılı")
else:
    print("Kullanıcı adı veya şifre yalnış")
