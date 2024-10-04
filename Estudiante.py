from Persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre: str, apellido:str, fecha_nacimiento:str, matricula:str, carrera:str, semestre:int):
        super().__init__(nombre, apellido, fecha_nacimiento)
        self.__matricula = matricula
        self.__carrera = carrera
        self.__semestre = semestre
    
    @property
    def matricula(self):
        return self.__matricula
    
    @property
    def carrera(self):
        return self.__carrera
    
    @property
    def semestre(self):
        return self.__semestre
    
    def estudiar(self, materia:str, horas:int):
        print(f"El estudiante ha estudiado {materia} por {horas} horas")
    
    def Presentarse(self):
        super().Presentarse()
        print(f"Además, soy estudiante de {self.__carrera}, en el semestre {self.__semestre}, y mi matrícula es {self.__matricula}.")

estudiante = Estudiante("Ana", "Gómez", "15/05/2000", "A12345", "Ingeniería de Software", 5)
estudiante.Presentarse()
    