def C_to_F(cel):
    faren = (cel * 9/5) + 32
    return faren

def F_to_C(faren):
    cel = (faren - 32) * (5/9)
    return cel

def C_to_K(cel):
    return (cel + 273.15)

def F_to_K(far):
    cel = F_to_C(far)
    kel = C_to_K(cel)
    return kel

def K_to_C(kel):
    return (kel - 273.15)

def K_to_F(kel):
    cel = K_to_C(kel)
    far = C_to_F(cel)
    return far