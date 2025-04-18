hava_sicakliği=int(input("sıcaklık gir = "))
if hava_sicakliği <=5:
    print("soğuk")
elif hava_sicakliği >=6 and hava_sicakliği <14:
    print("ılık")
elif hava_sicakliği>=15:
    print("sıcak")
else:
    print("yanlış derece")