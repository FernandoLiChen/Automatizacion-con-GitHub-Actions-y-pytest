def calcular_area_triangulo(base, altura):
    if base < 0 or altura < 0:
        return False
    if base == 0:
        return False
        
    return (base * altura) / 2 