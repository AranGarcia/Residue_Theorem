import curva_jordan
import math
import sympy

def cmplx_residuo(fz, singularidad, potencia):
    z = sympy.symbols('z')
    zn =  (z - sympy.sympify(singularidad) ) **potencia
    lambda_z = fz * zn
    derivada = sympy.diff(lambda_z, z, potencia - 1)
    r = derivada / math.factorial(potencia - 1)
    return r.subs(z, singularidad)
    

def int_res_cmplx(funcion, z, n, radio):
    z1, z2, z3 = sympy.symbols("z1 z2 z3")
    fz = sympy.sympify(funcion + "/ ( (z-z1)**" + str(n[0])
    +" * (z-z2)**" + str(n[1])
    +" * (z-z3)**" + str(n[2]) +")").subs({ z1 : z[0], z2 : z[1], z3 : z[2] })
    cumplen = []
    for i in range(3):
        if n[i] < 0:
            cumplen.append(0);
        else:
            cumplen.append(curva_jordan.pertenece_interior(z[i], radio))
    if 1 not in cumplen:
        if -1 not in cumplen:
            return None
        return 0

    suma_residuos = 0
    for i in range(3):
        if cumplen[i] == 1:
            resultado = cmplx_residuo(fz, z[i], n[i])
            suma_residuos += resultado
    return 2j * math.pi * suma_residuos