
class Alumno:
    def __init__(self, nombre, apellido, edad, curso):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.curso = curso

    def programar(self):
        print(f'el alumno {self.nombre} está programando')
        
nombre = input('Ingrese el nombre del alumno: ')
apellido = input('Ingrese el apellido del alumno: ')
edad = int(input('Ingrese la edad del alumno: '))
curso = input('Ingrese el curso del alumno: ')

alumno = Alumno(nombre, apellido, edad, curso)
alumno.programar()