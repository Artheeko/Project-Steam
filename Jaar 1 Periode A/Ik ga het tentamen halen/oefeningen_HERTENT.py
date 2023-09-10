# vraag de gebruiker om 3 getallen in te voeren en print vervolgens de getallen van groot naar klein.

"""
cijfer1 = float(input())
cijfer2 = float(input())
cijfer3 = float(input())

lst = [cijfer1, cijfer2, cijfer3]

lst.sort()
lst.reverse()
print(lst)
"""

'''
FEEDBACK:


dit gaat bijna helemaal goed, het enige is dat je print nu de lst uit dus de lijst.

als ik dit zo zie zou ik het goed keuren maar, het is veiliger omte doen.

print(lst[0])
print(lst[1])
print(lst[2])

of 


for cijfer in lst:
    print(cijfer)

'''

# vraag de gebruiker een aantal minuten, print vervolgens het aantal uren en print de resterende minuten in seconden.
"""
minuten = int(input('Voer uw minuten in: '))

uren = minuten // 60
print(f'het aantal uren is: {uren}')

restMin = uren * 60
print(f'de restrerende minuten in seconden zijn zijn {restMin}')
"""


'''
FEEDBACK

uren *60 geeft niet de rest minuten maar juist de hoeveel heid uren in minuut.


dus je wilt eigenlijk hebben oke 

stel 130 min.

dan is het 130//60 = 2 uur

dus dan is het just restmin =130(input van minuten) - 2*60 

of mooier denk als :

+ en -
* en /
het is : % en //

want 130 % 60  == 130 - 60 * (aantal uren)
'''

# maak een functie waarbij inch als parameter word ingevoerd het aantal cm berekend. 1 inch=2.54cm
"""
def inchToCm(inch):
    conv = inch * 2.54
    print(conv)
inchToCm(2)
"""

'''

FEEDBACK
er staat nergens dat je moet printen:

dus het is veiliger om te returnen 
def inchToCM(inch):
    ....
    return conv

'''

# vraag de gebruiker om een string en print vervolgens alleen de klinkers naast elkaar

"""
istring = str(input('Voer hier een string in: '))
klinkers = ['a', 'e', 'o', 'u', 'i']
for letter in istring:
    if letter in klinkers:
        print(letter)
"""

'''
FEEDBACK:

nice, maar input geeft altijd een string, dus je hoeft niet het ook nog is naar een str te converteren.

'''

#uuuh
"""
vraag de gebruiker om een getal tussen de 1 en de 100, genereer ook een random getal tussen de 1 en de 100.
als het ingevoerde getal niet overeenkomt met het willekeurige getal vraag je een nieuw getal en gaat er 1 punt van de score af tot dat het getal geraden is.  je begint met een score van 100.
#print vervolgens de score als het getal geraden is.
"""



# Voor morgen....

# Schrijf een programma waarin de gebruiker drie getallen kan inullen. Print vervolgens het middelste (que grootte) getal.

"""
getal1 = float((input('Voer hier het 1e getal in: ')))
getal2 = float((input('Voer hier het 2e getal in: ')))
getal3 = float((input('Voer hier het 1e getal in: ')))

lijst = [getal1, getal2, getal3]
lijst.sort()
print(lijst[1])
"""

# Schrijf een programma waarin je de gebruiker een string laat invoeren. Gebruik vervolgens een for-loop om de omgekeerde string te printen.

invoer = str(input('Voer een string in: '))
for letter in invoer:
    print(letter, end='')



# Schrijf een programma waarin een gebruiker getallen moet invoeren. Dit gaat door totdat de gebruiker 'stop' intoetst. De getallen moeten met elkaar vermenigvuldigd worden. Print het resultaat.
# Schrijf een functie isPositiefEnKleinerDan(x, y) waarin je bepaalt of gegeven getal 'x' een positief getal is, en kleiner dan getal 'y'. De parameters x en y zijn van het type int. De functie geeft True terug als dat zo is, anders False.




