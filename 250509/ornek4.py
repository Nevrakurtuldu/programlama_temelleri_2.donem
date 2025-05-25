ifade=input("bir metin giriniz")
toplam=0
for aranan in ifade:
    if aranan=="a":
        toplam=toplam+1
print("bu metinde toplam",toplam,"adet a vardır")