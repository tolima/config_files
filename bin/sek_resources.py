one_euro_in_sek = 8.32
one_sek_in_euro = 1./one_euro_in_sek


def sek_to_euro(price_in_sek):
    return price_in_sek * one_sek_in_euro

def euro_to_sek(price_in_euro):
    return price_in_euro * one_euro_in_sek
