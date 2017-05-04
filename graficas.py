import matplotlib.pyplot as plt

def graficar_region(z, r, h = (0,0), titulo = None):

    # Preparación de la figura
    fig = plt.gcf()
    fig.canvas.set_window_title("Teorema de Integración de Cauchy")
    plt.xlabel("Reales")
    plt.ylabel("Imaginarios")
    if titulo:
        plt.title(titulo, fontsize = 22, y=1.08)

    # Grafica lista de complejos
    for z0 in z:
        plt.plot(z0.real, z0.imag, marker = "o")
    
    # Grafica gama de t
    circle = plt.Circle((0, 0), color = "r",radius = r, alpha = .5, label = "$\gamma$(t), [0,2$\pi$]")
    plt.gca().add_patch(circle)

    # Ajusta y termina detalles
    plt.axis('equal')
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()

