kenar1 = int(input('Üçgenin birinci kenar uzunluğu : '))

kenar2 = int(input('Üçgenin ikinci kenar uzunluğu  : '))

kenar3 = int(input('Üçgenin üçüncü kenar uzunluğu  : '))

if kenar1 == kenar2 and kenar1 == kenar3 :

   print("eşkenar")

elif kenar1 != kenar2 and kenar1 != kenar3 and kenar2 != kenar3 :

   print("çeşitkenar")

else :

   print("ikizkenar")