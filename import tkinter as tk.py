import tkinter as tk
import keyboard

# Función para mostrar la ventana emergente con el mensaje centrado
def mostrar_ventana():
    ventana = tk.Tk()
    ventana.title("ERROR")
    
    # Remover bordes de la ventana
    ventana.overrideredirect(True)
    
    # Establecer tamaño
    ventana.geometry("200x200")
    
    # Crear un fondo
    frame = tk.Frame(ventana, bg="#3498db")
    frame.pack(expand=True, fill='both')
    
    # Agregar un texto centrado
    etiqueta = tk.Label(frame, text="Error C3L1D3R_03", bg="#3498db", fg="white", font=("Arial", 14))
    etiqueta.pack(expand=True)  # expand=True asegura que el texto se centre en ambos ejes
    
    # Hacer que la ventana aparezca centrada en la pantalla
    ventana.eval('tk::PlaceWindow . center')
    
    # Mantener la ventana abierta
    ventana.mainloop()

# Función para detectar la tecla 'h'
def detectar_tecla():
    while True:
        if keyboard.is_pressed('h'):
            mostrar_ventana()
            break

# Ejecuta la función para detectar la tecla
detectar_tecla()
