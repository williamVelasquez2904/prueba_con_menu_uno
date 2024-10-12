import tkinter as tk
from tkinter import messagebox
from menu_principal import menu_principal  # Importa la función del menú principal

# Función para validar el login
def validar_login():
    usuario = entry_usuario.get()
    clave = entry_clave.get()
    
    # Supongamos que estos son los credenciales correctos
    if usuario == "admin" and clave == "admin123":
        messagebox.showinfo("Login correcto", "Bienvenido a la UNIDAD MEDICA SAN LUIS")
        abrir_menu_principal()
    else:
        messagebox.showerror("Error", "Usuario o clave incorrectos")

# Función para abrir el menú principal
def abrir_menu_principal():
    login_window.destroy()
    menu_principal()

# Crear la ventana de login
login_window = tk.Tk()
login_window.title("Login")

tk.Label(login_window, text="Usuario").grid(row=0, column=0)
tk.Label(login_window, text="Clave").grid(row=1, column=0)

entry_usuario = tk.Entry(login_window)
entry_clave = tk.Entry(login_window, show="*")

entry_usuario.grid(row=0, column=1)
entry_clave.grid(row=1, column=1)

tk.Button(login_window, text="Login", command=validar_login).grid(row=2, column=0, columnspan=2)

login_window.mainloop()
