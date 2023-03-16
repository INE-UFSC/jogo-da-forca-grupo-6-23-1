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
            dificuldade = unidecode(input('''Defina a dificuldade:\n- fácil \n- médio \n- dificil \n- muito dificil \n> ''').lower())
            if dificuldade=='facil' or dificuldade=='medio' or dificuldade=='dificil' or dificuldade=='muito dificil':
                if dificuldade=='muito dificil':
                    dificuldade='muito_dificil'
                break
            else:
                print('Opção Inválida')

        Palavra().gerarPalavra(dificuldade)
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
                if Palavra().temLetra(chute):
                    self.letras_certas.append(chute)
                else:
                    jogador.perdeVida()
                    self.letras_erradas.append(chute)
            else:
                if Palavra().verificaChutePalavra(chute):
                    print(f'Você acertou a palavra:')
                    break
                else:
                    print('Você perdeu :(')
                    break

