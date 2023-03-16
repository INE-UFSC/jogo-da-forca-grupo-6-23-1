from Palavra import Palavra 
from Jogador import Jogador

jogador = Jogador()
palavra = Palavra()
class Jogo():
  
  
  
    def __init__(self, letras_erradas=[],letras_certas=[]):
        self.letras_erradas = letras_erradas
        self.letras_certas = letras_certas

    
    
    def layout(self):
        print(f"""                                          

                                 Letras erradas: {self.letras_erradas}""")
        jogador.mostra_vida()     
        print(f"""                   Palavra:  {palavra.printPalavra()} """)



    def main(self):
        self.layout()

        