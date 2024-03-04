a = float(input("Insira o valor de a: "))
b = float(input("Insira o valor de b: "))
c = float(input("Insira o valor de c: "))

primeiraRaiz = (-b + (b ** 2 - 4 * a * c) ** (1 / 2)) / (2 * a)
segundaRaiz = (-b - (b ** 2 - 4 * a * c) ** (1 / 2)) / (2 * a)

print("A primeira raíz da equação é: ", primeiraRaiz)
print("A segunda raíz da equação é: ", segundaRaiz)