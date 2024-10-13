import socket
import tkinter as tk
from datetime import datetime

# Función para mostrar la fecha y hora actual
def mostrar_fecha_hora():
    ahora = datetime.now()
    fecha_hora = ahora.strftime("%Y-%m-%d %H:%M:%S")
    label_fecha_hora.config(text=fecha_hora)
    menu_window.after(1000, mostrar_fecha_hora)  # Actualizar cada segundo

# Crear la ventana del menú principal
def menu_principal():
    global menu_window
    menu_window = tk.Tk()
    menu_window.title("Menu Principal")

     # Encabezado con logo y texto
    
    titulo="CONTROL DE DEVOLUCIONES"
    ruta_logo="img/logo_empresa.png"
    nombre_maquina=socket.gethostname()
    if nombre_maquina=='WilliamJose':
        titulo="UNIDAD MEDICA SAN LUIS"
        ruta_logo="img/logo_umsl.png"

    # Enruta_logo="img/logo_empresa.png"cabezado con logo y texto
    logo = tk.PhotoImage(file=ruta_logo)  # Asegúrate de ajustar la ruta del logo
    encabezado = tk.Frame(menu_window)
    encabezado.pack(side=tk.TOP, fill=tk.X)
    
    tk.Label(encabezado, image=logo).pack(side=tk.LEFT)
    #tk.Label(menu_window, text=titulo, font=("Arial", 24)).grid(row=0, column=1)
    tk.Label(encabezado, text=titulo, font=("Arial", 18)).pack(side=tk.LEFT, expand=True)
    
    global label_fecha_hora
    label_fecha_hora = tk.Label(encabezado, text="", font=("Arial", 12))
    label_fecha_hora.pack(side=tk.RIGHT)
    mostrar_fecha_hora()

    # Menú principal
    menu_frame = tk.Frame(menu_window)
    menu_frame.pack(side=tk.TOP, pady=20)

    tk.Button(menu_frame, text="Usuarios").pack(side=tk.LEFT, padx=10)
    tk.Button(menu_frame, text="Maestros", command=mostrar_submenu_maestros).pack(side=tk.LEFT, padx=10)
    tk.Button(menu_frame, text="Procesos").pack(side=tk.LEFT, padx=10)
    tk.Button(menu_frame, text="Reportes").pack(side=tk.LEFT, padx=10)
    tk.Button(menu_frame, text="Salir", command=menu_window.quit).pack(side=tk.LEFT, padx=10)

    menu_window.mainloop()

# Función para mostrar el submenú de Maestros
def mostrar_submenu_maestros():
    submenu_maestros = tk.Toplevel(menu_window)
    submenu_maestros.title("Maestros")

    tk.Button(submenu_maestros, text="Pacientes", command=abrir_pacientes).pack(side=tk.TOP, pady=5)
    tk.Button(submenu_maestros, text="Enfermedades").pack(side=tk.TOP, pady=5)
    tk.Button(submenu_maestros, text="Empresas").pack(side=tk.TOP, pady=5)
    tk.Button(submenu_maestros, text="Cargos", command=abrir_cargos).pack(side=tk.TOP, pady=5)

# Función para abrir la pantalla de Pacientes
def abrir_pacientes():
    pacientes_window = tk.Toplevel(menu_window)
    pacientes_window.title("Pacientes")
    tk.Label(pacientes_window, text="CRUD Pacientes").pack()

    # Aquí iría el código para el CRUD de Pacientes

# Función para abrir la pantalla de Cargos
def abrir_cargos():
    cargos_window = tk.Toplevel(menu_window)
    cargos_window.title("Cargos")
    tk.Label(cargos_window, text="CRUD Cargos").pack()

    # Aquí iría el código para el CRUD de Cargos

# Esto asegura que el archivo no ejecute nada accidentalmente si se importa desde otro lugar
if __name__ == "__main__":
    menu_principal()
