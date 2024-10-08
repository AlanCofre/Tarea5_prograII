class Asignatura:
    contador_asignaturas = 0  # Atributo de clase para contar asignaturas

    def __init__(self, nombre, codigo, creditos):
        # Validaciones básicas
        if not nombre:
            raise ValueError("El nombre de la asignatura no puede estar vacío.")
        if not codigo:
            raise ValueError("El código de la asignatura no puede estar vacío.")
        if creditos <= 0:
            raise ValueError("Los créditos deben ser un número positivo.")
        
        self.__nombre = nombre
        self.__codigo = codigo
        self.__creditos = creditos
        Asignatura.contador_asignaturas += 1

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        if not nombre:
            raise ValueError("El nombre de la asignatura no puede estar vacío.")
        self.__nombre = nombre

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        if not codigo:
            raise ValueError("El código de la asignatura no puede estar vacío.")
        self.__codigo = codigo

    @property
    def creditos(self):
        return self.__creditos

    @creditos.setter
    def creditos(self, creditos):
        if creditos <= 0:
            raise ValueError("Los créditos deben ser un número positivo.")
        self.__creditos = creditos

    @classmethod
    def cantidad_asignaturas(cls):
        return cls.contador_asignaturas

    def mostrar_informacion(self):
        print(f"Asignatura: {self.__nombre}, Código: {self.__codigo}, Créditos: {self.__creditos}")