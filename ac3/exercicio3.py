def operaçoes_aritmeticas():
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite um outro número: "))
    operacao = str(input("Escolha uma operação: "))
    if operacao == "soma":
        print("Resultado: ", num1 + num2)
    elif operacao == "subtracao":
        print("Resultado: ", num1 - num2)
    elif operacao == "multiplicação":
        print("Resultado: ", num1 * num2)
    elif operacao == "divisão":
        print("Resultado: ", num1 / num2)
    else:
        print("operação inválida")

operaçoes_aritmeticas()