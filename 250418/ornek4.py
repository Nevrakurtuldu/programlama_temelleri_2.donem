kilo = int(input("Kilonuzu girin: "))

boy = float(input("Boyunuzu girin (): "))

vki = kilo/(boy**2)

if vki >=18 and vki <25:

   print("Normal kilolu")

elif vki >= 25 and vki <30:

   print("kilolu")

elif vki >=30 and vki <35:
   print("obez")

elif vki >=35:
    print("ciddi obez")

else:

   print("girilemedi")