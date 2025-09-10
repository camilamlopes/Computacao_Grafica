from random import choice
from customtkinter import *
from PIL import Image, ImageTk

from utils import *

class App(CTk):
    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'
    BASE_DIR = os.path.dirname(__file__)

    def __init__(self):
        super().__init__()

        ## Title Bar
        self.title("TP 01 - Paint")
        
        icon_path = os.path.join(self.BASE_DIR, "images", "icon.ico")
        self.iconbitmap(icon_path)

        # Setup window
        self.setup_variables()
        self.window()

    def setup_variables(self):
        self.active_btn = None
        #self.line_width = self.choose_size_button.get()
        self.color = self.DEFAULT_COLOR

    def window(self):
        #self.configure(fg_color="green")

        window_width = 1080
        window_height = 600
        display_width = self.winfo_screenwidth()
        display_height = self.winfo_screenheight()

        left = int(display_width / 2 - window_width / 2)
        top = int(display_height / 2 - window_height / 2)

        self.geometry(f'{window_width}x{window_height}+{left}+{top}')

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.side_bar()
        self.main_content()

    # ========== MENU LATERAL ==========
    ## Escolha da ferramenta
    def btn_choice(self, choice):
        print("ferramenta escolhida:", choice)

        """ Atualiza a última alteração """
        self.last_change.configure(text=f"{choice}")

        """ Adiciona ao log """
        self.logs.configure(state="normal")
        self.logs.insert("end", f"{choice}\n")
        self.logs.configure(state="disabled")

    ## Ativa o botão selecionado
    def activate_button(self, btn):
        if self.active_btn is not None:
            self.active_btn.configure(fg_color="#393954")
        btn.configure(fg_color="#001B4B", hover_color="#02457A")
        self.active_btn = btn
        
    def side_bar(self):
        self.side_frame = CTkFrame(self, corner_radius=20, fg_color='#242442')
        self.side_frame.grid(row=0, column=0, sticky="nswe", padx=10, pady=(0,10))
        self.side_frame.grid_propagate(False)
        ##self.side_frame.columnconfigure(0, weight=0)
        self.side_frame.rowconfigure(7, weight=1)

        # Botões do menu
        ## Retas
        self.line_frame = CTkFrame(self.side_frame, fg_color="transparent")
        self.line_frame.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
        self.line_frame.grid_columnconfigure(0, weight=1)  # esquerda
        self.line_frame.grid_columnconfigure(1, weight=2)  # meio

        self.reta_label = CTkLabel(self.line_frame, text="Retas", font=("Arial", 14), anchor="w")
        self.reta_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.btn_line_dda = self.make_tool("DDA", 1, 0, self.line_frame, self.line_dda)
        self.btn_line_bresenham = self.make_tool("Bresenham", 2, 0,self.line_frame, self.line_bresenham)

        ## Circunferência
        self.circ_frame = CTkFrame(self.side_frame, fg_color="transparent")
        self.circ_frame.grid(row=2, column=0, padx=10, pady=5, sticky="ew")
        self.circ_frame.grid_columnconfigure(0, weight=1) # esquerda
        self.circ_frame.grid_columnconfigure(1, weight=2) # meio

        self.circ_label = CTkLabel(self.circ_frame, text="Circunferência", font=("Arial", 14), anchor="w")
        self.circ_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.btn_circ_bresenham = self.make_tool("Bresenham", 2, 0,self.circ_frame, self.circ_bresenham)

        ## Recorte
        self.cut_frame = CTkFrame(self.side_frame, fg_color="transparent")
        self.cut_frame.grid(row=3, column=0, padx=10, pady=5, sticky="ew")
        self.cut_frame.grid_columnconfigure(0, weight=1) # esquerda
        self.cut_frame.grid_columnconfigure(1, weight=2) # meio

        self.recorte_label = CTkLabel(self.cut_frame, text="Recorte", font=("Arial", 14), anchor="w")
        self.recorte_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.btn_cut_cs = self.make_tool("Cohen-Sutherland", 1, 0, self.cut_frame, self.cut_cs)
        self.btn_cut_lb = self.make_tool("Liang-Barsky", 2, 0, self.cut_frame, self.cut_lb)

    def make_tool(self, text, row, column, frame, function):
        btn = CTkButton(frame, text=text, command=function, fg_color="#393954", hover_color="#5F5F86")
        btn.grid(row=row, column=column, sticky="ew", padx=20, pady=5)

        return btn

    ## ------------- Funções dos botões -------------
    def line_dda(self):
        self.btn_choice("DDA")
        self.activate_button(self.btn_line_dda)

    def line_bresenham(self):
        self.btn_choice("Bresenham")
        self.activate_button(self.btn_line_bresenham)

    def circ_bresenham(self):
        self.btn_choice("Circunferencia - Bresenham")
        self.activate_button(self.btn_circ_bresenham)

    def cut_cs(self):
        self.btn_choice("Recorte - Cohen-Sutherland")
        self.activate_button(self.btn_cut_cs)

    def cut_lb(self):
        self.btn_choice("Recorte - Liang-Barsky")
        self.activate_button(self.btn_cut_lb)

    # ========== CONTEÚDO PRINCIPAL ==========

    def main_content(self):
        self.main_content = CTkFrame(self, corner_radius=20, fg_color='#242442')
        self.main_content.grid(row=0, column=1, sticky="nswe", padx=10, pady=(0,10))
        self.main_content.grid_rowconfigure(0, weight=1)
        self.main_content.grid_columnconfigure(0, weight=3)  # área de desenho
        self.main_content.grid_columnconfigure(1, weight=1)  # área de formatos

        # Centro área de pintura
        self.paint_area()

        # Direita - área de formas geométricas
        self.shapes_area()

    def paint_area(self):
        self.paint_frame = CTkFrame(self.main_content, corner_radius=20)
        self.paint_frame.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)

        self.canvas = CTkCanvas(self.paint_frame, bg="white", highlightthickness=0)
        self.canvas.pack(expand=True, fill="both", padx=0, pady=0)

    def shapes_area(self):
        self.shapes_frame = CTkFrame(self.main_content, corner_radius=20, fg_color='#242442')
        self.shapes_frame.grid(row=0, column=1, sticky="nswe", padx=10, pady=10)
        self.shapes_frame.grid_columnconfigure(0, weight=1)
        self.shapes_frame.grid_rowconfigure(0, weight=1)
        self.shapes_frame.grid_rowconfigure(1, weight=3)

        # Log
        self.log_area()

        # Ferramentas
        self.tools_area()

    def log_area(self):
        self.log_area = CTkFrame(self.shapes_frame, corner_radius=20, fg_color="#5F5F86")
        self.log_area.grid(row=0, column=0, sticky="nswe", pady=(0,5))
        self.log_area.grid_columnconfigure(0, weight=1)
        self.log_area.grid_rowconfigure(0, weight=1)
        self.log_area.grid_rowconfigure(1, weight=2)

        self.last_change_frame = CTkFrame(self.log_area, corner_radius=20, fg_color="#393954")
        self.last_change_frame.grid(row=0, column=0, sticky="nwe", padx=10, pady=10)
        self.last_change = CTkLabel(self.last_change_frame, text=" ", font=("Arial", 16))
        self.last_change.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.logs = CTkTextbox(self.log_area, corner_radius=20, fg_color="#242442",
                               font=("Arial", 14), 
                               border_width=0, 
                               state="disabled")
        self.logs.grid(row=1, column=0, padx=10, pady=(0,10), sticky="nswe")

    def tools_area(self):
        self.tool_area = CTkFrame(self.shapes_frame, corner_radius=20, fg_color="#242442")
        self.tool_area.grid(row=1, column=0, sticky="nswe", pady=(5,0), padx=5)
        self.tool_area.grid_columnconfigure(0, weight=1)
        self.tool_area.grid_rowconfigure(0, weight=1)
    
        self.tabview = CTkTabview(self.tool_area, corner_radius=20, 
                                  fg_color="#5F5F86", 
                                  segmented_button_fg_color="#242442",
                                  segmented_button_selected_color="#16162e",
                                  segmented_button_unselected_color="#393954")
        self.tabview.grid(row=0, column=0, padx=0, pady=0, sticky="nswe")

        # Tabs
        ## Canvas
        self.tabview.add("Canvas")

        ## Transformadas Geométricas
        self.tabview.add("Transformadas")

if __name__ == "__main__":
    app = App()
    app.mainloop()