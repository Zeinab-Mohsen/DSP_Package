def validate_num(P):
    if P == "" or P == "-":
        return True

    try:
        float(P)
        return True
    except ValueError:
        return False
