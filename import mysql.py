import mysql.connector
import tkinter as tk
from tkinter import messagebox

db = mysql.connector.connect(
    host="localhost",
    user="root",
    database="ejercicio_CRUD_Phyton",
    password = ""
)

def insertar_registro(nombre, apellido, fecha_nacimiento, telefono, email, cargo, salario):
    cursor = db.cursor()
    sql = "INSERT INTO empleados (nombres, apellidos, fecha_nacimiento, telefono, email, cargo, salario) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    valores = (nombre, apellido, fecha_nacimiento, telefono, email, cargo, salario)
    cursor.execute(sql, valores)
    db.commit()

    cursor.close()

def abrir_ventana_insertar_registro():
    def insertar_registro_auxiliar():
        nombre = entry_nombre.get()
        apellido = entry_apellido.get()
        fecha_nacimiento = entry_fecha_nacimiento.get()
        telefono = entry_telefono.get()
        email = entry_email.get()
        cargo = entry_cargo.get()
        salario = float(entry_salario.get())

        insertar_registro(nombre, apellido, fecha_nacimiento, telefono, email, cargo, salario)
        ventana_insertar_registro.destroy()

    ventana_insertar_registro = tk.Toplevel()
    ventana_insertar_registro.title("Insertar registro")

    # Crear etiquetas y campos de entrada
    etiqueta_nombre = tk.Label(ventana_insertar_registro, text="Nombre:")
    etiqueta_nombre.grid(row=0, column=0, padx=10, pady=5)

    entry_nombre = tk.Entry(ventana_insertar_registro)
    entry_nombre.grid(row=0, column=1, padx=10, pady=5)

    etiqueta_apellido = tk.Label(ventana_insertar_registro, text="Apellido:")
    etiqueta_apellido.grid(row=1, column=0, padx=10, pady=5)

    entry_apellido = tk.Entry(ventana_insertar_registro)
    entry_apellido.grid(row=1, column=1, padx=10, pady=5)

    etiqueta_fecha_nacimiento = tk.Label(ventana_insertar_registro, text="Fecha de nacimiento (YYYY-MM-DD):")
    etiqueta_fecha_nacimiento.grid(row=2, column=0, padx=10, pady=5)

    entry_fecha_nacimiento = tk.Entry(ventana_insertar_registro)
    entry_fecha_nacimiento.grid(row=2, column=1, padx=10, pady=5)

    etiqueta_telefono = tk.Label(ventana_insertar_registro, text="Teléfono:")
    etiqueta_telefono.grid(row=3, column=0, padx=10, pady=5)

    entry_telefono = tk.Entry(ventana_insertar_registro)
    entry_telefono.grid(row=3, column=1, padx=10, pady=5)

    etiqueta_email = tk.Label(ventana_insertar_registro, text="Email:")
    etiqueta_email.grid(row=4, column=0, padx=10, pady=5)

    entry_email = tk.Entry(ventana_insertar_registro)
    entry_email.grid(row=4, column=1, padx=10, pady=5)

    etiqueta_cargo = tk.Label(ventana_insertar_registro, text="Cargo:")
    etiqueta_cargo.grid(row=5, column=0, padx=10, pady=5)

    entry_cargo = tk.Entry(ventana_insertar_registro)
    entry_cargo.grid(row=5, column=1, padx=10, pady=5)

    etiqueta_salario = tk.Label(ventana_insertar_registro, text="Salario:")
    etiqueta_salario.grid(row=6, column=0, padx=10, pady=5)

    entry_salario = tk.Entry(ventana_insertar_registro)
    entry_salario.grid(row=6, column=1, padx=10, pady=5)

    # Crear botón para guardar
    boton_guardar = tk.Button(ventana_insertar_registro, text="Guardar", command=insertar_registro_auxiliar)
    boton_guardar.grid(row=7, column=0, columnspan=2, padx=10, pady=10)


def leer_registros():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM empleados")
    registros = cursor.fetchall()

    for registro in registros:
        print(registro)
    cursor.close()

def modificar_registro(id_empleado, nombre, apellido, salario):
    cursor = db.cursor()
    sql = "UPDATE empleados SET nombres = %s, apellidos = %s, salario = %s WHERE id = %s"
    valores = (nombre, apellido, salario, id_empleado)
    cursor.execute(sql, valores)
    db.commit()

    cursor.close()

def abrir_ventana_modificar_registro():
    def modificar_registro_auxiliar():
        id_empleado = int(entry_id_empleado.get())
        nombre = entry_nombre.get()
        apellido = entry_apellido.get()
        salario = float(entry_salario.get())

        modificar_registro(id_empleado, nombre, apellido, salario)
        ventana_modificar_registro.destroy()

    ventana_modificar_registro = tk.Toplevel()
    ventana_modificar_registro.title("Modificar registro")

    # Crear etiquetas y campos de entrada
    etiqueta_id_empleado = tk.Label(ventana_modificar_registro, text="ID empleado:")
    etiqueta_id_empleado.grid(row=0, column=0, padx=10, pady=5)

    entry_id_empleado = tk.Entry(ventana_modificar_registro)
    entry_id_empleado.grid(row=0, column=1, padx=10, pady=5)

    etiqueta_nombre = tk.Label(ventana_modificar_registro, text="Nombre:")
    etiqueta_nombre.grid(row=1, column=0, padx=10, pady=5)

    entry_nombre = tk.Entry(ventana_modificar_registro)
    entry_nombre.grid(row=1, column=1, padx=10, pady=5)

    etiqueta_apellido = tk.Label(ventana_modificar_registro, text="Apellido:")
    etiqueta_apellido.grid(row=2, column=0, padx=10, pady=5)

    entry_apellido = tk.Entry(ventana_modificar_registro)
    entry_apellido.grid(row=2, column=1, padx=10, pady=5)

    etiqueta_salario = tk.Label(ventana_modificar_registro, text="Salario:")
    etiqueta_salario.grid(row=3, column=0, padx=10, pady=5)

    entry_salario = tk.Entry(ventana_modificar_registro)
    entry_salario.grid(row=3, column=1, padx=10, pady=5)

    # Crear botón para modificar
    boton_modificar = tk.Button(ventana_modificar_registro, text="Modificar", command=modificar_registro_auxiliar)
    boton_modificar.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

def eliminar_registro(id_empleado):
    cursor = db.cursor()
    sql = "DELETE FROM empleados WHERE id = %s"
    valores = (id_empleado,)
    cursor.execute(sql, valores)
    db.commit()

    cursor.close() 

def abrir_ventana_eliminar_registro():
    def eliminar_registro_auxiliar():
        id_empleado = int(entry_id_empleado.get())

        eliminar_registro(id_empleado)
        ventana_eliminar_registro.destroy()

    ventana_eliminar_registro = tk.Toplevel()
    ventana_eliminar_registro.title("Eliminar registro")

    # Crear etiqueta y campo de entrada
    etiqueta_id_empleado = tk.Label(ventana_eliminar_registro, text="ID empleado:")
    etiqueta_id_empleado.grid(row=0, column=0, padx=10, pady=5)

    entry_id_empleado = tk.Entry(ventana_eliminar_registro)
    entry_id_empleado.grid(row=0, column=1, padx=10, pady=5)

    # Crear botón para eliminar
    boton_eliminar = tk.Button(ventana_eliminar_registro, text="Eliminar", command=eliminar_registro_auxiliar)
    boton_eliminar.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    # Aviso de confirmación
    messagebox.showwarning("¡Atención!", "¿Está seguro de que desea eliminar este registro? Esta acción es irreversible.")

def crear_ventana_principal():
    # Crear ventana principal
    ventana_principal = tk.Tk()
    ventana_principal.title("Menú Principal - CRUD Empleados")

    # Crear etiquetas
    etiqueta_titulo = tk.Label(ventana_principal, text="Menú Principal", font=("Arial", 23, "bold"))
    etiqueta_titulo.grid(row=0, column=0, columnspan=10, padx=70, pady=30)

    etiqueta_leer_registros = tk.Label(ventana_principal, text="1. Leer registros")
    etiqueta_leer_registros.grid(row=1, column=0, padx=30, pady=25)

    etiqueta_insertar_registro = tk.Label(ventana_principal, text="2. Insertar registro")
    etiqueta_insertar_registro.grid(row=2, column=0, padx=30, pady=25)

    etiqueta_modificar_registro = tk.Label(ventana_principal, text="3. Modificar registro")
    etiqueta_modificar_registro.grid(row=3, column=0, padx=30, pady=25)

    etiqueta_eliminar_registro = tk.Label(ventana_principal, text="4. Eliminar registro")
    etiqueta_eliminar_registro.grid(row=4, column=0, padx=30, pady=25)

    etiqueta_salir = tk.Label(ventana_principal, text="5. Salir")
    etiqueta_salir.grid(row=5, column=0, padx=30, pady=30)

    # Crear botones
    boton_leer_registros = tk.Button(ventana_principal, text="Leer", command=leer_registros)
    boton_leer_registros.grid(row=1, column=1, padx=10, pady=5)

    boton_insertar_registro = tk.Button(ventana_principal, text="Insertar", command=abrir_ventana_insertar_registro)
    boton_insertar_registro.grid(row=2, column=1, padx=10, pady=5)

    boton_modificar_registro = tk.Button(ventana_principal, text="Modificar", command=abrir_ventana_modificar_registro)
    boton_modificar_registro.grid(row=3, column=1, padx=10, pady=5)

    boton_eliminar_registro = tk.Button(ventana_principal, text="Eliminar", command=abrir_ventana_eliminar_registro)
    boton_eliminar_registro.grid(row=4, column=1, padx=10, pady=5)

    boton_salir = tk.Button(ventana_principal, text="Salir", command=ventana_principal.quit)
    boton_salir.grid(row=5, column=1, padx=10, pady=10)

    # Mantener la ventana abierta
    ventana_principal.mainloop()     

crear_ventana_principal()

db.close()

