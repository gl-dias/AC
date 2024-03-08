def eq_seg_grau(a, b, c):
    delta = b ** 2 - 4 * a * c
    raiz1 = (-b + (delta ** (1/2))) / (2 * a)
    raiz2 = (-b - (delta ** (1/2))) / (2 * a)
    return raiz1, raiz2

def bissexto(ano):
    if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
        return True
    return False

def main():
    print(bissexto(1900))
    print(bissexto(2000))
    print(eq_seg_grau(2, 16, 3))
    print(eq_seg_grau(1, -6, 8))
    
main()