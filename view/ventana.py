import tkinter as tk
from tkinter import ttk

class Ventana_Principal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Análisis Léxico")
        self.navbar = tk.Frame(self, bg="#1BF1E1") #CONTENEDOR DE LOS BOTONES Y CMB
        self.cmb = ttk.Combobox(self.navbar, state="readonly",
                                     values=["Opciones", "Abrir", "Guardar", "Guardar Como", "Salir"])
        self.btnAnalizar = ttk.Button(self.navbar, text="Analizar")
        self.btnErrores = ttk.Button(self.navbar, text="Errores")
        self.btnReporte = ttk.Button(self.navbar, text="Reporte")
        self.txtContainer = tk.Frame(self)
        self.txtArea = tk.Text(self.txtContainer, width=700, height=350)
        self.line_numbers = tk.Label(self.txtContainer, width=4, anchor="n")
        self.geometry("1300x550")

        #Esta funcion me va a mostrar los componentes en la ventana
        self.mostrar_Componentes()
        #Activa la funcionalidad de la numeracion
        self.txtArea.bind("<KeyRelease>", self.actualizar_numeracion_lineas)
        self.actualizar_numeracion_lineas(None)


    def mostrar_Componentes(self):

        self.navbar.pack(fill = tk.X) # NAVBAR SIMULADO

        self.cmb.set("Opciones")
        self.cmb.pack(side = tk.LEFT, padx=5, pady=10)
        self.btnAnalizar.pack(side = tk.LEFT, padx=5, pady=10)
        self.btnErrores.pack(side=tk.LEFT, padx=5, pady=10)
        self.btnReporte.pack(side=tk.LEFT, padx=5, pady=10)

        self.txtContainer.pack(padx = 50, pady = 50)
        self.txtContainer.configure(highlightbackground="black", highlightthickness=2)
        self.line_numbers.pack(side="left", fill="y")
        self.txtArea.pack(fill=tk.BOTH, expand=True)

    def actualizar_numeracion_lineas(self, event):
        # Función para mostrar la numeración de líneas en tiempo real
        line_numbers_text = "\n".join(str(i) for i in range(1, self.get_numero_lineas() + 1))
        self.line_numbers.config(text=line_numbers_text)

    def get_numero_lineas(self):
        # Función para obtener el número de líneas en el Text widget
        return int(self.txtArea.index("end-1c").split(".")[0])