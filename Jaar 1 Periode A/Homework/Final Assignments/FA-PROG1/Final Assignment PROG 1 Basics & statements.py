# De prijs van het gekozen product: 72
# Het betaalde bedrag: 200

# aantal munten van 50 eurocent is 2
# aantal munten van 20 eurocent is 1
# aantal munten van 10 eurocent is 0
# aantal munten van 5 eurocent is 1
# aantal munten van 2 eurocent is 1
# aantal munten van 1 eurocent is 1


#pseudocode -
# %-operator = rest bedrag
# 72 %- 200 = -128, het rest bedrag is 128. 128 houd ik over.

product = 72
munten = [50, 20 , 10 , 5 ,2 , 1]

betaald = int (input('Voer hier uw munten in'))
line1 = 'U heeft' ' '+ str(betaald) + ' '  'eurocent ingeworpen'
print(line1)

rest = (betaald - product)
if product < betaald:
    line2 = ('U heeft genoeg munten ingeworpen.')
    line3 = ('U krijgt ' ' '+ str(rest) +' ' ' eurocent terug.')
    print(line2)
    print(line3)

else:
    line3 = 'U heeft niet genoeg munten ingeworpen'
    print('Voer nu het restrerend bedrag in')

rest1 = (rest % munten[0])
overige = rest // munten[0]
rest2 = (rest1 % munten[1])
overige1 = rest // munten[1]
rest3 = (rest1 % munten[2])
overige2 = rest // munten[2]
rest4 = (rest1 % munten[3])
overige3 = rest // munten[3]
rest5 = (rest1 % munten[4])
overige4 = rest // munten[4]

print(overige)
print(rest1)
print(overige1)
print(rest2)
print(overige2)
print(rest3)
print(overige3)
print(rest4)
print(overige4)
print(rest5)
