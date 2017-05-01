#!/usr/bin/python3

import curva_jordan
import sys

print("Teorema del Residuo\n")

print("\u222e( f(z)dz / [ (z - z1)^n1 (z - z2)^n2 (z - z3)^n3 ] \nen "
     "una curva Jordan cerrada \u03b3(t) de radio r\n")

# Validación de entradas
funciones = {1 : "sen(z)", 2 : "cos(z)", 3 : "e^z",
    4 : "z^x", 5 : "senh(z)", 6 : "cosh(z)"}
z = []
n = []
try:
    radio = float(input("Radio = "))
    z.append( complex(input("z1 = ")) )
    z.append( complex(input("z2 = ")) )
    z.append( complex(input("z3 = ")) )

    # Entrada de funcion
    print("\nElige una f(z):")
    for f in funciones:
        print(f ,".-",funciones[f])
    num_fun = int(input("f(z) = "))
    if num_fun not in funciones:
        raise ValueError("Opcion invalida (" + str(num_fun) + ")")

    # Entrada de exponente n
    n.append( int( input("\nDefina exponente 'n1' de (z - z1) = ") ) )
    n.append( int( input("Defina exponente 'n2' de (z - z2) = ") ) )
    n.append( int( input("Defina exponente 'n3' de (z - z3) = ") ) )

    # Si se eligió z ^ n ...
    if num_fun == 4:
        indice = int(input("Defina el exponente 'x' = "))

except ValueError as err:
    print("Error: Entrada inválida (" + str(err) + ").")
    sys.exit(1)
except EOFError:
    print("\n\nEjecución terminada.")
    sys.exit(0)
# Fin validación entradas

cumplen = [ curva_jordan.pertenece_interior(z[i], radio) for i in range(3) ]