class Palavra():
    def __init__(self, palavra_chave:str):
        self.palavra_chave = palavra_chave
    
    def gerarPalavra(self):
        self.palavra_chave_escondida = ''
        for letra in self.palavra_chave_escondida:
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