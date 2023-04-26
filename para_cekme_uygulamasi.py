sahip_olunan_miktar = 2000
secim = 0
while secim != 4:
    print("1)Para Çekme\n2)Para Yatırma\n3)Kart Bilgileri\n4)Kart İade")
    secim = int(input("Secim yapiniz: "))
    if secim == 1:
        cekilecek_miktar = int(input("Mevcut Miktar: {} Cekilecek miktari giriniz: ".format(sahip_olunan_miktar)))
        if sahip_olunan_miktar < cekilecek_miktar:
            print("Yeterli bakiye mevcut değil")
        else:
         sahip_olunan_miktar = sahip_olunan_miktar - cekilecek_miktar
         print("Cekilen miktar: {} kalan miktar: {} ".format(cekilecek_miktar,sahip_olunan_miktar))
    elif secim == 2:
        yatirilacak_miktar = int(input("Ne kadar para yatırmak istiyorsunuz?: "))
        sahip_olunan_miktar = sahip_olunan_miktar + yatirilacak_miktar
        print("Yatırılan miktar: {} Mevcut miktar: {}".format(yatirilacak_miktar,sahip_olunan_miktar))
    elif secim == 3:
        print("Hesap Durumu:{}".format(sahip_olunan_miktar))
    elif secim == 4:
        print("Kartınız iade ediliyor...")
        break
    else:
        print("Yanlis secim yaptiniz tekrar deneyiniz!")
        
    



    