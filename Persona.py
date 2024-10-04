class Persona: 
    def __init__(self, nombre: str, apellido:str, fecha_nacimiento:str):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__fecha_nacimiento = fecha_nacimiento

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def apellido(self):
        return self.__apellido
    
    @property
    def fecha_nacimiento(self):
        return self.__fecha_nacimiento
    

    def Presentarse(self):  
        print(f'Hola, mi nombre es {self.__nombre} {self.__apellido} y nací el {self.__fecha_nacimiento}')


#persona = Persona("Alan", "Cofre", "29 de junio de 2001" )
#persona.Presentarse()



