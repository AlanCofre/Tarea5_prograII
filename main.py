import customtkinter as ctk
from Asignatura import Asignatura
from Profesor import Profesor
from Estudiante import Estudiante
from Grupo import Grupo
from ProgramaAcademico import ProgramaAcademico

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistema de Gestión Universitaria")
        self.geometry("800x600")

        # Lista de objetos
        self.asignaturas = []
        self.profesores = []
        self.estudiantes = []
        self.grupos = []
        self.programa_academico = ProgramaAcademico("Sistemas en informática", "ISW001")

        # Crear el marco de control principal
        self.frame_principal = ctk.CTkFrame(self)
        self.frame_principal.pack(padx=20, pady=20, fill="both", expand=True)

        self.label_titulo = ctk.CTkLabel(self.frame_principal, text="Sistema de Gestión Universitaria", font=("Arial", 20))
        self.label_titulo.pack(pady=10)

        # Botones principales
        self.boton_crear_asignatura = ctk.CTkButton(self.frame_principal, text="Crear Asignatura", command=self.crear_asignatura)
        self.boton_crear_asignatura.pack(pady=10)

        self.boton_crear_profesor = ctk.CTkButton(self.frame_principal, text="Crear Profesor", command=self.crear_profesor)
        self.boton_crear_profesor.pack(pady=10)

        self.boton_crear_estudiante = ctk.CTkButton(self.frame_principal, text="Crear Estudiante", command=self.crear_estudiante)
        self.boton_crear_estudiante.pack(pady=10)

        self.boton_crear_grupo = ctk.CTkButton(self.frame_principal, text="Crear Grupo", command=self.crear_grupo)
        self.boton_crear_grupo.pack(pady=10)

        self.boton_mostrar_programa = ctk.CTkButton(self.frame_principal, text="Mostrar Programa Académico", command=self.mostrar_programa)
        self.boton_mostrar_programa.pack(pady=10)

        self.text_output = ctk.CTkTextbox(self.frame_principal, width=600, height=200)
        self.text_output.pack(pady=10)

    def crear_asignatura(self):
        ventana_asignatura = ctk.CTkToplevel(self)
        ventana_asignatura.title("Crear Asignatura")

        label_nombre = ctk.CTkLabel(ventana_asignatura, text="Nombre:")
        label_nombre.pack(pady=5)
        entry_nombre = ctk.CTkEntry(ventana_asignatura)
        entry_nombre.pack(pady=5)

        label_codigo = ctk.CTkLabel(ventana_asignatura, text="Código:")
        label_codigo.pack(pady=5)
        entry_codigo = ctk.CTkEntry(ventana_asignatura)
        entry_codigo.pack(pady=5)

        label_creditos = ctk.CTkLabel(ventana_asignatura, text="Créditos:")
        label_creditos.pack(pady=5)
        entry_creditos = ctk.CTkEntry(ventana_asignatura)
        entry_creditos.pack(pady=5)

        def guardar_asignatura():
            nombre = entry_nombre.get()
            codigo = entry_codigo.get()
            creditos = int(entry_creditos.get())
            asignatura = Asignatura(nombre, codigo, creditos)
            self.asignaturas.append(asignatura)
            self.text_output.insert("end", f"Asignatura '{nombre}' creada con éxito.\n")
            ventana_asignatura.destroy()

        boton_guardar = ctk.CTkButton(ventana_asignatura, text="Guardar Asignatura", command=guardar_asignatura)
        boton_guardar.pack(pady=10)

    def crear_profesor(self):
        ventana_profesor = ctk.CTkToplevel(self)
        ventana_profesor.title("Crear Profesor")

        label_nombre = ctk.CTkLabel(ventana_profesor, text="Nombre:")
        label_nombre.pack(pady=5)
        entry_nombre = ctk.CTkEntry(ventana_profesor)
        entry_nombre.pack(pady=5)

        label_apellido = ctk.CTkLabel(ventana_profesor, text="Apellido:")
        label_apellido.pack(pady=5)
        entry_apellido = ctk.CTkEntry(ventana_profesor)
        entry_apellido.pack(pady=5)

        label_fecha = ctk.CTkLabel(ventana_profesor, text="Fecha de Nacimiento (dd/mm/aaaa):")
        label_fecha.pack(pady=5)
        entry_fecha = ctk.CTkEntry(ventana_profesor)
        entry_fecha.pack(pady=5)

        label_numero = ctk.CTkLabel(ventana_profesor, text="Número de Empleado:")
        label_numero.pack(pady=5)
        entry_numero = ctk.CTkEntry(ventana_profesor)
        entry_numero.pack(pady=5)

        label_departamento = ctk.CTkLabel(ventana_profesor, text="Departamento:")
        label_departamento.pack(pady=5)
        entry_departamento = ctk.CTkEntry(ventana_profesor)
        entry_departamento.pack(pady=5)

        def guardar_profesor():
            nombre = entry_nombre.get()
            apellido = entry_apellido.get()
            fecha = entry_fecha.get()
            numero = entry_numero.get()
            departamento = entry_departamento.get()
            profesor = Profesor(nombre, apellido, fecha, numero, departamento)
            self.profesores.append(profesor)
            self.text_output.insert("end", f"Profesor '{nombre} {apellido}' creado con éxito.\n")
            ventana_profesor.destroy()

        boton_guardar = ctk.CTkButton(ventana_profesor, text="Guardar Profesor", command=guardar_profesor)
        boton_guardar.pack(pady=10)

    def crear_estudiante(self):
        ventana_estudiante = ctk.CTkToplevel(self)
        ventana_estudiante.title("Crear Estudiante")

        label_nombre = ctk.CTkLabel(ventana_estudiante, text="Nombre:")
        label_nombre.pack(pady=5)
        entry_nombre = ctk.CTkEntry(ventana_estudiante)
        entry_nombre.pack(pady=5)

        label_apellido = ctk.CTkLabel(ventana_estudiante, text="Apellido:")
        label_apellido.pack(pady=5)
        entry_apellido = ctk.CTkEntry(ventana_estudiante)
        entry_apellido.pack(pady=5)

        label_fecha = ctk.CTkLabel(ventana_estudiante, text="Fecha de Nacimiento (dd/mm/aaaa):")
        label_fecha.pack(pady=5)
        entry_fecha = ctk.CTkEntry(ventana_estudiante)
        entry_fecha.pack(pady=5)

        label_matricula = ctk.CTkLabel(ventana_estudiante, text="Matrícula:")
        label_matricula.pack(pady=5)
        entry_matricula = ctk.CTkEntry(ventana_estudiante)
        entry_matricula.pack(pady=5)

        label_carrera = ctk.CTkLabel(ventana_estudiante, text="Carrera:")
        label_carrera.pack(pady=5)
        entry_carrera = ctk.CTkEntry(ventana_estudiante)
        entry_carrera.pack(pady=5)

        label_semestre = ctk.CTkLabel(ventana_estudiante, text="Semestre:")
        label_semestre.pack(pady=5)
        entry_semestre = ctk.CTkEntry(ventana_estudiante)
        entry_semestre.pack(pady=5)

        def guardar_estudiante():
            nombre = entry_nombre.get()
            apellido = entry_apellido.get()
            fecha = entry_fecha.get()
            matricula = entry_matricula.get()
            carrera = entry_carrera.get()
            semestre = int(entry_semestre.get())
            estudiante = Estudiante(nombre, apellido, fecha, matricula, carrera, semestre)
            self.estudiantes.append(estudiante)
            self.text_output.insert("end", f"Estudiante '{nombre} {apellido}' creado con éxito.\n")
            ventana_estudiante.destroy()

        boton_guardar = ctk.CTkButton(ventana_estudiante, text="Guardar Estudiante", command=guardar_estudiante)
        boton_guardar.pack(pady=10)

    def crear_grupo(self):
        ventana_grupo = ctk.CTkToplevel(self)
        ventana_grupo.title("Crear Grupo")

        if not self.asignaturas:
            self.text_output.insert("end", "Debe crear asignaturas primero.\n")
            ventana_grupo.destroy()
            return
        if not self.profesores:
            self.text_output.insert("end", "Debe crear profesores primero.\n")
            ventana_grupo.destroy()
            return

        label_numero = ctk.CTkLabel(ventana_grupo, text="Número del Grupo:")
        label_numero.pack(pady=5)
        entry_numero = ctk.CTkEntry(ventana_grupo)
        entry_numero.pack(pady=5)
        
        label_asignatura = ctk.CTkLabel(ventana_grupo, text="Seleccione Asignatura:")
        label_asignatura.pack(pady=5)
        entry_asignatura = ctk.CTkOptionMenu(ventana_grupo, values=[a.nombre for a in self.asignaturas])
        entry_asignatura.pack(pady=5)

        # Selección de Profesor
        label_profesor = ctk.CTkLabel(ventana_grupo, text="Seleccione Profesor:")
        label_profesor.pack(pady=5)
        entry_profesor = ctk.CTkOptionMenu(ventana_grupo, values=[f"{p.nombre} {p.apellido}" for p in self.profesores])
        entry_profesor.pack(pady=5)

        def guardar_grupo():
            numero_grupo = int(entry_numero.get())
        
            # Obtener la asignatura seleccionada
            nombre_asignatura = entry_asignatura.get()
            asignatura_seleccionada = None
            
            for asignatura in self.asignaturas:
                if asignatura.nombre == nombre_asignatura:
                    asignatura_seleccionada = asignatura
                    break
            
            if asignatura_seleccionada is None:
                self.text_output.insert("end", "La asignatura seleccionada no existe.\n")
                return

            # Obtener el profesor seleccionado
            nombre_profesor = entry_profesor.get()
            profesor_seleccionado = None
            
            for profesor in self.profesores:
                if f"{profesor.nombre} {profesor.apellido}" == nombre_profesor:
                    profesor_seleccionado = profesor
                    break
            
            if profesor_seleccionado is None:
                self.text_output.insert("end", "El profesor seleccionado no existe.\n")
                return
        
            grupo = Grupo(numero_grupo, asignatura_seleccionada, profesor_seleccionado)
            self.grupos.append(grupo)
            self.text_output.insert("end", f"Grupo {numero_grupo} creado con éxito.\n")
            ventana_grupo.destroy()
            

        boton_guardar = ctk.CTkButton(ventana_grupo, text="Guardar Grupo", command=guardar_grupo)
        boton_guardar.pack(pady=10)

    def mostrar_programa(self):
        if not self.grupos:
            self.text_output.insert("end", "No se ha agregado ningún grupo al programa académico.\nPrimero debe agregar grupos.\n")
            return
        
        
        self.text_output.insert("end", f"Programa Académico: {self.programa_academico.nombre} ({self.programa_academico.codigo})\n")
        
    
        for grupo in self.grupos:
            asignatura = grupo.asignatura.nombre
            profesor = f"{grupo.profesor.nombre} {grupo.profesor.apellido}"
            self.text_output.insert("end", f"Grupo {grupo.numero_grupo}: Asignatura: {asignatura}, Profesor: {profesor}\n")

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")  # Modo oscuro de CustomTkinter
    ctk.set_default_color_theme("blue")  # Tema azul de CustomTkinter
    app = App()
    app.mainloop()
