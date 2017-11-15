from __future__ import print_function

import numpy as np
import math

import integration
import interpolation
import linear_systems
import polynomials
import solutions
'''
simpson los dos
bisecciones
newton rapson
montante
ajuste a exponencial
a polinomial
lagrange

def debug(variable):
    print(variable, "=", eval(variable))


def print_running(message):
    print("Solucion: ", message)

'''
print_running("Trapezoidal Multiple")
x = np.array([2, 4, 5])
y = np.array([1, 3, 6])
debug("x")
debug("y")
[xi] = integration.trapezoidal_multiple(x, y)
debug("xi")

print("\n")

print_running("Trapezoidal Simple")
f = lambda x: x ** 2 * math.log(x ** 2 + 1)
a = 0.0
b = 2.0
h = 0.25
n = int((b - a) / h)
debug("a")
debug("b")
debug("n")
[xi] = integration.trapezoidal_simple(f, b, a, n)
debug("xi")

print("\n")

print_running("Simpson 1/3 Multiple")
x = np.array([0, 6, 12])
y = np.array([124, 134, 148])
debug("x")
debug("y")
[xi] = integration.simpson_multiple(x, y)
debug("xi")

print("\n")

print_running("Simpson 1/3 Simple")
f = lambda x: x ** 2 * math.log(x ** 2 + 1)
a = 0.0
b = 2.0
h = 0.25
n = int((b - a) / h)
debug("a")
debug("b")
debug("n")
[xi] = integration.simpson_simple(f, b, a, n)
debug("xi")

print("\n")

print_running("Secante")
f = lambda x: 4 * x ** 3 + x + math.cos(x) - 10
tol = 10 ** -5
iter_max = 100
a = 1.0
b = 2.0
debug("tol")
debug("iter_max")
debug("a")
debug("b")
[root, iter, converged] = solutions.secante(f, a, b, tol, iter_max)
debug("root")
debug("iter")
debug("converged")

print("\n")

print_running("Newton-Raphson")
f = lambda x: 4 * x ** 3 + x + math.cos(x) - 10
df = lambda x: 12 * x ** 2 + 1 - math.sin(x)
tol = 10 ** -5
iter_max = 100
x0 = 1.0
debug("tol")
debug("iter_max")
debug("x0")
[root, iter, converged] = solutions.newtonRapson(f, df, x0, tol, iter_max)
debug("root")
debug("iter")
debug("converged")

print("\n")

print_running("Biseccion")
f = lambda x: 4 * x ** 3 + x + math.cos(x) - 10
tol = 10 ** -5
iter_max = 100
a = 1.0
b = 2.0
debug("tol")
debug("iter_max")
debug("a")
debug("b")
[root, iter, converged] = solutions.biseccion(f, a, b, tol, iter_max)
debug("root")
debug("iter")
debug("converged")

print("\n")

print_running("Lagrange")
x = np.array([2, 11 / 4, 4])
y = np.array([1 / 2, 4 / 11, 1 / 4])
x_int = 3
debug("x")
debug("y")
debug("x_int")
[y_int] = interpolation.lagrange(x, y, x_int)
debug("y_int")

print("\n")

print_running("Eliminacion Gausseana")
a = np.array([[1, -1, 2, -1], [2, -2, 3, -3], [1, 1, 1, 0], [1, -1, 4, 3]])
b = np.array([-8, -20, -2, 4])
debug("a")
debug("b")
[a] = linear_systems.gauss_elimination(a, b)
debug("a")

print("\n")
'''
print_running("Newton (diferencias divididas)")
x = np.array([1.0, 1.3, 1.6, 1.9, 2.2])
y = np.array([0.7651977, 0.6200860, 0.4554022, 0.2818186, 0.1103623])
debug("x")
debug("y")
[f] = polynomials.newton_divided_difference(x, y)
debug("f")

print("\n")
'''
print_running("Linear Systems: Backward Substitution")
u = a[:, 0:-1]
d = a[:, -1]
debug("u")
debug("d")
[x] = linear_systems.backward_substitution(u, d)
debug("x")

print("\n")

print_running("Linear Systems: Forward Substitution")
l = np.array([[3, 0, 0, 0], [-1, 1, 0, 0], [3, -2, -1, 0], [1, -2, 6, 2]])
c = np.array([5, 6, 4, 2])
debug("l")
debug("c")
[x] = linear_systems.forward_substitution(l, c)
debug("x")
'''
