class Jogador():
    
    def __init__(self):
        self.vida = 6
    
    def perdeVida(self):
        self.vida -= 1

    def mostra_vida(self):
        if self.vida == 6:
            print("""
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """)
                        
        elif self.vida == 5:
            print("""
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """)
                       
        elif self.vida == 4:
            print("""
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """)
            
        elif self.vida == 3:
            print("""
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """)
            
            
        elif self.vida == 2:
            print("""
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """)
            
        elif self.vida == 1:
            print("""
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """)
            
        elif self.vida == 0:
            print("""
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """)
