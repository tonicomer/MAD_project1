import numpy as np
import riemann
def left_endpoint(x_vals:np.ndarray,func:np.ufunc):
    return np.sum(func(x_vals[:-1])*(x_vals[1:]-x_vals[:-1]))
def trapezoid(x_vals: np.ndarray, func:np.ufunc)->float:
    answer = np.sum((func(x_vals[:-1]) + func(x_vals[1:]))/2 * (x_vals[1:]-x_vals[:-1]))
    return answer
def simpson(x_vals: np.ndarray, func: np.ufunc)->float:
    h = x_vals[1] - x_vals[0]
    answer = (h/6) * np.sum((func(x_vals[:-1]) + (4*func((x_vals[1:] + x_vals[:-1])/2) + func(x_vals[1:]))))
    return answer
