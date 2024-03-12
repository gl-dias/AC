def determina_tipo_triangulo(a, b, c):
    if a + b < c or a + c < b or b + c < a:
        return "Não é um triângulo"
    elif a == b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"
    
def testa_triangulo():
    print(determina_tipo_triangulo(4, 4, 4))
    print(determina_tipo_triangulo(2, 4, 4))
    print(determina_tipo_triangulo(3, 4, 5)) 
    print(determina_tipo_triangulo(1, 1, 4))

testa_triangulo()