from Persona import Persona

class Profesor(Persona):
    def __init__(self, nombre: str, apellido:str, fecha_nacimiento:str, numero_empleado:str, departamento:str ):
        super().__init__(nombre, apellido, fecha_nacimiento)
        self.__numero_empleado = numero_empleado 
        self.__departamento = departamento
    
    @property
    def numero_empleado(self):
        return self.__numero_empleado
    
    @property
    def departamento(self):
        return self.__departamento

    def enseñar(materia:str):
        print(f'el profesor esta enseñando {materia}')

    def Presentarse(self):
        super().Presentarse()
        print(f'Soy profesor del departamento de {self.__departamento}')


profesor = Profesor("Victor","Gonzalez", "05/03/2005", "936593", "Medicina")
profesor.Presentarse()    