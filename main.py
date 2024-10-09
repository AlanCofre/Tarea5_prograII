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
        self.geometry("500x400")

        # Lista de objetos
        self.asignaturas = []
        self.profesores = []
        self.estudiantes = []
        self.grupos = []
        self.programa_academico = ProgramaAcademico("Sistemas en informática", "ISW001")

        # Crear pestañas
        self.tabs = ctk.CTkTabview(self)
        self.tabs.pack(padx=20, pady=10, fill="both", expand=True)

        self.tab_asignaturas = self.tabs.add("Asignaturas")
        self.tab_profesores = self.tabs.add("Profesores")
        self.tab_estudiantes = self.tabs.add("Estudiantes")
        self.tab_grupos = self.tabs.add("Grupos")
        self.tab_programa = self.tabs.add("Programa Académico")

        # Asignaturas
        self.crear_boton_asignaturas(self.tab_asignaturas)

        # Profesores
        self.crear_boton_profesores(self.tab_profesores)

        # Estudiantes
        self.crear_boton_estudiantes(self.tab_estudiantes)

        # Grupos
        self.crear_boton_grupos(self.tab_grupos)

        # Programa Académico
        self.crear_boton_programa(self.tab_programa)

        # Cuadro de texto para la salida
        self.text_output = ctk.CTkTextbox(self, width=450, height=300)
        self.text_output.pack(pady=10)

    # -------------------------------------------------
    # Asignaturas
    def crear_boton_asignaturas(self, frame):
        boton_crear_asignatura = ctk.CTkButton(frame, text="Crear Asignatura", command=self.crear_asignatura)
        boton_crear_asignatura.pack(pady=10)

        boton_eliminar_asignatura = ctk.CTkButton(frame, text="Eliminar Asignatura", command=self.eliminar_asignatura)
        boton_eliminar_asignatura.pack(pady=10)

        boton_mostrar_asignaturas = ctk.CTkButton(frame, text="Mostrar Asignaturas", command=self.mostrar_asignaturas)
        boton_mostrar_asignaturas.pack(pady=10)

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
            try:
                nombre = entry_nombre.get().strip()
                codigo = entry_codigo.get().strip()
                creditos = int(entry_creditos.get())

                if not nombre or not codigo:
                    self.text_output.insert("end", "El nombre y el código no pueden estar vacíos.\n")
                    return
                if creditos <= 0:
                    self.text_output.insert("end", "Los créditos deben ser un número positivo.\n")
                    return

                # Verificar si la asignatura ya existe
                for asignatura in self.asignaturas:
                    if asignatura.nombre == nombre and asignatura.codigo == codigo:
                        self.text_output.insert("end", f"La asignatura '{nombre}' ya existe.\n")
                        return

                asignatura = Asignatura(nombre, codigo, creditos)
                self.asignaturas.append(asignatura)
                self.text_output.insert("end", f"Asignatura '{nombre}' creada con éxito.\n")
                ventana_asignatura.destroy()

            except ValueError:
                self.text_output.insert("end", "Por favor, ingrese un valor válido para los créditos.\n")

        boton_guardar = ctk.CTkButton(ventana_asignatura, text="Guardar Asignatura", command=guardar_asignatura)
        boton_guardar.pack(pady=10)

    def eliminar_asignatura(self):
        ventana_eliminar_asignatura = ctk.CTkToplevel(self)
        ventana_eliminar_asignatura.title("Eliminar Asignatura")

        label_codigo = ctk.CTkLabel(ventana_eliminar_asignatura, text="Código de la Asignatura:")
        label_codigo.pack(pady=5)
        entry_codigo = ctk.CTkEntry(ventana_eliminar_asignatura)
        entry_codigo.pack(pady=5)

        def eliminar():
            codigo = entry_codigo.get().strip()
            asignatura_encontrada = None
            for asignatura in self.asignaturas:
                if asignatura.codigo == codigo:
                    asignatura_encontrada = asignatura
                    break
            if asignatura_encontrada:
                self.asignaturas.remove(asignatura_encontrada)
                self.text_output.insert("end", f"Asignatura con código '{codigo}' eliminada.\n")
            else:
                self.text_output.insert("end", f"No se encontró una asignatura con el código '{codigo}'.\n")
            ventana_eliminar_asignatura.destroy()

        boton_eliminar = ctk.CTkButton(ventana_eliminar_asignatura, text="Eliminar", command=eliminar)
        boton_eliminar.pack(pady=10)

    def mostrar_asignaturas(self):
        self.text_output.delete(1.0, "end")
        if not self.asignaturas:
            self.text_output.insert("end", "No hay asignaturas creadas.\n")
        for asignatura in self.asignaturas:
            self.text_output.insert("end", f"Asignatura: {asignatura.nombre} | Código: {asignatura.codigo} | Créditos: {asignatura.creditos}\n")

    # -------------------------------------------------
    # Profesores
    def crear_boton_profesores(self, frame):
        boton_crear_profesor = ctk.CTkButton(frame, text="Crear Profesor", command=self.crear_profesor)
        boton_crear_profesor.pack(pady=10)

        boton_eliminar_profesor = ctk.CTkButton(frame, text="Eliminar Profesor", command=self.eliminar_profesor)
        boton_eliminar_profesor.pack(pady=10)

        boton_mostrar_profesores = ctk.CTkButton(frame, text="Mostrar Profesores", command=self.mostrar_profesores)
        boton_mostrar_profesores.pack(pady=10)

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
            try:
                nombre = entry_nombre.get().strip()
                apellido = entry_apellido.get().strip()
                fecha = entry_fecha.get().strip()
                numero = entry_numero.get().strip()
                departamento = entry_departamento.get().strip()

                if not nombre or not apellido or not fecha or not numero or not departamento:
                    self.text_output.insert("end", "Todos los campos deben estar completos.\n")
                    return

                # Verificar si el profesor ya existe
                for profesor in self.profesores:
                    if profesor.numero_empleado == numero:
                        self.text_output.insert("end", f"El profesor con número de empleado '{numero}' ya existe.\n")
                        return

                profesor = Profesor(nombre, apellido, fecha, numero, departamento)
                self.profesores.append(profesor)
                self.text_output.insert("end", f"Profesor '{nombre} {apellido}' creado con éxito.\n")
                ventana_profesor.destroy()

            except ValueError:
                self.text_output.insert("end", "Error al crear el profesor. Verifique los datos ingresados.\n")

        boton_guardar = ctk.CTkButton(ventana_profesor, text="Guardar Profesor", command=guardar_profesor)
        boton_guardar.pack(pady=10)

    def eliminar_profesor(self):
        ventana_eliminar_profesor = ctk.CTkToplevel(self)
        ventana_eliminar_profesor.title("Eliminar Profesor")

        label_numero = ctk.CTkLabel(ventana_eliminar_profesor, text="Número de Empleado:")
        label_numero.pack(pady=5)
        entry_numero = ctk.CTkEntry(ventana_eliminar_profesor)
        entry_numero.pack(pady=5)

        def eliminar():
            numero = entry_numero.get().strip()
            profesor_encontrado = None
            for profesor in self.profesores:
                if profesor.numero_empleado == numero:
                    profesor_encontrado = profesor
                    break
            if profesor_encontrado:
                self.profesores.remove(profesor_encontrado)
                self.text_output.insert("end", f"Profesor con número '{numero}' eliminado.\n")
            else:
                self.text_output.insert("end", f"No se encontró un profesor con el número '{numero}'.\n")
            ventana_eliminar_profesor.destroy()

        boton_eliminar = ctk.CTkButton(ventana_eliminar_profesor, text="Eliminar", command=eliminar)
        boton_eliminar.pack(pady=10)

    def mostrar_profesores(self):
        self.text_output.delete(1.0, "end")
        if not self.profesores:
            self.text_output.insert("end", "No hay profesores creados.\n")
        for profesor in self.profesores:
            self.text_output.insert("end", f"Profesor: {profesor.nombre} {profesor.apellido} | Departamento: {profesor.departamento} | Número de Empleado: {profesor.numero_empleado}\n")

    # -------------------------------------------------
    # Estudiantes
    def crear_boton_estudiantes(self, frame):
        boton_crear_estudiante = ctk.CTkButton(frame, text="Crear Estudiante", command=self.crear_estudiante)
        boton_crear_estudiante.pack(pady=10)

        boton_eliminar_estudiante = ctk.CTkButton(frame, text="Eliminar Estudiante", command=self.eliminar_estudiante)
        boton_eliminar_estudiante.pack(pady=10)

        boton_mostrar_estudiantes = ctk.CTkButton(frame, text="Mostrar Estudiantes", command=self.mostrar_estudiantes)
        boton_mostrar_estudiantes.pack(pady=10)

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
            try:
                nombre = entry_nombre.get().strip()
                apellido = entry_apellido.get().strip()
                fecha = entry_fecha.get().strip()
                matricula = entry_matricula.get().strip()
                carrera = entry_carrera.get().strip()
                semestre = int(entry_semestre.get().strip())

                if not nombre or not apellido or not fecha or not matricula or not carrera:
                    self.text_output.insert("end", "Todos los campos deben estar completos.\n")
                    return
                if semestre <= 0:
                    self.text_output.insert("end", "El semestre debe ser un número positivo.\n")
                    return

                # Verificar si el estudiante ya existe
                for estudiante in self.estudiantes:
                    if estudiante.matricula == matricula:
                        self.text_output.insert("end", f"El estudiante con matrícula '{matricula}' ya existe.\n")
                        return

                estudiante = Estudiante(nombre, apellido, fecha, matricula, carrera, semestre)
                self.estudiantes.append(estudiante)
                self.text_output.insert("end", f"Estudiante '{nombre} {apellido}' creado con éxito.\n")
                ventana_estudiante.destroy()

            except ValueError:
                self.text_output.insert("end", "Error en los datos. Verifique que el semestre sea un número válido.\n")

        boton_guardar = ctk.CTkButton(ventana_estudiante, text="Guardar Estudiante", command=guardar_estudiante)
        boton_guardar.pack(pady=10)

    def eliminar_estudiante(self):
        ventana_eliminar_estudiante = ctk.CTkToplevel(self)
        ventana_eliminar_estudiante.title("Eliminar Estudiante")

        label_matricula = ctk.CTkLabel(ventana_eliminar_estudiante, text="Matrícula del Estudiante:")
        label_matricula.pack(pady=5)
        entry_matricula = ctk.CTkEntry(ventana_eliminar_estudiante)
        entry_matricula.pack(pady=5)

        def eliminar():
            matricula = entry_matricula.get().strip()
            estudiante_encontrado = None
            for estudiante in self.estudiantes:
                if estudiante.matricula == matricula:
                    estudiante_encontrado = estudiante
                    break
            if estudiante_encontrado:
                self.estudiantes.remove(estudiante_encontrado)
                self.text_output.insert("end", f"Estudiante con matrícula '{matricula}' eliminado.\n")
            else:
                self.text_output.insert("end", f"No se encontró un estudiante con matrícula '{matricula}'.\n")
            ventana_eliminar_estudiante.destroy()

        boton_eliminar = ctk.CTkButton(ventana_eliminar_estudiante, text="Eliminar", command=eliminar)
        boton_eliminar.pack(pady=10)

    def mostrar_estudiantes(self):
        self.text_output.delete(1.0, "end")
        if not self.estudiantes:
            self.text_output.insert("end", "No hay estudiantes creados.\n")
        for estudiante in self.estudiantes:
            self.text_output.insert("end", f"Estudiante: {estudiante.nombre} {estudiante.apellido} | Matrícula: {estudiante.matricula} | Carrera: {estudiante.carrera}\n")

    # -------------------------------------------------
    # Grupos
    def crear_boton_grupos(self, frame):
        boton_crear_grupo = ctk.CTkButton(frame, text="Crear Grupo", command=self.crear_grupo)
        boton_crear_grupo.pack(pady=10)

        boton_eliminar_grupo = ctk.CTkButton(frame, text="Eliminar Grupo", command=self.eliminar_grupo)
        boton_eliminar_grupo.pack(pady=10)

        boton_mostrar_grupos = ctk.CTkButton(frame, text="Mostrar Grupos", command=self.mostrar_grupos)
        boton_mostrar_grupos.pack(pady=10)

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

        label_profesor = ctk.CTkLabel(ventana_grupo, text="Seleccione Profesor:")
        label_profesor.pack(pady=5)
        entry_profesor = ctk.CTkOptionMenu(ventana_grupo, values=[f"{p.nombre} {p.apellido}" for p in self.profesores])
        entry_profesor.pack(pady=5)

        def guardar_grupo():
            try:
                numero_grupo = int(entry_numero.get().strip())
                if numero_grupo <= 0:
                    self.text_output.insert("end", "El número de grupo debe ser un número positivo.\n")
                    return

                # Verificar si ya existe un grupo con ese número
                for grupo in self.grupos:
                    if grupo.numero_grupo == numero_grupo:
                        self.text_output.insert("end", f"El grupo con número {numero_grupo} ya existe.\n")
                        return

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

                # Crear el grupo
                grupo = Grupo(numero_grupo, asignatura_seleccionada, profesor_seleccionado)
                self.grupos.append(grupo)
                self.text_output.insert("end", f"Grupo {numero_grupo} creado con éxito.\n")
                ventana_grupo.destroy()

            except ValueError:
                self.text_output.insert("end", "El número de grupo debe ser un número entero válido.\n")

        boton_guardar = ctk.CTkButton(ventana_grupo, text="Guardar Grupo", command=guardar_grupo)
        boton_guardar.pack(pady=10)

    def eliminar_grupo(self):
        ventana_eliminar_grupo = ctk.CTkToplevel(self)
        ventana_eliminar_grupo.title("Eliminar Grupo")

        label_numero_grupo = ctk.CTkLabel(ventana_eliminar_grupo, text="Número del Grupo:")
        label_numero_grupo.pack(pady=5)
        entry_numero_grupo = ctk.CTkEntry(ventana_eliminar_grupo)
        entry_numero_grupo.pack(pady=5)

        def eliminar():
            try:
                numero_grupo = int(entry_numero_grupo.get().strip())
                grupo_encontrado = None
                for grupo in self.grupos:
                    if grupo.numero_grupo == numero_grupo:
                        grupo_encontrado = grupo
                        break
                if grupo_encontrado:
                    self.grupos.remove(grupo_encontrado)
                    self.text_output.insert("end", f"Grupo {numero_grupo} eliminado con éxito.\n")
                else:
                    self.text_output.insert("end", f"No se encontró un grupo con el número {numero_grupo}.\n")
                ventana_eliminar_grupo.destroy()
            except ValueError:
                self.text_output.insert("end", "Por favor, ingrese un número válido para el grupo.\n")

        boton_eliminar = ctk.CTkButton(ventana_eliminar_grupo, text="Eliminar", command=eliminar)
        boton_eliminar.pack(pady=10)

    def mostrar_grupos(self):
        self.text_output.delete(1.0, "end")
        if not self.grupos:
            self.text_output.insert("end", "No hay grupos creados.\n")
        for grupo in self.grupos:
            self.text_output.insert("end", f"Grupo {grupo.numero_grupo}: Asignatura: {grupo.asignatura.nombre}, Profesor: {grupo.profesor.nombre} {grupo.profesor.apellido}\n")

    # -------------------------------------------------
    # Programa Académico
    def crear_boton_programa(self, frame):
        boton_mostrar_programa = ctk.CTkButton(frame, text="Mostrar Programa Académico", command=self.mostrar_programa)
        boton_mostrar_programa.pack(pady=10)

    def mostrar_programa(self):
        self.text_output.delete(1.0, "end")
        if not self.grupos:
            self.text_output.insert("end", "No hay grupos en el programa académico.\n")
            return
        self.text_output.insert("end", f"Programa Académico: {self.programa_academico.nombre} ({self.programa_academico.codigo})\n")
        self.mostrar_grupos()

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")  # Modo oscuro de CustomTkinter
    ctk.set_default_color_theme("blue")  # Tema azul de CustomTkinter
    app = App()
    app.mainloop()
