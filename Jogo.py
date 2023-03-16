from Palavra import Palavra
from Jogador import Jogador
from unidecode import unidecode


class Jogo():

    def __init__(self):
        self.letras_erradas = []
        self.letras_certas = []

    def layout(self, jogador: Jogador, palavra: Palavra):

        print(f"""                                          

                                 Letras erradas: {self.letras_erradas}""")
        jogador.mostraVida()
        print(f"""                   Palavra:  {palavra.getPalavra()} """)

    def main(self):

        while True:
            dificuldade = unidecode(input(
                '''Defina a dificuldade:\n- fácil \n- médio \n- dificil \n- muito dificil \n> ''').lower())
            if dificuldade == 'facil' or dificuldade == 'medio' or dificuldade == 'dificil' or dificuldade == 'muito dificil':
                if dificuldade == 'muito dificil':
                    dificuldade = 'muito_dificil'
                break
            else:
                print('Opção Inválida')

        jogador = Jogador(6)
        palavra = Palavra()
        palavra.gerarPalavra(dificuldade)

        while True:
            if jogador.getVida() <= 0:
                print('Você perdeu :(')
                break
            self.layout(jogador, palavra)
            while True:
                chute = input('Digite o chute: \n> ')
                if len(chute) < 1 or chute == ' ':
                    print('Você deve digitar algo')
                else:
                    break

            if len(chute) == 1:
                if palavra.temLetra(chute):
                    self.letras_certas.append(chute)
                else:
                    jogador.perdeVida()
                    self.letras_erradas.append(chute)
            else:
                if palavra.verificaChutePalavra(chute):
                    print(f'Você acertou a palavra:')
                    break
                else:
                    print('Você perdeu :(')
                    break
