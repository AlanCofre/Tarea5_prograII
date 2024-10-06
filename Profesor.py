from Persona import Persona

class Profesor(Persona):
    def __init__(self, nombre: str, apellido:str, fecha_nacimiento:str, numero_empleado:str, departamento:str):
        """
        Constructor de la clase Profesor.
        Inicializa los atributos heredados de la clase Persona (nombre, apellido y fecha de nacimiento)
        y agrega los atributos específicos del profesor: número de empleado y departamento.
        """
        if not numero_empleado:
            raise ValueError("El número de empleado no puede estar vacío.")
        if not departamento:
            raise ValueError("El departamento no puede estar vacío.")
        
        # Llamamos al constructor de la clase base (Persona) para inicializar los atributos heredados
        super().__init__(nombre, apellido, fecha_nacimiento)
        self.__numero_empleado = numero_empleado 
        self.__departamento = departamento
    
    # Propiedad para obtener el número de empleado
    @property
    def numero_empleado(self):
        """
        Getter para obtener el valor del número de empleado.
        """
        return self.__numero_empleado
    
    # Setter para modificar el número de empleado
    @numero_empleado.setter
    def numero_empleado(self, value):
        """
        Setter para cambiar el valor del número de empleado.
        """
        if not value:
            raise ValueError("El número de empleado no puede estar vacío.")
        self.__numero_empleado = value
    
    # Propiedad para obtener el departamento
    @property
    def departamento(self):
        """
        Getter para obtener el valor del departamento.
        """
        return self.__departamento
    
    # Setter para modificar el departamento
    @departamento.setter
    def departamento(self, value):
        """
        Setter para cambiar el valor del departamento.
        """
        if not value:
            raise ValueError("El departamento no puede estar vacío.")
        self.__departamento = value  # Corrección de error tipográfico

    # Método público para enseñar una materia
    def enseñar(self, materia: str):
        """
        Método público que simula que el profesor está enseñando una materia.
        """
        if not materia:
            raise ValueError("La materia no puede estar vacía.")
        
        print(f'El profesor está enseñando {materia}')

    # Sobrescribir el método Presentarse para incluir detalles del profesor
    def Presentarse(self):
        """
        Sobrescribe el método presentarse de la clase Persona.
        Llama al método original para mostrar la presentación básica, y añade
        la información específica del profesor: su número de empleado y departamento.
        """
        # Llamamos al método Presentarse de la clase Persona y añadimos la información específica del profesor
        super().Presentarse()
        print(f'Soy profesor del departamento de {self.__departamento}')

# Crear una instancia de la clase Profesor y llamamos al método Presentarse
profesor = Profesor("Victor", "Gonzalez", "05/03/2005", "936593", "Medicina")
profesor.Presentarse()
