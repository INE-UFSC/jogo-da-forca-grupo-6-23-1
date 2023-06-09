import json
import random

class Palavra():
    
    def __init__(self):
        self.palavra_chave = ''
        self.palavra_chave_escondida = ''

    def getTamanhoPalavra(self):
        return len(self.palavra_chave)
    
    def gerarPalavra(self, dificuldade):
        arquivo_lista_nomes = open('./utils/lista_palavras.json', "r")
        lista_nomes = json.loads(arquivo_lista_nomes.read())

        self.palavra_chave = random.choice(lista_nomes[dificuldade])

        arquivo_lista_nomes.close()

        for letra in self.palavra_chave:
            self.palavra_chave_escondida+='_'

    def verificaChutePalavra(self, chute:str):
        if chute.lower() == self.palavra_chave.lower():
            self.palavra_chave_escondida = self.palavra_chave
            return True
        else: 
            return False

    def temLetra(self, chute:str):
        if self.palavra_chave.lower().count(chute.lower()) > 0:
            for i in range(len(self.palavra_chave)):
                if i == 0 and chute.lower() == self.palavra_chave[i].lower():
                   self.palavra_chave_escondida = chute + self.palavra_chave_escondida[i+1:]
                elif chute.lower() == self.palavra_chave[i].lower():
                    self.palavra_chave_escondida = self.palavra_chave_escondida[:i] + chute + self.palavra_chave_escondida[i+1:]
            return True
        else:
            return False

    def getPalavra(self):
        return self.palavra_chave_escondida
    
    def getPalavraOriginal(self):
        return self.palavra_chave