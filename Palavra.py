import json
import random

class Palavra():
    def __init__(self):
        self.palavra_chave = ''
        self.palavra_chave_escondida = ''
    
    def gerarPalavra(self, dificuldade):
        arquivo_lista_nomes = open('./utils/lista_palavras.json', "r")
        lista_nomes = json.loads(arquivo_lista_nomes.read())

        self.palavra_chave = random.choice(lista_nomes[dificuldade])

        arquivo_lista_nomes.close()

        for letra in self.palavra_chave:
            self.palavra_chave_escondida+='_'

    def temLetra(self, chute:str):
        if len(chute)==1:
            if chute in self.palavra_chave:
                ... #revela as vezes que a letra apareceu na palavra
            else:
                ... #perde uma vida
        elif len(chute)==len(self.palavra_chave):
            if chute==self.palavra_chave:
                ... #ganhar
            else:
                ... #perder
        else:
            return "Chute inválido"

    def printPalavra(self):
        return self.palavra_chave_escondida