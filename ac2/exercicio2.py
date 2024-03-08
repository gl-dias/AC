def calcula_salario(valor_hora, num_horas):
    irpf = 0.275
    return (valor_hora * num_horas) * irpf

def main():
    print(calcula_salario(15, 8))

main()