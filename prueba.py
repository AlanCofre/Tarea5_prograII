# Importar las clases desde los archivos donde ya las tienes
from Asignatura import Asignatura
from Profesor import Profesor
from Estudiante import Estudiante
from Grupo import Grupo
from ProgramaAcademico import ProgramaAcademico

def prueba_programa_academico():
    # Crear varias asignaturas
    asignatura1 = Asignatura("Matemática", "MATH101", 5)
    asignatura2 = Asignatura("Programación", "PROG202", 6)
    
    # Crear profesores
    profesor1 = Profesor("Alonso", "Roberto", "12/12/1980", "PR001", "Matemáticas")
    profesor2 = Profesor("Elena", "Gómez", "15/08/1978", "PR002", "Informática")
    
    # Crear grupos
    grupo1 = Grupo(101, asignatura1, profesor1)
    grupo2 = Grupo(102, asignatura2, profesor2)
    
    # Crear estudiantes
    estudiante1 = Estudiante("Juan", "Perez", "01/01/2000", "A001", "Ingeniería", 1)
    estudiante2 = Estudiante("María", "Gomez", "02/02/2000", "A002", "Ingeniería", 1)

    # Agregar estudiantes a los grupos
    grupo1.agregar_estudiante(estudiante1)
    grupo2.agregar_estudiante(estudiante2)

    # Crear un programa académico
    programa_academico = ProgramaAcademico("Ingeniería de Software", "ISW001")
    
    # Agregar los grupos al programa académico
    programa_academico.agregar_grupo(grupo1)
    programa_academico.agregar_grupo(grupo2)
    
    # Mostrar la información completa del programa académico
    print("\nMostrando el programa académico completo:")
    programa_academico.mostrar_programa()
    
    # Eliminar un grupo del programa académico y mostrar el programa actualizado
    print("\nEliminando un grupo del programa académico:")
    programa_academico.eliminar_grupo(101)
    programa_academico.mostrar_programa()

# Ejecutar la prueba
prueba_programa_academico()