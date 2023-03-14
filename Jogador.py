class Jogador():
    
    def __init__(self):
        self.vida = 6
    
    def mostra_vida(self):
        if self.vida == 6:
            print(' O')
            print('/|\\')
            print('/ \\')
                        
        if self.vida == 5:
            print(" O")
            print("/|\\")
            print("  \\")
           
            
        if self.vida == 4:
            print(" O")
            print(" |\\")
            print("  \\")
            
        if self.vida == 3:
            print(" O")
            print(" |\\")
            
        if self.vida == 2:
            print(" O")
            print(" |")
            
        if self.vida == 1:
            print("O")
            
        if self.vida == 0:
            print("Você perdeu!")