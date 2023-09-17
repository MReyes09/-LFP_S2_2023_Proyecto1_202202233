import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
from controller.analizador import Analizador

class Ventana_Principal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Análisis Léxico")
        self.file_path = None
        self.navbar = tk.Frame(self, bg="#1BF1E1") #CONTENEDOR DE LOS BOTONES Y CMB
        self.cmb = ttk.Combobox(self.navbar, state="readonly",
                                     values=["Opciones", "Abrir", "Guardar", "Guardar Como", "Salir"])
        self.btnAnalizar = ttk.Button(self.navbar, text="Analizar")
        self.btnErrores = ttk.Button(self.navbar, text="Errores")
        self.btnReporte = ttk.Button(self.navbar, text="Reporte")
        self.txtContainer = tk.Frame(self)
        self.txtArea = tk.Text(self.txtContainer, width=700, height=350)
        self.line_numbers = tk.Text(self.txtContainer, width=4, height=350, bg="#F0F0F0", state="disabled")
        self.geometry("1300x550")

        #Esta funcion me va a mostrar los componentes en la ventana
        self.mostrar_Componentes()

        #Activa la funcionalidad de la numeracion
        self.txtArea.bind("<KeyRelease>", self.actualizar_numeracion_lineas)
        self.txtArea.bind("<MouseWheel>", self.actualizar_numeracion_lineas_scroll)
        self.actualizar_numeracion_lineas(None)

        #Activar la funcionalidad del cmb
        self.cmb.bind("<<ComboboxSelected>>", self.accion_cmb)

        #Activar funcionalidad del analizador
        self.btnAnalizar.bind("<Button-1>", self.analizador_Lex)


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
        self.line_numbers.config(state="normal")  # Habilita la edición de la enumeración de líneas
        self.line_numbers.delete(1.0, tk.END)  # Borra el contenido actual de la enumeración de líneas
        self.line_numbers.insert(1.0, line_numbers_text)  # Inserta la nueva enumeración
        self.line_numbers.config(state="disabled")  # Deshabilita la edición de la enumeración de líneas

    def get_numero_lineas(self):

        # Función para obtener el número de líneas en el Text widget
        return int(self.txtArea.index("end-1c").split(".")[0])

    def accion_cmb(self, event):

        """
        Esta funcion controla los posibles resultados ya definidos en el cmb, el cual ejecutara una accion
        dependiendo de cual se escoja
        """

        selected_option = self.cmb.get() #Se obtiene el valor actual del cmb

        if selected_option == "Abrir":
            # Realizar acción correspondiente a "Abrir"
            self.file_path = filedialog.askopenfilename(filetypes=[("Archivos JSON", "*.json")])
            file_path = self.file_path

            if file_path:

                with open(file_path,'r') as file:
                    content = file.read() #Transforma el contenido del archivo en un Str

                self.txtArea.delete(1.0,tk.END)
                self.txtArea.insert(tk.END, content)
                self.actualizar_numeracion_lineas(None)

        elif selected_option == "Guardar":

            try:

                if self.file_path:

                    with open(self.file_path, 'w') as file:
                        content = self.txtArea.get(1.0, tk.END)
                        file.write(content)

                    messagebox.showinfo("Éxito", "El archivo se a guardado satisfactoriamente")

                else:

                    self.guardar_Como()

            except Exception as e:

                messagebox.showerror("Error", "Se produjo un error al intentar guardar el archivo")
                print(f"error: {e}")

        elif selected_option == "Guardar Como":

            self.guardar_Como()

        elif selected_option == "Salir":

            messagebox.showinfo("Salir de la app", "¡Hasta la próxima!")
            self.destroy()

    def actualizar_numeracion_lineas_scroll(self, event):
        # Función para actualizar la enumeración de líneas al hacer scroll
        self.line_numbers.yview_moveto(self.txtArea.yview()[0])

    def guardar_Como(self):

        try:
            file_path = filedialog.asksaveasfilename(filetypes=[("Archivos JSON", "*.json")], defaultextension=".json")

            if file_path:

                self.file_path = file_path  # Actualiza la file_path con la nueva ubicación
                with open(file_path, 'w') as file:
                    content = self.txtArea.get(1.0, tk.END)  # Obtener el contenido del txtArea
                    file.write(content)
                messagebox.showinfo("Éxito", "El archivo se a guardado satisfactoriamente en la ruta\n"
                                             f"{file_path}")

        except Exception as e:

            print(f"Error: {e}")
            messagebox.showerror("Error","Se produjo un error al intentar guardar el archivo")

    def analizador_Lex(self, event):

        if self.file_path:

            texto = self.txtArea.get(1.0, tk.END)  # Obtener el contenido del txtArea
            scanner = Analizador(texto)
            scanner.analizar()
            scanner.re_operar()

        else:
            messagebox.showerror("Error", "Abre un archivo JSON antes de analizar")
