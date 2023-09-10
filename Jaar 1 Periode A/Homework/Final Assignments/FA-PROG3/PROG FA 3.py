file = "Kluizen.txt"
readtxt = open(file)
kluisregels = readtxt.readlines()
readtxt.close() #close file toegevoegd n.a.v feedback

def aantal_kluizen_vrij():
    freeLockers = 12 - len(kluisregels)
    return freeLockers
#print(aantal_kluizen_vrij())


def nieuwe_kluis():
    if aantal_kluizen_vrij() == 0:
        return -2
    newLocker = input("Geef hier de code voor uw nieuwe kluis: ")
    if ';' in newLocker:
        return -1

    all_LockerNMB = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    for nmb in kluisregels:

        kluisnummer = int(nmb[:nmb.find(';')])   # Voor elk nummer in de tekst 'kluizen.txt' print dan alle regels
                                                 # (: staat voor ':' stoppen bij ) tot ;
        all_LockerNMB.remove(kluisnummer)
        #print(kluisnummer)                      # Laat alle bezette kluisnummers zien

    new_Line = '\n' + str(all_LockerNMB[0]) + ';' + newLocker   # Begin met een ENTER en voeg daar het volgende nummer toe (kluisnummer) en voeg daarachter een ; (puntcomma). newLocker is je wachtwoord wat je invoert. Dus je voegt het nieuwe wachtwoord toe aan de lijst.
    kluisregels.append(new_Line)
    #print(kluisregels)

    open_File = open('Kluizen.txt' , 'w')

    for line in kluisregels:
        open_File.write(line)

    return  all_LockerNMB[0]

#print(kluisregels)  #print alles wat in de kluis zit
#print(nieuwe_kluis())



def kluis_openen():
    kluisNummer = (input('Wat is uw kluisnummer')) #int type toegevoegd
    kluisCode = input('Wat is de code van uw kluis')

    for regel in kluisregels:
        lckrList = regel.split(';')

        if kluisNummer == lckrList[0]:
            if kluisCode == lckrList[1].strip():
                return True
            else:
                toegang = False
        else: toegang = False
    return toegang

def main():
    keuze = int(input(' 1: Ik wil weten hoeveel kluizen nog vrij zijn\n 2: Ik wil een nieuwe kluis \n 3: Ik wil even iets uit mijn kluis halen\n'))
    if keuze == 1:
        print(aantal_kluizen_vrij())
    if keuze == 2:
        print(nieuwe_kluis())
    if keuze == 3:
        print(kluis_openen())
main()
