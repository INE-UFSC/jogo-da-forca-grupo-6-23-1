from Jogo import Jogo
from unidecode import unidecode

comecar = Jogo()
while True:
    comecar.main()
    while True:
        continuar = unidecode(input('Deseja Continuar?\n- Sim\n- Não\n> ').lower())
        if continuar=='nao' or continuar=='n' or continuar=='sim' or continuar=='s':
            break
    if continuar=='nao' or continuar=='n':
        break