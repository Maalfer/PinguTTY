# Hecho por jaavii_rodrgzz para ElPingüinoDeMario 🐧
# Hecho por jaavii_rodrgzz para ElPingüinoDeMario 🐧
# Hecho por jaavii_rodrgzz para ElPingüinoDeMario 🐧

import customtkinter
from tkinter import messagebox

app = customtkinter.CTk()
app.title("PinguTTY")
app.resizable(False, False)
app.geometry("400x300")

titulo = customtkinter.CTkLabel(app, text="PinguTTY", font=("Arial", 25))
titulo.place(x=145, y=15)
def instrucciones():
    messagebox.showinfo("Instrucciones de uso", "Estas son las instrucciones de uso:\n\nAplicación para vagos, de tal forma que puedan hacer el tratamiento de la TTY copiando y pegando.\n\nCada vez que se haga clic en uno de los pasos, el comando se copiará al portapapeles")

def paso1():
    texto1 = "script /dev/null -c bash"
    app.clipboard_clear()
    app.clipboard_append(texto1)
    app.update()

    messagebox.showinfo("Paso 1", "Copiado al portapapeles: script /dev/null -c bash")

def paso2():
    texto2 = "stty raw -echo; fg"
    app.clipboard_clear()
    app.clipboard_append(texto2)
    app.update()

    messagebox.showinfo("Paso 2", "Copiado al portapapeles: stty raw -echo; fg")

def paso3():
    texto3 = "reset xterm"
    app.clipboard_clear()
    app.clipboard_append(texto3)
    app.update()

    messagebox.showinfo("Paso 3", "Copiado al portapapeles: reset xterm")

def paso4():
    texto4 = "export SHELL=bash && export TERM=xterm"
    app.clipboard_clear()
    app.clipboard_append(texto4)
    app.update()

    messagebox.showinfo("Paso 4", "Copiado al portapapeles: export SHELL=bash && export TERM=xterm")

botonInstrucciones = customtkinter.CTkButton(app, text="Instrucciones", corner_radius=15, border_color="black", border_width=2, height=40, text_color="black", hover=False, command=instrucciones)
botonInstrucciones.place(x=130, y=60)

botonPaso1 = customtkinter.CTkButton(app, text="Paso 1", fg_color="green", corner_radius=15, border_color="black", border_width=2, height=40, text_color="black", hover=False, command=paso1)
botonPaso1.place(x=30, y=150)

botonPaso2 = customtkinter.CTkButton(app, text="Paso 2", fg_color="#d93d32", corner_radius=15, border_color="black", border_width=2, height=40, text_color="black", hover=False, command=paso2)
botonPaso2.place(x=230, y=150)

botonPaso3 = customtkinter.CTkButton(app, text="Paso 3", fg_color="#b0b312", corner_radius=15, border_color="black", border_width=2, height=40, text_color="black", hover=False, command=paso3)
botonPaso3.place(x=30, y=230)

botonPaso4 = customtkinter.CTkButton(app, text="Paso 4", fg_color="purple", corner_radius=15, border_color="black", border_width=2, height=40, text_color="black", hover=False, command=paso4)
botonPaso4.place(x=230, y=230)

app.mainloop()