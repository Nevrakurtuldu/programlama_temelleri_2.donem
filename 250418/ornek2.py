saat=int(input("otoparkta kaç saat kaldını = "))

if saat <1:
    print("1 saate 5 TL")
elif saat>1 and saat<5:
    print("ödenecek tutar",saat*4)
elif saat>5:
    print("ödenecek tutar",saat*3)
else:
    print("geçersiz")