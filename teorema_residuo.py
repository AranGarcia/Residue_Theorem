import curva_jordan
import math
import sympy

def cmplx_residuo(fz, singularidad, potencia):
    z, z0, z1, z2 = sympy.symbols('z z1 z2 z3')
    zn =  (z - sympy.sympify(singularidad) ) **potencia
    lambda_z = fz * zn
    return sympy.diff(lambda_z, z, potencia - 1) / math.factorial(potencia - 1)
    

def int_res_cmplx(funcion, z, n, radio):

    fz = sympy.sympify(funcion + "/ ( (z-z1)**" + str(n[0])
    +" * (z-z2)**" + str(n[1])
    +" * (z-z3)**" + str(n[2]) +")")
    print(fz)
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
            residuo = cmplx_residuo(fz, 'z' + str(i + 1), n[i]).subs(z)
            print(residuo)