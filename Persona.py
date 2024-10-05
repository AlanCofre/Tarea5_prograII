class Persona: 
    def __init__(self, nombre: str, apellido:str, fecha_nacimiento:str):
        """
        Constructor de la clase Persona.
        Inicializa los atributos privados de la clase: nombre, apellido y fecha de nacimiento.
        """
        if not nombre or not apellido or not fecha_nacimiento:
            raise ValueError("El nombre, apellido y fecha de nacimiento no pueden estar vacíos.")
        self.__nombre = nombre
        self.__apellido = apellido
        self.__fecha_nacimiento = fecha_nacimiento

    # Propiedad para obtener el nombre
    @property
    def nombre(self):
        """
        Getter para obtener el valor del nombre.
        Returns:
        str: El nombre de la persona.
        """
        return self.__nombre
    
    # Setter para establecer el nombre
    @nombre.setter
    def nombre(self, value):
        """
        Setter para cambiar el valor del nombre.
        Parámetros:
        value (str): El nuevo nombre que se va a asignar.
        """
        if not value:
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = value

    # Propiedad para obtener el apellido
    @property
    def apellido(self):
        """
        Getter para obtener el valor del apellido.
        Returns:
        str: El apellido de la persona.
        """
        return self.__apellido
    
    # Setter para establecer el apellido
    @apellido.setter
    def apellido(self, value):
        """
        Setter para cambiar el valor del apellido.
        Parámetros:
        value (str): El nuevo apellido que se va a asignar.
        """
        if not value:
            raise ValueError("El apellido no puede estar vacío.")
        self.__apellido = value

    # Propiedad para obtener la fecha de nacimiento
    @property
    def fecha_nacimiento(self):
        """
        Getter para obtener el valor de la fecha de nacimiento.
        Returns:
        str: La fecha de nacimiento de la persona.
        """
        return self.__fecha_nacimiento
    
    # Setter para establecer la fecha de nacimiento
    @fecha_nacimiento.setter
    def fecha_nacimiento(self, value):
        """
        Setter para cambiar el valor de la fecha de nacimiento.
        Parámetros:
        value (str): La nueva fecha de nacimiento que se va a asignar.
        """
        if not value:
            raise ValueError("La fecha de nacimiento no puede estar vacía.")
        self.__fecha_nacimiento = value

    def Presentarse(self):  
        """
        Método público para que la persona se presente.
        Imprime un mensaje con el nombre completo y la fecha de nacimiento de la persona.
        """
        print(f'Hola, mi nombre es {self.__nombre} {self.__apellido} y nací el {self.__fecha_nacimiento}')
