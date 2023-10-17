import tkinter as tk
import mysql.connector
# from ttkbootstrap import Style
from tkinter import ttk, messagebox


def add_note():
    # Creacion de la ventana de tkinter
    root = tk.Toplevel(root1)
    root.geometry("500x500")
    root.title('Insertar Datos en la Base de Datos')
    
    # Estilos para los widgets
    label_style = ("Arial", 12)
    entry_style = ("Arial", 12)

    
    # Widgets de entrada
    label_nombre = tk.Label(root, text="Nombre:", font=label_style)
    label_nombre.pack()
    nombre_entry = tk.Entry(root, font=entry_style)
    nombre_entry.pack(padx=10, pady=5)


    # Widgets de entrada edad
    label_edad = tk.Label(root, text="Edad:", font=label_style)
    label_edad.pack()
    edad_entry = tk.Entry(root, font=entry_style)
    edad_entry.pack(padx=10, pady=5)


    # Widgets de entrada usuario
    label_nombre_usuario = tk.Label(root, text="Usuario:", font=label_style)
    label_nombre_usuario.pack()
    nombre_usuario_entry = tk.Entry(root, font=entry_style)
    nombre_usuario_entry.pack(padx=10, pady=5)

    # Widgets de entrada email
    label_email = tk.Label(root, text="Email:", font=label_style)
    label_email.pack()
    email_entry = tk.Entry(root, font=entry_style)
    email_entry.pack(padx=10, pady=5)

    # Widgets de entrada telefono
    label_telefono = tk.Label(root, text="Telefono:", font=label_style)
    label_telefono.pack()
    numero_telefonico_entry = tk.Entry(root, font=entry_style)
    numero_telefonico_entry.pack(padx=10, pady=5)

    # Widgets de entrada empresa
    label_empresa = tk.Label(root, text="Empresa:", font=label_style)
    label_empresa.pack()
    empresa_entry = tk.Entry(root, font=entry_style)
    empresa_entry.pack(padx=10, pady=5)
    

    # FUNCION PARA GUARDAR DATOS:
    def save_data():
        nombre = nombre_entry.get()
        edad = edad_entry.get()
        nombre_usuario = nombre_usuario_entry.get()
        email = email_entry.get()
        numero_telefonico = numero_telefonico_entry.get()
        empresa = empresa_entry.get()
    
        # Conexion la base de datos
        conexion_guardar_Data = mysql.connector.connect(
            host="localhost",
            user= "root",
            password="-.Enmanuel0202.-",
            database="users_DataBase",
            port=3306
        )
    
        # Objeto cursor
        cursor = conexion_guardar_Data.cursor()
    
        # Consulta para ensertar los datos a la tabla
        consulta = "INSERT INTO users2 (nombre, edad, username, email, numero_telefonico, empresa) VALUES(%s, %s, %s,%s, %s, %s)"
    
        # Datos a insertar
        datos = (nombre, edad, nombre_usuario, email, numero_telefonico, empresa)
    
        # Ejecutar la consulta utilizando el método execute() del objeto cursor
        cursor.execute(consulta, datos)
    
        # Confirmar la transaccion
        conexion_guardar_Data.commit()
        
        # Cerrar la conexion y el cursor
        cursor.close()
        conexion_guardar_Data.close()
        
        # Conectar a la base de datos MySQL
        conexion_mostrar_Data = mysql.connector.connect(
            host="localhost",
            user= "root",
            password="-.Enmanuel0202.-",
            database="users_DataBase",
            port=3306
        )

        # Crear un cursor para ejecutar consultas
        cursor1 = conexion_mostrar_Data.cursor()

        # Consulta SQL para seleccionar todos los datos de la tabla
        consulta_mostrar_datos = "SELECT * FROM users2"

        # Ejecutar la consulta
        cursor1.execute(consulta_mostrar_datos)

        # Obtener todos los registros
        filas = cursor1.fetchall()
    
        filas_actuales = [tree.item(item, 'values') for item in tree.get_children()]
    
        for row in tree.get_children():
            tree.delete(row)
    
    
        for fila in filas:
            if fila not in filas_actuales:
                tree.insert("", "end", values=fila)
    
        # Limpiar los campos una vez se haya completado los datos
        nombre_entry.delete(0, tk.END)
        edad_entry.delete(0, tk.END)
        nombre_usuario_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        numero_telefonico_entry.delete(0, tk.END)
        empresa_entry.delete(0, tk.END)
        
    
    # Estilo para los botones
    button_style = ("Arial", 14, "bold")
    # BOTON PARA ENVIAR DATOS:
    save_button = tk.Button(root, command=save_data, text="Ingresar Datos", font=button_style,bg='#4CAF50', fg='white')
    save_button.pack(pady=20)
    
    
# FRONTEND:

    # # Estilos para los widgets
    # label_style = ("Arial", 12)
    # entry_style = ("Arial", 12)
    # button_style = ("Arial", 14, "bold")

    # # Widgets de entrada
    # label_nombre = tk.Label(root, text="Nombre:", font=label_style)
    # label_nombre.pack()
    # nombre_entry = tk.Entry(root, font=entry_style)
    # nombre_entry.pack(padx=10, pady=5)


    # # Widgets de entrada edad
    # label_edad = tk.Label(root, text="Edad:", font=label_style)
    # label_edad.pack()
    # edad_entry = tk.Entry(root, font=entry_style)
    # edad_entry.pack(padx=10, pady=5)


    # # Widgets de entrada usuario
    # label_nombre_usuario = tk.Label(root, text="Usuario:", font=label_style)
    # label_nombre_usuario.pack()
    # nombre_usuario_entry = tk.Entry(root, font=entry_style)
    # nombre_usuario_entry.pack(padx=10, pady=5)

    # # Widgets de entrada email
    # label_email = tk.Label(root, text="Email:", font=label_style)
    # label_email.pack()
    # email_entry = tk.Entry(root, font=entry_style)
    # email_entry.pack(padx=10, pady=5)

    # # Widgets de entrada telefono
    # label_telefono = tk.Label(root, text="Telefono:", font=label_style)
    # label_telefono.pack()
    # numero_telefonico_entry = tk.Entry(root, font=entry_style)
    # numero_telefonico_entry.pack(padx=10, pady=5)

    # # Widgets de entrada empresa
    # label_empresa = tk.Label(root, text="Empresa:", font=label_style)
    # label_empresa.pack()
    # empresa_entry = tk.Entry(root, font=entry_style)
    # empresa_entry.pack(padx=10, pady=5)

    # # Boton para enviar datos
    # boton_enviar = tk.Button(root, text='Insertar Datos', command=insert_data, font=button_style, bg='#4CAF50', fg='white')
    # boton_enviar.pack(pady=20)


# FUNCION PARA ELIMINAR DATOS:
def eliminar_Data():
    conn = mysql.connector.connect(
        host="localhost",
        user= "root",
        password="-.Enmanuel0202.-",
        database="users_DataBase",
        port=3306
    )
    
    # Obtener el ID de la fila seleccionada en el Treeview
    x = tree.selection()[0]
    
    # Eliminar la fila seleccionada
    tree.delete(x)
   
    # Objeto cursor 
    cursor_eliminar_Datos = conn.cursor()
    
    # Consulta para eliminar datos 
    consulta_eliminar_Data = "DELETE FROM users2 WHERE id=%s"
    
    # Ejecutar la consulta 
    cursor_eliminar_Datos.execute(consulta_eliminar_Data, (x,))
    
    # Confirmar la transaccion  
    conn.commit()
    
    # Cerrar la conexion a la base de datos
    conn.close()
    


# VENTANA PARA EL TREEVIEW: 

# Conectar a la base de datos MySQL
conexion_mostrar_Data = mysql.connector.connect(
    host="localhost",
    user= "root",
    password="-.Enmanuel0202.-",
    database="users_DataBase",
    port=3306
)


# Crear un cursor para ejecutar consultas
cursor_mostrar_datos = conexion_mostrar_Data.cursor()

# Consulta SQL para seleccionar todos los datos de la tabla
consulta_mostrar_datos = "SELECT * FROM users2"

# Ejecutar la consulta
cursor_mostrar_datos.execute(consulta_mostrar_datos)

# Obtener todos los registros
filas = cursor_mostrar_datos.fetchall()

# Función para cerrar la conexión a la base de datos
def cerrar_conexion():
    conexion_mostrar_Data.close()
    root1.destroy()
        
# VENTANA PRINCIPAL
root1 = tk.Tk()
root1.title("Datos de la Tabla de Usuarios")



# Crear un Treeview en root1 para mostrar los datos
tree = ttk.Treeview(root1)
# Asignar los nombres de las columnas al treeview
tree["columns"] = tuple(cursor_mostrar_datos.column_names)


# Configurar encabezados de las columnas
for col in cursor_mostrar_datos.column_names:
    tree.column(col, anchor="s")
    tree.heading(col, text=col)
    


# Insertar datos en el Treeview
for i in filas:
    tree.insert("", "end", iid=i[0], values=i)

tree.pack(padx=20, pady=20)

# Estilo para los botones
button_style1 = ("Arial", 14, "bold")

# Botón para cerrar la conexión y salir
boton_cerrar = tk.Button(root1, text="Cerrar", command=cerrar_conexion,
                         font=button_style1, bg='#4CAF50', fg='white')
boton_cerrar.pack(pady=20)
    
# Boton para eliminar la fila seleccionada
boton_eliminar = tk.Button(root1, text="Eliminar Fila", command=eliminar_Data,
                           font=button_style1, bg='#4CAF50', fg='white')
boton_eliminar.pack(pady=20, padx=20)
    
# Boton para añadir nuevos datos
boton_abrir = tk.Button(root1,text="Añadir Registro", command=add_note,
                        font=button_style1, bg='#4CAF50', fg='white')
boton_abrir.pack(pady=20, padx=20)

# Ejecutar el bucle principal de Tkinter
root1.mainloop()