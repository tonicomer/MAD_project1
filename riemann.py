import numpy as np
def left_endpoint(x_vals:np.ndarray,func:np.ufunc):
    return np.sum(func(x_vals[:-1])*(x_vals[1:]-x_vals[:-1]))
def trapezoid(x_vals: np.ndarray, func:np.ufunc)->float:
    answer = np.sum((func(x_vals[:-1]) + func(x_vals[1:]))/2 * (x_vals[1:]-x_vals[:-1]))
    return answer
