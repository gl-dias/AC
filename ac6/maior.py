valor1 = input()
valor1 = valor1.split(" ")
a,b,c = valor1 

maior = (int(a) + int(b) + abs(int(a) - int(b)))  / 2
resultado = (int(maior) + int(c) + abs(int(maior) - int(c))) / 2

print(int(resultado), "eh o maior")