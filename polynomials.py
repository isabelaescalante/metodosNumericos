from __future__ import print_function

import numpy as np

def newton_divided_difference(x_array, y_array) :
    """
    Find the coefficients of Newton's divided difference and the Newton's polynomial
    Inputs:
            x: Array containing x values
            y: Array containing y values
    Outpus:
            f: Array containing Newton's divided difference coefficients
    """
    x = np.array(x_array)
    y = np.array(y_array)

    n = x.size
    q = np.zeros((n, n - 1))
    q = np.concatenate((y[:, None], q), axis=1)  # Insert 'y' in the first column of the matrix 'q'

    for i in range(1, n):
        for j in range(1, i + 1):
            q[i, j] = (q[i, j - 1] - q[i - 1, j - 1]) / (x[i] - x[i - j])

    # Copy the diagonal values of the matrix q to the vector f
    f = np.zeros(n)
    for i in range(0, n):
        f[i] = q[i, i]
    
    return f

'''
    # Prints the polynomial
    print("The polynomial is:")
    print("p(x)=%+.4f" % f[0], end=' ')
    for i in range(1, n):
        print("%+.4f" % f[i], end=' ')
        for j in range(1, i + 1):
            print("(x%+.4f)" % (x[j] * -1), end=' ')
    print("")
'''
