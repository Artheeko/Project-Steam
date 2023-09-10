# Schrijf een for-loop die langs alle letters van een string loopt en de letter uitprint,
# maar alleen als het een klinker is ('aeiou').

s = "Guido van Rossum heeft programmeertaal Python bedacht."
#i = ['a', 'e', 'i', 'o', 'u']
for i in s:
    if i in 'aeiou':
        print(i)
