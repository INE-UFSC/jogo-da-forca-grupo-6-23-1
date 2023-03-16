class Jogador():

    def __init__(self, vida):
        self.vida = vida
    
    def perdeVida(self):
        self.vida -= 1

    def mostraVida(self):
        if self.vida == 6:
            print("Você ainda tem 6 vidas")
                        
        elif self.vida == 5:
            print(" O")
                       
        elif self.vida == 4:
            print(" O")
            print(" |")
            
            
        elif self.vida == 3:
            print(" O")
            print("/|")
            
            
        elif self.vida == 2:
            print(" O")
            print("/|\\")
            
            
        elif self.vida == 1:
            print(" O")
            print("/|\\")
            print("/")
            
        elif self.vida == 0:
            print(" O")
            print("/|\\")
            print("/ \\")

    def getVida(self):
        return self.vida