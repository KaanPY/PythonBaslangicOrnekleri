# Bir firma işe alımlarda 40 yaş altı kişileri tercih etmektedir. Bu şartı sağlayan kişilerde de sürücü
# belgesi olan üniversite mezunlarını tercih etmektedir. Buna göre kullanıcıya önce yaş sorulsun.
# Yaşı 40 iki soruyu sorarak ise alınıp alınmadıklarını çıktı olarak veren kodu yaznınız.

yas = int(input("Yaşınız?: "))

if(yas >= 40):
    print("Üzgünüz 40 yaş altı kişiler tercih edilmektedir.")
else:
    ehliyet = input("Ehliyetiniz var mı? E/H: ")
    mezun = input("Üniversiteden mezun musunuz? E/H: ")
    
    if(ehliyet == "E" and mezun == "E"):
        print("İşe alındınız!")
    else:
        print("Üzgünüz!")
