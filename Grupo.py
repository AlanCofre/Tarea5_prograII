import Asignatura
class Grupo:
    contador_grupos = 0  # Atributo de clase para contar grupos

    def __init__(self, numero_grupo, asignatura, profesor):
        self.__numero_grupo = numero_grupo  # Atributo privado
        self.__asignatura = Asignatura.nombre  # Atributo privado (objeto Asignatura)
        self.__profesor = Profesor.nombre  # Atributo privado (objeto Profesor)
        self._estudiantes = [Estudiante.nombre]  # Lista protegida de estudiantes
        Grupo.contador_grupos += 1  # Incrementar contador de grupos

    # Propiedad para obtener y modificar el número del grupo
    @property
    def numero_grupo(self):
        return self._numero_grupo

    @numero_grupo.setter
    def numero_grupo(self, numero_grupo):
        self._numero_grupo = numero_grupo

    # Propiedad para obtener y modificar la asignatura
    @property
    def asignatura(self):
        return self._asignatura

    @asignatura.setter
    def asignatura(self, asignatura):
        self._asignatura = asignatura

    # Propiedad para obtener y modificar el profesor
    @property
    def profesor(self):
        return self._profesor

    @profesor.setter
    def profesor(self, profesor):
        self._profesor = profesor

    # Propiedad para obtener la lista de estudiantes
    @property
    def estudiantes(self):
        return self._estudiantes

    # Método de clase para obtener la cantidad total de grupos creados
    @classmethod
    def cantidad_grupos(cls):
        return cls.contador_grupos

    # Método para agregar un estudiante
    def agregar_estudiante(self, estudiante):
        if estudiante not in self._estudiantes:
            self._estudiantes.append(estudiante)
            print(f"Estudiante {estudiante['nombre']} agregado al grupo {self._numero_grupo}.")
        else:
            print(f"El estudiante {estudiante['nombre']} ya está en el grupo {self._numero_grupo}.")

    # Método para eliminar un estudiante por matrícula
    def eliminar_estudiante(self, matricula):
        for estudiante in self._estudiantes:
            if estudiante["matricula"] == matricula:
                self._estudiantes.remove(estudiante)
                print(f"Estudiante con matrícula {matricula} eliminado del grupo {self._numero_grupo}.")
                return
        print(f"No se encontró un estudiante con matrícula {matricula} en el grupo {self._numero_grupo}.")

    # Método para mostrar la información completa del grupo
    def mostrar_grupo(self):
        print(f"\nGrupo: {self._numero_grupo}")
        print(f"Asignatura: {self._asignatura.nombre}")
        print(f"Profesor: {self._profesor}")
        print(f"Estudiantes en el grupo ({len(self._estudiantes)} estudiantes):")
        for estudiante in self._estudiantes:
            print(f"- {estudiante['nombre']}, Matrícula: {estudiante['matricula']}")

hola = Grupo(12, "matematica", "alonso roberto")

grupo.mostrar_grupo()