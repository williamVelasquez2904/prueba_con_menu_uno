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
    titulo="UNIDAD MEDICA SAN LUIS"
    titulo="CONTROL DE DEVOLUCIONES"
    logo = tk.PhotoImage(file="logo.png")  # Asegúrate de ajustar la ruta del logo
    tk.Label(menu_window, image=logo).grid(row=0, column=0)
    tk.Label(menu_window, text=titulo, font=("Arial", 24)).grid(row=0, column=1)
    
    global label_fecha_hora
    label_fecha_hora = tk.Label(menu_window, text="", font=("Arial", 12))
    label_fecha_hora.grid(row=0, column=2)
    mostrar_fecha_hora()

    # Menú principal
    tk.Button(menu_window, text="Usuarios").grid(row=1, column=0)
    tk.Button(menu_window, text="Maestros", command=mostrar_submenu_maestros).grid(row=1, column=1)
    tk.Button(menu_window, text="Procesos").grid(row=1, column=2)
    tk.Button(menu_window, text="Reportes").grid(row=1, column=3)
    tk.Button(menu_window, text="Salir", command=menu_window.quit).grid(row=1, column=4)

    menu_window.mainloop()

# Función para mostrar el submenú de Maestros
def mostrar_submenu_maestros():
    submenu_maestros = tk.Toplevel(menu_window)
    submenu_maestros.title("Maestros")

    tk.Button(submenu_maestros, text="Pacientes", command=abrir_pacientes).grid(row=0, column=0)
    tk.Button(submenu_maestros, text="Enfermedades").grid(row=0, column=1)
    tk.Button(submenu_maestros, text="Empresas").grid(row=0, column=2)
    tk.Button(submenu_maestros, text="Cargos", command=abrir_cargos).grid(row=0, column=3)

# Función para abrir la pantalla de Pacientes
def abrir_pacientes():
    pacientes_window = tk.Toplevel(menu_window)
    pacientes_window.title("Pacientes")
    tk.Label(pacientes_window, text="CRUD Pacientes").grid(row=0, column=0)

    # Aquí iría el código para el CRUD de Pacientes

# Función para abrir la pantalla de Cargos
def abrir_cargos():
    cargos_window = tk.Toplevel(menu_window)
    cargos_window.title("Cargos")
    tk.Label(cargos_window, text="CRUD Cargos").grid(row=0, column=0)

    # Aquí iría el código para el CRUD de Cargos

# Esto asegura que el archivo no ejecute nada accidentalmente si se importa desde otro lugar
if __name__ == "__main__":
    menu_principal()
