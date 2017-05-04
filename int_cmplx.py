#!/usr/bin/python3

import graficas
import sympy
import sys
import teorema_residuo

print("Teorema del Residuo\n")

print("\u222e( f(z)dz / [ (z - z1)^n1 (z - z2)^n2 (z - z3)^n3 ] \nen "
     "una curva Jordan cerrada \u03b3(t) de radio r\n")

# Validación de entradas
funciones = {1 : "sin(z)", 2 : "cos(z)", 3 : "e^z",
    4 : "z^x", 5 : "sinh(z)", 6 : "cosh(z)"}

zs = []
n = []
try:
    radio = float(input("Radio = "))
    zs.append( complex(input("z1 = ")) )
    zs.append( complex(input("z2 = ")) )
    zs.append( complex(input("z3 = ")) )

    # Entrada de funcion
    print("\nElige una f(z):")
    for f in funciones:
        print(f ,".-",funciones[f])
    num_fun = int(input("f(z) = "))

    # Si se eligió z ^ n ...
    if num_fun == 4:
        indice = int(input("Define el exponente 'x' = "))
        funciones[4] = funciones[4].replace('^x', '**' + str(indice))
        print(funciones[4])

    # Opcion Inválida
    if num_fun not in funciones:
        raise ValueError("Opcion invalida (" + str(num_fun) + ")")

    # Entrada de exponente n1, n2 y n2
    n.append( int( input("\nDefine exponente 'n1' de (z - z1) = ") ) )
    n.append( int( input("Define exponente 'n2' de (z - z2) = ") ) )
    n.append( int( input("Define exponente 'n3' de (z - z3) = ") ) )
except ValueError as err:
    print("Error: Entrada invalida (" + str(err) + ").")
    sys.exit(1)
except EOFError:
    print("\n\nFin de ejecucion.")
    sys.exit(0)
# Fin validación entradas

integral = teorema_residuo.int_res_cmplx(funciones[num_fun], zs, n, radio)

z, z1, z2, z3 = sympy.symbols('z z1 z2 z3')
tit = sympy.sympify(funciones[num_fun] + "/ ( (z-z1)**" + str(n[0])
    +" * (z-z2)**" + str(n[1])
    +" * (z-z3)**" + str(n[2]) +")").subs({ z1 : zs[0], z2 : zs[1], z3 : zs[2] })
ti = r'$\oint_\gamma' +  sympy.latex(tit) + ' = ' + str(integral) + r'$'
graficas.graficar_region(zs, radio, titulo=ti)