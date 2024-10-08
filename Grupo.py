from Asignatura import Asignatura 
from Profesor import Profesor     
from Estudiante import Estudiante 

class Grupo:
    contador_grupos = 0  # Atributo de clase para contar grupos

    def __init__(self, numero_grupo: int, asignatura: Asignatura, profesor: Profesor):
        if numero_grupo <= 0:
            raise ValueError("El número de grupo debe ser un entero positivo.")
        self.__numero_grupo = numero_grupo  # Atributo privado
        self.__asignatura = asignatura  # Atributo privado (objeto Asignatura)
        self.__profesor = profesor  # Atributo privado (objeto Profesor)
        self.__estudiantes = []  # Lista protegida de estudiantes
        Grupo.contador_grupos += 1  # Incrementar contador de grupos

    # Propiedad para obtener y modificar el número del grupo
    @property
    def numero_grupo(self):
        return self.__numero_grupo

    @numero_grupo.setter
    def numero_grupo(self, numero_grupo):
        if numero_grupo <= 0:
            raise ValueError("El número de grupo debe ser un entero positivo.")
        self.__numero_grupo = numero_grupo

    # Propiedad para obtener la asignatura
    @property
    def asignatura(self):
        return self.__asignatura

    # Propiedad para obtener el profesor
    @property
    def profesor(self):
        return self.__profesor

    # Propiedad para obtener la lista de estudiantes
    @property
    def estudiantes(self):
        return list(self.__estudiantes)

    # Método de clase para obtener la cantidad total de grupos creados
    @classmethod
    def cantidad_grupos(cls):
        return cls.contador_grupos

    # Método para agregar un estudiante
    def agregar_estudiante(self, estudiante: Estudiante):
        if estudiante not in self.__estudiantes:
            self.__estudiantes.append(estudiante)
            print(f"Estudiante {estudiante.nombre} agregado al grupo {self.__numero_grupo}.")
        else:
            print(f"El estudiante {estudiante.nombre} ya está en el grupo {self.__numero_grupo}.")

    # Método para eliminar un estudiante por matrícula
    def eliminar_estudiante(self, matricula: str):
        for estudiante in self.__estudiantes:
            if estudiante.matricula == matricula:
                self.__estudiantes.remove(estudiante)
                print(f"Estudiante con matrícula {matricula} eliminado del grupo {self.__numero_grupo}.")
                return
        print(f"No se encontró un estudiante con matrícula {matricula} en el grupo {self.__numero_grupo}.")

    # Método para mostrar la información completa del grupo
    def mostrar_grupo(self):
        print(f"\nGrupo: {self.__numero_grupo}")
        print(f"Asignatura: {self.__asignatura.nombre}")
        print(f"Profesor: {self.__profesor.nombre} {self.__profesor.apellido}")
        print(f"Estudiantes en el grupo ({len(self.__estudiantes)} estudiantes):")
        for estudiante in self.__estudiantes:
            print(f"- {estudiante.nombre}, Matrícula: {estudiante.matricula}")

