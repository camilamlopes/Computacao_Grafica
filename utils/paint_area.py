# Módulo de informações básicas sobre primitivas geométricas e operações de desenho.
"""Definições e operações básicas para formas geométricas, incluindo:
    - Ponto
    - Linha
    - Circunferência
    - Polígono (janela de recorte)

    obs.: Drawing é a classe base para desenhar cada pixel no canvas.
"""
from customtkinter import CTkFrame, CTkCanvas

# Desenhar no canvas
class Drawing:
    def __init__(self):
        pass

    def draw(self, x, y, color="#000000"):
        """Pinta o pixel lógico (x,y) com a cor dada."""
        if 0 <= x < self.buffer_w and 0 <= y < self.buffer_h:
            rect_id = self.pixel_ids[x][y]
            self.canvas.itemconfig(rect_id, fill=color)
    
    """Limpa todo o canvas com a cor dada."""
    def clear(self, color="white"):
        for x in range(self.buffer_w):
            for y in range(self.buffer_h):
                self.draw(x, y, color)
# Ponto
class Point(Drawing):
    ##
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color


    def __str__(self):
        return f"Desenhando ponto nas coordenadas ({self.x}, {self.y}) com a cor {self.color}"

# Linha
class Line(Drawing):
    ##
    def __init__(self, point1, point2, color):
        self.point1 = point1
        self.point2 = point2
        self.color = color

    def __str__(self):
        return f"Desenhando linha de ({self.point1.x}, {self.point1.y}) até ({self.point2.x}, {self.point2.y}) com a cor {self.color}"
    
# Circunferência
class Circle(Drawing):
    ##
    def __init__(self, center, radius, color):
        self.center = center
        self.radius = radius
        self.color = color

    def __str__(self):
        return f"Desenhando circunferência com centro em ({self.center.x}, {self.center.y}), raio {self.radius} e cor {self.color}"

# Polígono (janela de recorte)
class Polygon(Drawing):
    ##
    def __init__(self, lines, color):
        self.lines = lines
        self.color = color

    def __str__(self):
        linhas_str = ", ".join([f"({l.point1.x}, {l.point1.y}) até ({l.point2.x}, {l.point2.y})" for l in self.lines])
        return f"Desenhando polígono com arestas em {linhas_str} e cor {self.color}"

# ================= Área de pintura =================
## Área de pintura com buffer lógico de pixels
class PaintArea(Drawing):
    def __init__(self, parent, width, height, pixel_size=5, bg="white"):
        super().__init__()

        self.frame = CTkFrame(parent, corner_radius=20)
        self.frame.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)

        # Canvas que vai exibir os pixels
        self.canvas = CTkCanvas(self.frame, bg=bg, highlightthickness=0,
                                width=width, height=height)
        self.canvas.pack(expand=True, fill="both")

        # Buffer lógico de pixels
        self.buffer_w = width // pixel_size
        self.buffer_h = height // pixel_size
        self.pixel_size = pixel_size
        self.pixel_ids = [[None for _ in range(self.buffer_h)] for _ in range(self.buffer_w)]

        # Criar os quadradinhos que representam os pixels
        for x in range(self.buffer_w):
            for y in range(self.buffer_h):
                x1 = x * pixel_size
                y1 = y * pixel_size
                x2 = x1 + pixel_size
                y2 = y1 + pixel_size
                rect_id = self.canvas.create_rectangle(x1, y1, x2, y2, fill=bg, outline=bg)
                self.pixel_ids[x][y] = rect_id

## Desenha a grade no canvas 
    def draw_grid(self, cell_size=20):  
        width = int(self.canvas["width"])
        height = int(self.canvas["height"])

        # Linhas verticais
        for x in range(0, width, cell_size):
            self.canvas.create_line(x, 0, x, height, fill="lightgray")

        # Linhas horizontais
        for y in range(0, height, cell_size):
            self.canvas.create_line(0, y, width, y, fill="lightgray")