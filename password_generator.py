
# ============================================================
# Generatore di Password Sicure con Interfaccia Grafica
# Copyright (c) 2025 Andrea Tavolozza
# Tutti i diritti riservati.
#
# Licenza: MIT
# Repository: https://github.com/andreaelleti/Password-Generator
# ============================================================

import tkinter as tk
from tkinter import messagebox
import secrets
import string

def genera_password(lunghezza):
    caratteri = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(caratteri) for _ in range(lunghezza))

def genera():
    try:
        lunghezza = int(entry_lunghezza.get())
        if lunghezza < 8:
            messagebox.showwarning("Attenzione", "La lunghezza minima consigliata è 8 caratteri.")
            return
        password = genera_password(lunghezza)
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
    except ValueError:
        messagebox.showerror("Errore", "Inserisci un numero valido per la lunghezza.")

def copia_password():
    root.clipboard_clear()
    root.clipboard_append(entry_password.get())
    messagebox.showinfo("Copiato", "Password copiata negli appunti!")

# Creazione finestra principale
root = tk.Tk()
root.title("Generatore di Password Sicure")

# Etichetta e campo per la lunghezza
tk.Label(root, text="Lunghezza password:").grid(row=0, column=0, padx=10, pady=10)
entry_lunghezza = tk.Entry(root)
entry_lunghezza.insert(0, "20")
entry_lunghezza.grid(row=0, column=1, padx=10, pady=10)

# Pulsante per generare la password
btn_genera = tk.Button(root, text="Genera Password", command=genera)
btn_genera.grid(row=1, column=0, columnspan=2, pady=10)

# Campo per visualizzare la password generata
entry_password = tk.Entry(root, width=40)
entry_password.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Pulsante per copiare la password
btn_copia = tk.Button(root, text="Copia negli Appunti", command=copia_password)
btn_copia.grid(row=3, column=0, columnspan=2, pady=10)

# Avvio dell'interfaccia
root.mainloop()
