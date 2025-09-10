# Módulo de informações básicas sobre primitivas geométricas e operações de desenho.
"""Definições e operações básicas para formas geométricas, incluindo:
    - Ponto
    - Linha
    - Circunferência
    - Polígono (janela de recorte)

    obs.: Drawing é a classe base para desenhar cada pixel no canvas.
"""

# Desenhar no canvas
class Drawing:
    def __init__(self):
        pass

    def draw(self):
        pass

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
