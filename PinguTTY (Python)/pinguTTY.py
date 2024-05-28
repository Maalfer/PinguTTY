# Hecho por jaavii_rodrgzz para ElPingüinoDeMario 🐧
# Hecho por jaavii_rodrgzz para ElPingüinoDeMario 🐧
# Hecho por jaavii_rodrgzz para ElPingüinoDeMario 🐧

import customtkinter
from tkinter import messagebox
import tkinter.font as tkFont

app = customtkinter.CTk()
app.title("PinguTTY")
app.geometry("400x300")

titulo = customtkinter.CTkLabel(app, text="PinguTTY", font=("Arial", 25))
titulo.place(x=145, y=15)
def instrucciones():
    messagebox.showinfo("Instrucciones de uso", "Estas son las instrucciones de uso:\n\nAplicación para vagos, de tal forma que puedan hacer el tratamiento de la TTY copiando y pegando.\n\nCada vez que se haga clic en uno de los pasos, el comando se copiará al portapapeles")

def paso1():
    messagebox.showinfo("Paso 1", "Copiado al portapapeles: script /dev/null -c bash")

    texto = "script /dev/null -c bash"
    app.clipboard_clear()
    app.clipboard_append(texto)
    app.update()

def paso2():
    messagebox.showinfo("Paso 2", "Copiado al portapapeles: stty raw -echo; fg")

    texto = "stty raw -echo; fg"
    app.clipboard_clear()
    app.clipboard_append(texto)
    app.update()

def paso3():
    messagebox.showinfo("Paso 3", "Copiado al portapapeles: reset xterm")

    texto = "reset xterm"
    app.clipboard_clear()
    app.clipboard_append(texto)
    app.update()

def paso4():
    messagebox.showinfo("Paso 4", "Copiado al portapapeles: export SHELL=bash && export TERM=xterm")

    texto = "export SHELL=bash && export TERM=xterm"
    app.clipboard_clear()
    app.clipboard_append(texto)
    app.update()

botonInstrucciones = customtkinter.CTkButton(app, text="Instrucciones", text_color="black", hover=False, command=instrucciones)
botonInstrucciones.place(x=130, y=60)

botonPaso1 = customtkinter.CTkButton(app, text="Paso 1", fg_color="green", text_color="black", hover=False, command=paso1)
botonPaso1.place(x=30, y=150)

botonPaso2 = customtkinter.CTkButton(app, text="Paso 2", fg_color="#d93d32", text_color="black", hover=False, command=paso2)
botonPaso2.place(x=230, y=150)

botonPaso3 = customtkinter.CTkButton(app, text="Paso 3", fg_color="#b0b312", text_color="black", hover=False, command=paso3)
botonPaso3.place(x=30, y=230)

botonPaso4 = customtkinter.CTkButton(app, text="Paso 4", fg_color="purple", text_color="black", hover=False, command=paso4)
botonPaso4.place(x=230, y=230)

app.mainloop()
