from collections import namedtuple

TaxBand = namedtuple("TaxBand", ["lower", "upper", "percentage"])


def LBTT_Calculator(price):

    tax_bands_default = [
        TaxBand(0, 145000, 0),
        TaxBand(145000, 250000, 2),
        TaxBand(250000, 325000, 5),
        TaxBand(325000, 750000, 10),
        TaxBand(750000, float("inf"), 12),
    ]

    if price < 0:
        raise ValueError("Negative price input")

    tax = 0
    for lower, upper, percentage in tax_bands_default:
        tax += min(max(price - lower, 0), upper - lower) * percentage / 100

    return tax


if __name__ == "__main__":
    print(LBTT_Calculator(500000))
