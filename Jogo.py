from Palavra import Palavra 
from Jogador import Jogador

class Jogo():

    def __init__(self, letras_erradas=[],letras_certas=[]):
        self.letras_erradas = letras_erradas
        self.letras_certas = letras_certas

    def layout(self):
        '''to do'''
        #printar a forca e a palavra escondida aqui
        print('to do')



    def main(self):
        while True:
            dificuldade = input('''Defina a dificuldade:
- fácil
- médio
- dificil
> ''').lower()
            if dificuldade=='fácil' or dificuldade=='médio' or dificuldade=='dificil':
                break
            else:
                print('Opção Inválida')

        palavra_chute = Palavra.gerarPalavra(dificuldade)
        jogador=Jogador(6)

        while True:
            if jogador.getVida()<=0:
                print('Você perdeu :(')
                break
            else:
                self.layout()
                while True:
                    chute = input('''Digite o chute:
> ''')
                    if len(chute)<1:
                        print('Você deve digitar algo')
                    elif len(chute)==1:
                        if Palavra.temLetra(chute):
                            self.letras_certas.append(chute)
                        else:
                            self.letras_erradas.append(chute)
                    else:
                        if Palavra.verificaChutePalavra():
                            ...
                        else:
                            ...