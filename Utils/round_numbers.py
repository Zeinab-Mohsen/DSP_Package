from decimal import Decimal, ROUND_HALF_UP


def round_with_exponent(decimal_value, exponent):
    value = Decimal(decimal_value)
    exponent_decimal = Decimal(exponent)  
    
    rounded_value = value.quantize(Decimal(1) / (Decimal(10) ** exponent_decimal), rounding=ROUND_HALF_UP)
    
    return float(rounded_value)