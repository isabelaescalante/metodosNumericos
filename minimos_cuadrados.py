import numpy as np
import math
from scipy.optimize import curve_fit

def exponencial(x_array, y_array) :
    x = np.empty((int(len(x_array))))
    y = np.empty((int(len(y_array))))

    for i in x_array :
        x = np.append(x, [i])
    
    for j in y_array :
        y = np.append(y, [j])

    popt, pcov = curve_fit(lambda t,a,b: a*np.exp(b*t),  x,  y)

    result = popt.tolist()
    string_result = "a: " + str(result[0]) + ", b: " + str(result[1])
    return string_result

def polinomial(x_array, y_array, n) :
    x = np.empty((int(len(x_array))))
    y = np.empty((int(len(y_array))))

    for i in x_array :
        x = np.append(x, [i])
    
    for j in y_array :
        y = np.append(y, [j])

    result = np.polyfit(x,y,n)

    final = result.tolist()
    size = int(len(final))
    resultado = ""
    for i in range(0, size) :
        resultado += "a" + str(i) + "= " + str(final[i]) + " "

    return resultado
    
'''
if __name__ == '__main__':
    x = np.array([1.2, 2.5, 3.3, 6.7, 4.5])
    y = np.array([2.5, 2.2, 3.4, 12.8, 7.2])
    x1 = np.array([1, 2, 3, 4, 5])
    y1 = np.array([1.25, 2.4, 3.6, 4.75, 5])
    print(exponencial(x,y))
    print(polinomial(x1, y1, 4))
'''