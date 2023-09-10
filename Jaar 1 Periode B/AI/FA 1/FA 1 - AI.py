# TODO: Vul hier je naam, klas en studentnummer in.
naam = "Jamiro"
klas = "v1H"
studentnummer = 1815432


def is_even(n):
    """
    Bepaal of een getal even is.

    Args:
        n (int): Een geheel getal.

    Returns:
        bool: True als even, False als oneven.
    """
    n = n % 2
    if n == 0:
        return True
    else:
        return False


def floor(real):
    """ Bepaal het grootste gehele getal (int), dat kleiner dan of gelijk is aan real (float). """
    return int(real // 1)


def ceil(real):
    """ Bepaal het kleinste gehele getal (int), groter dan of gelijk aan real (float). """
    return int(-1 * real // 1 * -1)


def div(n):
    """
    Bepaal alle delers van een geheel getal.

    Het positieve gehele getal a is een deler van n, als er een positief geheel getal b is, zodat a × b = n.

    Args:
        n (int): Een geheel getal.

    Returns:
        list: Een gesorteerde lijst met alle delers van `n`.
    """

    divisors = []

    for p in range(1, n + 1):
        if n % p == 0:
            divisors.append(p)

    return sorted(divisors)


def is_prime(n):
    """
    Bepaal of gegeven getal een priemgetal is.

    Hint: maak gebruik van de functie `div()`.
    Optioneel: bedenk een efficiënter alternatief.

    Args:
        n (int): Een geheel getal.

    Returns:
        bool: True als het getal een priemgetal is, anders False.
    """
    div(n)
    if len(div(n)) == 2:
        return True
    else:
        return False


def primes(num):
    """
    Bepaal alle priemgetallen kleiner dan een bepaald geheel getal.

    Hint: Maak gebruik van de functie `is_prime()`.

    Args:
        num (int): Een geheel getal.

    Returns:
        list: Een gesorteerde lijst met alle priemgetallen kleiner dan `num`.
    """
    is_prime(n)

    primelist = []
    return sorted(primelist)


def primefactors(n):
    """
    Bepaal de verzameling van priemfactoren van n.

    Args:
        n (int): Een geheel getal.

    Returns:
        list: Een gesorteerde lijst met alle priemfactoren van n. Als n kleiner
            dan 2, retourneer dan een lege lijst `[]`.
    """
    factors = []
    return sorted(factors)


def gcd(a, b):
    """
    Bepaal de grootste grootste gemene deler (ook wel 'greatest common divisor', gcd) van twee natuurlijke getallen.

    Je hebt twee opties voor deze opgave:
    1.  Je programmeert hier het algoritme van Euclides.
        Zie: https://nl.wikipedia.org/wiki/Algoritme_van_Euclides
    2.  Je bedenkt zelf een oplossing waarbij je gebruik maakt van de eerder
        geschreven methode div(n) om de gcd te bepalen.

    Args:
        a (int): Een geheel getal.
        b (int): Een geheel getal.

    Returns:
        int: De grootste grootste gemene deler.
    """
    return


def lcm(a, b):
    """
    Bepaal het kleinste gemene veelvoud, kgv (ook wel 'least common multiple', lcm) van twee natuurlijke getallen.

    Args:
        a (int): Een geheel getal.
        b (int): Een geheel getal.

    Returns:
        int: Het kleinste gemene veelvoud.
    """
    return


def add_frac(n1, d1, n2, d2):
    """Sommeer twee breuken als breuk. Vereenvoudig de breuk zover als mogelijk.

    Args:
        n1 (int): De teller van de eerste breuk.
        d1 (int): De noemer van de eerste breuk.
        n2 (int): De teller van de tweede breuk.
        d2 (int): De noemer van de tweede breuk.

    Returns:
        tuple: De som *als breuk*, met eerst de teller en dan de noemer van het resultaat.

    Examples:
        Gegeven 1/3 + 1/5 = 8/15, dan

        >> add_frac(1, 3, 1, 5)
        (8, 15)

        Gegeven 1/2 + 1/4 = 3/4, dan

        >> add_frac(1, 2, 1, 4)
        (3, 4)

        Gegeven 2/3 + 3/2 = 13/6, dan

        >> add_frac(2, 3, 3, 2)
        (13, 6)
    """
    return 1, 1
