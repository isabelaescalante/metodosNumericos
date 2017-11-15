import numpy as np
import math
from scipy.optimize import curve_fit

def exponencial(x_array, y_array) :
    x = x_array
    y = y_array

    popt, pcov = curve_fit(lambda t,a,b: a*np.exp(b*t),  x,  y)

    result = popt.tolist()
    string_result = "a: " + str(result[0]) + ", b: " + str(result[1])
    return string_result

def polinomial(x_array, y_array, n) :
    x = np.array(x_array)
    y = np.array(y_array)
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
    #x = np.array([1, 2, 3, 4, 5])
    #y = np.array([1.25, 2.4, 3.6, 4.75, 5])
    print(exponencial(x,y))

'''