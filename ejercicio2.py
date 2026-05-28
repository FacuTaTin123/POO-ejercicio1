class Mago:
    def hechizos(self):
        print('Hechiza')
        
class Guerrero:
    def defensa(self):
        print('Defiende')
        
class Elfo:
    def aura(self):
        print('Aura')
        
class DarkLord(Guerrero, Elfo, Mago):
    pass

dark_lord = DarkLord()
dark_lord.aura()