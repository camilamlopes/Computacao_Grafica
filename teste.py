import matplotlib.pyplot as plt

# Coordenadas dos pontos
A = (0,0)
B = (32,0)   # cateto = 32
C = (0,24)   # cateto = 24

# Triângulo
x = [A[0], B[0], C[0], A[0]]
y = [A[1], B[1], C[1], A[1]]

plt.figure(figsize=(6,6))
plt.plot(x, y, 'bo-', linewidth=2)
plt.fill(x, y, alpha=0.2)

# Rótulos
plt.text(A[0]-1, A[1]-1, "A(0,0)", fontsize=10)
plt.text(B[0]+1, B[1], "B(32,0)", fontsize=10)
plt.text(C[0]-2, C[1], "C(0,24)", fontsize=10)

# Lados
plt.text(16, -1, "32 cm", ha="center")
plt.text(-2, 12, "24 cm", va="center", rotation=90)
plt.text(16, 14, "40 cm", ha="center", rotation=-37)

plt.axis("equal")
plt.grid(False)
plt.title("Triângulo Retângulo com Catetos 24 cm e 32 cm")
plt.show()
