anoBissexto = int(input("Insira um ano: "))

if anoBissexto % 400 == 0 or anoBissexto % 4 == 0 and anoBissexto % 100 != 0:
    print(True)
else:
    print(False)
