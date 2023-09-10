# Naam: Jamiro Kolf
# Klas: V1H
# Datum: 14-9-2022
# Pseudocode:
"""""
Het betaalde bedrag wordt afgetrokken van de prijs van het product, daarna kijkt het programma of er teveel of 
te weinig betaald is.

Als er te weinig betaald is; sluit het programma zich en vraagt het de gebruiker om het opniew te proberen.
Als er wel genoeg betaald is berekent het programma het overige bedrag 
(wisselgeld) in munten van 50,20,10,5,2 en 1 eurocent.
"""""

product = 72
line1 = 'De prijs van het gekozen product: ' + str(product)
print(line1)


munten = [50, 20, 10, 5, 2, 1]


betaald = int(input('Voer hier uw munten in: '))
line2 = 'Het betaalde bedrag:' ' ' + str(betaald)
print(line2)
rest = (betaald - product)

if product < betaald:
    ingeworpen = 'U heeft genoeg munten ingeworpen.'
    terug = ('U krijgt ' ' ' + str(rest) + ' ' ' eurocent terug.')
    print(ingeworpen)
    print(terug)

else:
    nietGng = 'U heeft niet genoeg munten ingeworpen, probeer het opnieuw.'
    print(nietGng)
    exit()


vijftigC = rest // munten[0]
teruggave = rest % munten[0]
line3 = 'aantal munten van ' + str(munten[0]) + ' ''eurocent is ' + str(vijftigC)
print(line3)


twintigC = teruggave // munten[1]
teruggave = teruggave % munten[1]
line4 = 'aantal munten van ' + str(munten[1]) + ' ''eurocent is ' + str(twintigC)
print(line4)


tienC = teruggave // munten[2]
teruggave = teruggave % munten[2]
line5 = 'aantal munten van ' + str(munten[2]) + ' ''eurocent is ' + str(tienC)
print(line5)


vijfC = teruggave // munten[3]
teruggave = teruggave % munten[3]
line6 = 'aantal munten van ' + str(munten[3]) + ' ''eurocent is ' + str(vijfC)
print(line6)


tweeC = teruggave // munten[4]
teruggave = teruggave % munten[4]
line7 = 'aantal munten van ' + str(munten[4]) + ' ''eurocent is ' + str(tweeC)
print(line7)


eenC = teruggave // munten[5]
teruggave = teruggave % munten[5]
line8 = 'aantal munten van ' + str(munten[5]) + ' ''eurocent is ' + str(eenC)
print(line8)

print('Dankuwel voor uw komst, fijne dag!')
