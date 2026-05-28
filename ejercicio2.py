'''
Ejercicio ( herencia)

Crear 3 clases: “Mago” , “Guerrero” y “Elfo”

La clase “Mago”, debe tener un método llamado “hechizos”
la clase “Guerrero” debe tener un método llamado “defensa”
la clase “Elfo” debe tener una método llamado “aura”.

Luego crear una clase llamada “DarkLord” que herede de “Guerrero “ y “Elfo”, en ese orden y por lo tanto puede usar “defensa” y “aura”, además de los hechizos.

por último cambiar el orden de las herencias de la clase “DarkLord” y observa cómo se va modificando el orden del MRO.
'''
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