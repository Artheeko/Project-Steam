def is_schrikkeljaar(jaartal):
    if jaartal % 4 == 0 and jaartal % 100 != 0:
        return True
    else:
        return False

is_schrikkeljaar(2016)
