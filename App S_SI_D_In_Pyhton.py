import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import os

# Declaración de variables globales
dataSecuencialFilePath = ""
indexSecuencialIndexFilePath = ""
dataSecuencialIndexFilePath = ""
dataDirectedFilePath = ""

class SecuencialesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación Secuenciales")

        # Labels
        self.label_id = tk.Label(root, text="ID:")
        self.label_id.grid(row=0, column=0, padx=5, pady=5)

        self.label_nombre = tk.Label(root, text="Nombre:")
        self.label_nombre.grid(row=1, column=0, padx=5, pady=5)

        self.label_nota = tk.Label(root, text="Nota:")
        self.label_nota.grid(row=2, column=0, padx=5, pady=5)

        # TextBox
        self.id_textbox = tk.Entry(root)
        self.id_textbox.grid(row=0, column=1, padx=5, pady=5)

        self.nombre_textbox = tk.Entry(root)
        self.nombre_textbox.grid(row=1, column=1, padx=5, pady=5)

        self.nota_textbox = tk.Entry(root)
        self.nota_textbox.grid(row=2, column=1, padx=5, pady=5)

        # Botones
        self.open_file_button = tk.Button(root, text="Abrir Archivo", command=self.open_file)
        self.open_file_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.save_folder_button = tk.Button(root, text="Guardar Carpeta", command=self.save_folder)
        self.save_folder_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.add_data_button = tk.Button(root, text="Agregar Datos", command=self.add_data)
        self.add_data_button.grid(row=5, column=0, columnspan=2, pady=10)

        # ListBox
        self.listbox = tk.Listbox(root)
        self.listbox.grid(row=6, column=0, columnspan=2, pady=10)

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            global dataSecuencialFilePath
            dataSecuencialFilePath = file_path
            
            # Llamamos al método UpdateList
            self.update_list()
            
    def update_list(self):
        self.listbox.delete(0, tk.END)  # Limpiamos el contenido actual del ListBox

        if os.path.exists(dataSecuencialFilePath):
            with open(dataSecuencialFilePath, "r") as file:
                    lines = file.readlines()
                    self.listbox.insert(tk.END, *lines)
                

    def save_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            global dataDirectedFilePath
            dataDirectedFilePath = f"{folder_path}/DatosSecuenciales.dat"
            
            # Llamamos al método generate_file para generar el archivo
            self.generate_file(folder_path)

    def generate_file(self, folder_path):
        global dataSecuencialFilePath
        dataSecuencialFilePath = f"{folder_path}/datosSecuencialesPython.dat"

        if os.path.exists(dataSecuencialFilePath):
            return

        with open(dataSecuencialFilePath, "w"):
            pass

    def add_data(self):
        global dataSecuencialFilePath

        if not dataSecuencialFilePath:
            return

        Id = self.id_textbox.get()
        Name = self.nombre_textbox.get()
        Note = self.nota_textbox.get()

        if Id and Name and Note:
            # Llamamos al método AddInformationSecuencial
            self.add_information_secuencial(Id, Name, Note)

            # Limpiamos los TextBox después de agregar datos
            self.id_textbox.delete(0, tk.END)
            self.nombre_textbox.delete(0, tk.END)
            self.nota_textbox.delete(0, tk.END)

            # Llamamos al método UpdateList
            self.update_list()
            
    def add_information_secuencial(self, Id, Name, Note):
        global dataSecuencialFilePath

        with open(dataSecuencialFilePath, "a") as file:
            file.write(f"{Id},{Name},{Note}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = SecuencialesApp(root)
    root.mainloop()
