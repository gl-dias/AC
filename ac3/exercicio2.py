def dia_semana(num):
    num <= 7
    match num:
        case 1:
            return "domingo"
        case 2:
            return "segunda"
        case 3:
            return "terça"
        case 4:
            return "quarta"
        case 5:
            return "quinta"
        case 6:
            return "sexta"
        case 7:
            return "sábado"
        case _:
            return 
        

def testa_dia_semana():
    print(dia_semana(2)) 
    print(dia_semana(6)) 
    print(dia_semana(7)) 
    print(dia_semana(9)) 

testa_dia_semana()