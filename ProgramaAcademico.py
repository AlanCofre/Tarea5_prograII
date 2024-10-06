class ProgramaAcademico:
    contador_programas = 0  # Atributo de clase para contar programas académicos

    def __init__(self, nombre, codigo):
        self._nombre = nombre  # Atributo privado
        self._codigo = codigo  # Atributo privado
        self._grupos = []  # Lista protegida de grupos
        ProgramaAcademico.contador_programas += 1  # Incrementar contador de programas

    # Propiedad para obtener y modificar el nombre del programa
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        if not nombre:
            raise ValueError("El nombre del programa académico no puede estar vacío.")
        self._nombre = nombre

    # Propiedad para obtener y modificar el código del programa
    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, codigo):
        if not codigo:
            raise ValueError("El código del programa académico no puede estar vacío.")
        self._codigo = codigo

    # Propiedad para obtener la lista de grupos (solo lectura)
    @property
    def grupos(self):
        return self._grupos

    # Método de clase para obtener la cantidad total de programas creados
    @classmethod
    def cantidad_programas(cls):
        return cls.contador_programas

    # Método para agregar un grupo al programa académico
    def agregar_grupo(self, grupo):
        if grupo not in self._grupos:
            self._grupos.append(grupo)
            print(f"Grupo {grupo.numero_grupo} agregado al programa {self._nombre}.")
        else:
            print(f"El grupo {grupo.numero_grupo} ya está en el programa {self._nombre}.")

    # Método para eliminar un grupo por su número
    def eliminar_grupo(self, numero_grupo):
        for grupo in self._grupos:
            if grupo.numero_grupo == numero_grupo:
                self._grupos.remove(grupo)
                print(f"Grupo {numero_grupo} eliminado del programa {self._nombre}.")
                return
        print(f"No se encontró el grupo {numero_grupo} en el programa {self._nombre}.")

    # Método para mostrar la información completa del programa académico
    def mostrar_programa(self):
        print(f"\nPrograma Académico: {self._nombre}")
        print(f"Código: {self._codigo}")
        print("Grupos:")
        if not self._grupos:
            print("No hay grupos en este programa académico.")
        for grupo in self._grupos:
            grupo.mostrar_grupo()

