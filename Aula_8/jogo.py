from random import randint


def main():
    vida_aventureiro = 100
    ataque_aventureiro = randint(10, 20)
    defesa_aventreiro = randint(1, 5)
    vida_monstro = randint(60, 80)
    ataque_monstro = randint(20, 30)
    rodada = 1
    print("=" * 20)
    print("Aventureiro:", "vida", vida_aventureiro, "- atk", ataque_aventureiro, "- def", defesa_aventreiro)
    print("Monstro:", "vida", vida_monstro, "- atk", ataque_monstro)
    print("Rodada", rodada)
    while vida_aventureiro > 0 and vida_monstro > 0:
        rodada = rodada + 1
        print("=" * 20)
        print("Aventureiro:", "vida", vida_aventureiro, "- atk", ataque_aventureiro, "- def", defesa_aventreiro)
        print("Monstro:", "vida", vida_monstro, "- atk", ataque_monstro)
        print("Rodada", rodada)
        vida_monstro = vida_monstro - randint(1, ataque_aventureiro)
        if vida_monstro <= 0:
            print("O monstro morreu")
            break
        dano_monstro = randint(1, ataque_monstro) - defesa_aventreiro
        if dano_monstro <= 0:
            vida_aventureiro = vida_aventureiro
        else:
            vida_aventureiro = vida_aventureiro - dano_monstro
        if vida_aventureiro <= 0:
            print("O aventureiro morreu")
            break


main()
