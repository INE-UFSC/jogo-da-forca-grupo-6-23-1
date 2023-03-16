from Palavra import Palavra 
from Jogador import Jogador
from unidecode import unidecode

class Jogo():

    
    
    def layout(self):
        jogador = Jogador()
        palavra = Palavra()
        print(f"""                                          

                                 Letras erradas: {self.letras_erradas}""")
        jogador.mostra_vida()     
        print(f"""                   Palavra:  {palavra.printPalavra()} """)



    def main(self):

        

        while True:
            dificuldade = unidecode(input('''Defina a dificuldade:\n- fácil \n- médio \n- dificil> ''').lower())
            if dificuldade=='facil' or dificuldade=='medio' or dificuldade=='dificil':
                break
            else:
                print('Opção Inválida')

        palavra_chute = Palavra().gerarPalavra(dificuldade)
        print(palavra_chute)
        jogador=Jogador(6)

        while True:
            if jogador.getVida()<=0:
                print('Você perdeu :(')
                break
            self.layout()
            while True:
                chute = input('Digite o chute: \n> ')
                if len(chute)<1 or chute==' ':
                    print('Você deve digitar algo')
                else:
                    break

            if len(chute)==1:
                if ...:
                    self.letras_certas.append(chute)
                else:
                    jogador.perdeVida()
                    self.letras_erradas.append(chute)
            else:
                if ....verificaChutePalavra(chute):
                    print(f'Você acertou a palavra: {palavra_chute}')
                    break
                else:
                    print('Você perdeu :(')
                    break

