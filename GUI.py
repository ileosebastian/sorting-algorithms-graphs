from tkinter import *
from tkinter import ttk

import random # Para evitar ingresar datos de forma manual
import threading # Para los hilos de ejecucion

import logging

from insertionSort import insertion_sort
from mergeSort import merge_sort

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] (%(threadname)-s) %(message)s')

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Simulador de algoritmos de ordenamiento")
        master.geometry('1000x600')
        master.resizable(width=0, height=0)
        master.config(bg='lightgrey', bd=25)

        # Variables a usar
        self.selected_algorithm = StringVar()
        self.data = []

    

    def deployPrincipal(self):

        self.UI_frame_principal = Frame(self.master, width=600, bg='white')
        self.UI_frame_principal.place(in_=self.master, anchor="c", relx=.50, rely=.50)
        title_1 = Label(self.UI_frame_principal, text="Simulador de algoritmos de ordenamiento", bg='white', fg='blue', font=('Helvetica', 24), justify=CENTER)
        title_1.grid(row=0, column=0, padx=5, sticky=W)

        title_2 = Label(self.UI_frame_principal, text="Por inserción y por mezcla", bg='white', fg='blue', font=('Helvetica', 18), justify=CENTER)
        title_2.grid(row=1, column=0, padx=5, sticky=W)

        title_2 = Label(self.UI_frame_principal, text="Escoja el tipo de comparativa:", bg='white', fg='black', font=('Helvetica', 14), justify=CENTER)
        title_2.grid(row=2, column=0, padx=5, sticky=W)

        Button(self.UI_frame_principal, text="Gráfica", command=self.deployGraphMenu, bg='lightblue').grid(row=3, column=0, padx=5, pady=5)

        # Button(self.UI_frame_principal, text="Desempeño", command=self.deployPerformanceMenu, bg='red').grid(row=4, column=0, padx=5, pady=5)

    def switch_frameGRAPH(self, frame_menu, ghost_menu):
        frame_menu.destroy()
        ghost_menu.destroy()
        self.deployPrincipal()

    def deployGraphMenu(self):
        self.UI_frame_principal.destroy()
        self.master.update()
        # Frames, labels, inputs, etc.
        self.UI_frame_menu = Frame(self.master, width=830, height=200, bg='grey') # Inicializar el frame
        self.UI_frame_menu.grid(row=0, column=0, padx=5, pady=5)
        
        self.ghost_frame = Frame(self.master, width=900, height=200, bg='lightgrey')
        self.ghost_frame.grid(row=1, column=0, padx=5, pady=5)
        # En el canvas se van a mostrar los algoritmos
        self.canvas_insertion = Canvas(self.ghost_frame, width=450, height=340, bg='white') 
        self.canvas_insertion.grid(row=1, column=0, padx=2, pady=5)

        self.canvas_merge = Canvas(self.ghost_frame, width=450, height=340, bg='white') 
        self.canvas_merge.grid(row=1, column=1, padx=4, pady=5)

    # Interactuar con la GUI
        # Fila 1 del menu:
        # Mensaje:
        Label(self.UI_frame_menu, text="Ingrese parámetros para generar una lista gráfica aleatoria: ", bg='grey', fg='white').grid(row=0, column=0, padx=5, sticky=W)
        # Opciones de algoritmo 
                    # PARA ESCOJER EL ALGORITMO
                    # self.algMenu = ttk.Combobox(self.UI_frame_menu, textvariable=self.selected_algorithm, values=['Algoritmo de Inserción', 'Algoritmo por Mezcla'])
                    # self.algMenu.grid(row=0, column=1, padx=5, pady=5)
                    # self.algMenu.current(0)

        # Fila 2 del menu:
        # Label(UI_frame_menu, text="Tamaño: ", bg='grey', fg='white').grid(row=1, column=0, padx=5, sticky=W)
        self.sizeEntry = Scale(self.UI_frame_menu, from_=3, to=18, resolution=1, orient=HORIZONTAL, label="Tamaño:")
        self.sizeEntry.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        # Label(UI_frame_menu, text="Mínimo valor: ", bg='grey', fg='white').grid(row=1, column=2, padx=5, sticky=W)
        self.minEntry = Scale(self.UI_frame_menu, from_=0, to=10, resolution=1, orient=HORIZONTAL, label="Valor mínimo:")
        self.minEntry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        # Label(UI_frame_menu, text="Máximo valor: ", bg='grey', fg='white').grid(row=1, column=4, padx=5, sticky=W)
        self.maxEntry = Scale(self.UI_frame_menu, from_=11, to=100, resolution=1, orient=HORIZONTAL, label="Valor máximo:") 
        self.maxEntry.grid(row=1, column=2, padx=5, pady=5, sticky=W)

        self.graph_button = Button(self.UI_frame_menu, text="Graficar", command=self.Generate, bg='blue', fg='white', width=10)
        self.graph_button.grid(row=1, column=3, padx=5, sticky=W)

        # Fila 3 del menu
        self.speedScale = Scale(self.UI_frame_menu, from_=0.1, to=2.0, length=200, digits=2, resolution=0.2, orient=HORIZONTAL, label="Velocidad")
        self.speedScale.grid(row=2, column=0, padx=5, pady=5)

        self.sort_button = Button(self.UI_frame_menu, text="Ordenar", command=self.StartAlgorithm, bg='lightgrey', fg='black', width=10)
        self.sort_button.grid(row=2, column=1, padx=5, pady=5)
        self.sort_button.focus_displayof()

        self.return_button = Button(self.UI_frame_menu, text="Volver al menú", command= lambda: self.switch_frameGRAPH(self.UI_frame_menu, self.ghost_frame), bg='lightblue', fg='black', width=15)
        self.return_button.grid(row=2, column=2, padx=5, sticky=W)


    def Generate(self):

        # Generar lista randomica a partir de los inputs
        size = int(self.sizeEntry.get())
        minValue = int(self.minEntry.get())
        maxValue = int(self.maxEntry.get())
        
        self.data = []
        for _ in range(size):
            self.data.append(random.randrange(minValue, maxValue+1))

        self.drawData_insertion(self.data, ['red' for x in range(len(self.data))]) # datap['red1', 'red2', ..., 'redN' ]
        self.drawData_merge(self.data, ['red' for x in range(len(self.data))])
        self.sort_button.config(bg='green', fg='white')
        self.sort_button.focus()

    # Dibujara en pantalla cada dato, en forma de barra, de la lista a ordenar
    def drawData_insertion(self, data, colorArray):
        self.canvas_insertion.delete("all")
        c_width = 600
        c_height = 340
        x_width = c_width / (len(data) + 7) 
        offset = 10
        spacing = 8
        normalizedData = [i / max(data) for i in data]

        for i, height in enumerate(normalizedData):
            # coordenadas izquierda
            x0 = i * x_width + offset + spacing
            y0 = c_height - height * 300
            # coordenadas derecha
            x1 = (i + 1) * x_width + offset
            y1 = c_height

            self.canvas_insertion.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
            self.canvas_insertion.create_text(x0+2, y0, anchor=SW, text=str(data[i]))
        
        self.master.update_idletasks()

    def drawData_merge(self, data, colorArray):
        self.canvas_merge.delete("all")
        c_width = 600
        c_height = 340
        x_width = c_width / (len(data) + 7) 
        offset = 10
        spacing = 8
        normalizedData = [i / max(data) for i in data]

        for i, height in enumerate(normalizedData):
            # coordenadas izquierda
            x0 = i * x_width + offset + spacing
            y0 = c_height - height * 300
            # coordenadas derecha
            x1 = (i + 1) * x_width + offset
            y1 = c_height

            self.canvas_merge.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
            self.canvas_merge.create_text(x0+2, y0, anchor=SW, text=str(data[i]))
        
        self.master.update_idletasks()

    # Aqui se ejecuta el algoritmo deseado
    def StartAlgorithm(self):
        
        # Para evitar que se usen Inputs mientras se ejecuta graficamente el algoritmo para interactuar con la interfaz
        self.UI_frame_menu.focus_displayof()
        warning_message = Label(self.UI_frame_menu, text="Por favor, espere a que los algoritmos finalicen ", bg='grey', fg='red')
        warning_message.grid(row=3, column=0, sticky=N+S)
        self.master.update()
        
        # From Insertion Sort
        data_for_insertion = self.data
        # insertion_sort(data_for_insertion, self.drawData_insertion, self.speedScale.get())
        hilo_1 = threading.Thread(name='Hilo_1', target=insertion_sort, args=(data_for_insertion, self.drawData_insertion, self.speedScale.get(), ))

        # self.drawData_insertion(data_for_insertion, ['green' for x in range(len(data_for_insertion))]) 

        # From Merge Sort
        data_for_merge = self.data
        # merge_sort(data_for_merge, self.drawData_merge, self.speedScale.get())
        hilo_2 = threading.Thread(name='Hilo_2', target=merge_sort, args=(data_for_merge, self.drawData_merge, self.speedScale.get(), ))

        # self.drawData_merge(data_for_merge, ['green' for x in range(len(data_for_merge))]) 

        hilo_1.start()
        hilo_2.start()

        self.drawData_insertion(data_for_insertion, ['green' for x in range(len(data_for_insertion))]) 
        self.drawData_merge(data_for_merge, ['green' for x in range(len(data_for_merge))]) 

        warning_message.destroy()
        self.sort_button.focus_displayof()
        self.UI_frame_menu.focus()
        self.sort_button.config(bg='lightgrey', fg='black')
        

    # def deployPerformanceMenu(self):
    #     pass

if __name__ == "__main__":
    root = Tk()
    simulador = GUI(root)
    simulador.deployPrincipal()
    root.mainloop()
