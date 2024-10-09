
from Persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre: str, apellido:str, fecha_nacimiento:str, matricula:str, carrera:str, semestre:int):
        """
        Constructor de la clase Estudiante.
        Inicializa los atributos heredados de la clase Persona (nombre, apellido y fecha de nacimiento)
        y agrega los atributos específicos del estudiante: matrícula, carrera y semestre.
        """
        if not matricula:
            raise ValueError("La matrícula no puede estar vacía.")
        if not carrera:
            raise ValueError("La carrera no puede estar vacía.")
        if semestre <= 0:
            raise ValueError("El semestre debe ser un número positivo.")
        # Llamamos al constructor de la clase base (Persona) para inicializar los atributos heredados
        super().__init__(nombre, apellido, fecha_nacimiento)
        self.__matricula = matricula
        self.__carrera = carrera
        self.__semestre = semestre
    
    # Propiedad para obtener la matrícula
    @property
    def matricula(self):
        """
        Getter para obtener el valor de la matrícula.
        """
        return self.__matricula
    
    # Setter para modificar la matrícula
    @matricula.setter
    def matricula(self, value):
        """
        Setter para cambiar el valor de la matrícula.
        """
        if not value:
            raise ValueError("La matrícula no puede estar vacía.")
        self.__matricula = value

    # Propiedad para obtener la carrera
    @property
    def carrera(self):
        """
        Getter para obtener el valor de la carrera.
        """
        return self.__carrera
    
    # Setter para modificar la carrera
    @carrera.setter
    def carrera(self, value):
        """
        Setter para cambiar el valor de la carrera.
        """
        if not value:
            raise ValueError("La carrera no puede estar vacía.")
        self.__carrera = value

    # Propiedad para obtener el semestre
    @property
    def semestre(self):
        """
        Getter para obtener el valor del semestre.
        """
        return self.__semestre
    
    # Setter para modificar el semestre
    @semestre.setter
    def semestre(self, value):
        """
        Setter para cambiar el valor del semestre.
        """
        if value <= 0:
            raise ValueError("El semestre debe ser un número positivo.")
        self.__semestre = value

    # Método para que el estudiante estudie una materia
    def estudiar(self, materia: str, horas: int):
        """
        Método público que simula que el estudiante está estudiando una materia durante
        un cierto número de horas.
        """
        if not materia:
            raise ValueError("La materia no puede estar vacía.")
        if horas <= 0:
            raise ValueError("Las horas deben ser un número positivo.")
        print(f"El estudiante ha estudiado {materia} por {horas} horas")
    
    # Sobreescribir el método Presentarse para incluir detalles del estudiante
    def Presentarse(self):
        """
        Sobrescribe el método presentarse de la clase Persona.
        Llama al método original para mostrar la presentación básica, y añade
        la información específica del estudiante: carrera, semestre y matrícula.
        """
        # Llamamos al método Presentarse de la clase Persona y añadimos la información específica del estudiante
        super().Presentarse()
        print(f"Además, soy estudiante de {self.__carrera}, en el semestre {self.__semestre}, y mi matrícula es {self.__matricula}.")

