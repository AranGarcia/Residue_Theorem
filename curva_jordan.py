import math
import cmath

def distancia_cmplx(z1, z2):
    """
    distancia_cmplx(z1, z2) -> número real

    Devuelve un valor real que representa la distancia entre dos números complejos.
    """
    return math.sqrt( (z1.real - z2.real)**2 + (z1.imag - z2.imag)**2 )

def pertenece_interior(z, r, centro = 0):
    """
    pertenece_interior( centro(h,k), radio, coordenada_compleja) -> estado de coordenada compleja

    Verifica que un número complejo se encuentro dentro, sobre o fuera de una curva jordan
    con centro en (h,k) y de radio r.
    -Valor de retorno-
        -1 = El número complejo se encuentra fuera de la curva.
        0 = El número complejo se encuentra sobre la curva.
        1 = El número complejo se encuentra dentro de la curva.
    """
    d = distancia_cmplx(z, centro)
    print(d)
    if r < d:
        return -1
    if r > d:
        return 1
    
    return 0
