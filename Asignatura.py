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
        
        self._nombre = nombre
        self._codigo = codigo
        self._creditos = creditos
        Asignatura.contador_asignaturas += 1

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        if not nombre:
            raise ValueError("El nombre de la asignatura no puede estar vacío.")
        self._nombre = nombre

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, codigo):
        if not codigo:
            raise ValueError("El código de la asignatura no puede estar vacío.")
        self._codigo = codigo

    @property
    def creditos(self):
        return self._creditos

    @creditos.setter
    def creditos(self, creditos):
        if creditos <= 0:
            raise ValueError("Los créditos deben ser un número positivo.")
        self._creditos = creditos

    @classmethod
    def cantidad_asignaturas(cls):
        return cls.contador_asignaturas

    def mostrar_informacion(self):
        print(f"Asignatura: {self._nombre}, Código: {self._codigo}, Créditos: {self._creditos}")


