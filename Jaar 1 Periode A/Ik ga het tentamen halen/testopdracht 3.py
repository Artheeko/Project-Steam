invoer = input('Voer hier een string in: ')
invoer = invoer.lower()

reverse = reversed(invoer)
if invoer == reverse:
    print('dit is een palingdroom')
else:
    print('Dit is geen palingdroom')
