leeftijd = int(input('Geef je leeftijd: '))
paspoort = str(input('Nederlands paspoort: '))

ja = ('JA', 'Ja', 'jA', 'ja')

if leeftijd >= int(18) and paspoort in ja:
    print('Gefeliciteerd, je mag stemmen!')
else: print('U mag niet stemmen')
