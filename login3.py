import tkinter as tk
from tkinter import messagebox

# Función para centrar la ventana en la pantalla
def centrar_ventana(ventana, ancho, alto):
    screen_width = ventana.winfo_screenwidth()
    screen_height = ventana.winfo_screenheight()
    
    x = (screen_width // 2) - (ancho // 2)
    y = (screen_height // 2) - (alto // 2)
    ventana.geometry(f'{ancho}x{alto}+{x}+{y}')

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
    from menu_principal import menu_principal
    menu_principal()

# Crear la ventana de login
login_window = tk.Tk()
login_window.title("Inicio de sesión")

# Centrar y ajustar el tamaño de la ventana
centrar_ventana(login_window, 400, 400)

# Título
tk.Label(login_window, text="Inicio de sesión", font=("Arial", 18)).pack(pady=10)

# Imagen alusiva al inicio de sesión
imagen = tk.PhotoImage(file="img/inicio_imagen.png")  # Ajusta la ruta de la imagen
tk.Label(login_window, image=imagen).pack(pady=10)

# Campos de usuario y clave
tk.Label(login_window, text="Usuario").pack(pady=5)
entry_usuario = tk.Entry(login_window)
entry_usuario.pack(pady=5)

tk.Label(login_window, text="Clave").pack(pady=5)
entry_clave = tk.Entry(login_window, show="*")
entry_clave.pack(pady=5)

tk.Button(login_window, text="Login", command=validar_login).pack(pady=20)

login_window.mainloop()
