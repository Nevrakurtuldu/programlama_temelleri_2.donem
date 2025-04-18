kg=int(input("ağırlık giriniz"))
if kg <=10:
    islem=kg*10
    print("tutarınız",islem)

else:
    islem= 100+(kg-10)*7.5
    print("tutarınız",islem)

