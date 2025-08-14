from customtkinter import *
from PIL import Image, ImageTk



class App(CTk):
    def __init__(self):
        super().__init__()

        ## Title Bar
        self.title("TP 01 - Paint")
        self.BASE_DIR = os.path.dirname(__file__)
        icon_path = os.path.join(self.BASE_DIR, "images", "icon.ico")
        self.iconbitmap(icon_path)

        # Setup window
        self.window()

    def window(self):
        self.configure(fg_color="green")

        window_width = 800
        window_height = 600
        display_width = self.winfo_screenwidth()
        display_height = self.winfo_screenheight()

        left = int(display_width / 2 - window_width / 2)
        top = int(display_height / 2 - window_height / 2)

        self.geometry(f'{window_width}x{window_height}+{left}+{top}')

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)

        self.head_config()
        self.draw_config()
        
    def on_click(self):
        print("Botao clicado!")

    def head_config(self):
        head_color = 'red'
        self.head_frame = CTkFrame(self, corner_radius=0, fg_color=head_color)
        self.head_frame.grid(row=0, column=0, sticky="ew", padx=0, pady=0)
        ##self.head_frame.columnconfigure(0, weight=0)
        self.head_frame.configure(height=80)

        pencil_image = CTkImage(
            light_image=Image.open(os.path.join(self.BASE_DIR, "images", "002-pencil.png")),
            dark_image=Image.open(os.path.join(self.BASE_DIR, "images", "002-pencil.png")),
            size=(40, 40)
        )

        self.btn_pencil = CTkButton( self.head_frame, image=pencil_image, text="",
                                     fg_color=head_color, hover_color=head_color, width=40, height=40, cursor='hand2',
                                     command=self.on_click()
        )
        self.btn_pencil.grid(row=0, column=0, padx=10, pady=10)

        self.btn_color = CTkButton(self.head_frame, text='', corner_radius=100, width=40, height=40, cursor='hand2')
        self.btn_color.grid(row=0, column=1, padx=10, pady=10)

        self.scale_size = CTkSlider(self.head_frame, from_=1, to=100)
        self.scale_size.grid(row=0, column=2, padx=10, pady=10)

    def draw_config(self):
        self.draw_frame = CTkFrame(self, corner_radius=0, fg_color="blue")
        self.draw_frame.grid(row=1, column=0, sticky="nsew", padx=0, pady=0)
        self.draw_frame.columnconfigure(0, weight=1)
        self.draw_frame.rowconfigure(0, weight=1)

        self.draw_area = CTkFrame(self.draw_frame, fg_color="white")
        self.draw_area.grid(row=0, column=0, padx=70, pady=70, sticky="nsew")
        

app = App()
app.mainloop()