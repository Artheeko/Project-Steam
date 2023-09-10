# vraag de gebruiker om 3 getallen in te voeren en print vervolgens de getallen van groot naar klein.

#step1
getal1 = float(input())
getal2 = float(input())
getal3 = float(input())

#step2

lst = [getal1, getal2, getal3]
lst.sort()
lst.reverse()



for i in lst:
    print(i)
