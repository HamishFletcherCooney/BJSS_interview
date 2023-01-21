TYPES = {
    'RESIDENTIAL': 0,
    'COMMERSIAL CONVEYENCE': 1,
    'COMMERSIAL LEASE' : 2
}


def LBTT_Tax_Bands(res_type, FTB=False, ADS=False):
    tax_bands = [
        (0, 145000, 0),
        (145000, 250000, 2),
        (250000, 325000, 5),
        (325000, 750000, 10),
        (750000, 999999999999, 12),
    ]
    return tax_bands

def LBTT_Calculator(price,tax_bands):
    # tax bands format(lower,inclusive upper bound,percentage)
    
    tax = 0
    for lower, upper, percentage in tax_bands:
        tax += min(max(price - lower, 0), upper - lower) * percentage / 100

    return tax


def test_LBTT():
    tax_bands=LBTT_Tax_Bands(TYPES['RESIDENTIAL'])
    assert LBTT_Calculator(-37,tax_bands) == 0
    assert LBTT_Calculator(0,tax_bands) == 0
    assert LBTT_Calculator(500000,tax_bands) == 23350
    assert LBTT_Calculator(1000000,tax_bands) == 78350
    #assert False
