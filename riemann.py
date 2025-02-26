import numpy as np
def left_endpoint(x_vals:np.ndarray,func:np.ufunc): ## The left_endpoint function is approximating f(a) * (b-a).
    return np.sum(func(x_vals[:-1])*(x_vals[1:]-x_vals[:-1])) ## Evaluates the function at the left endpoints.
## The left endpoints are all the input x_vals except for the last one, hence the indexing. 
## The function is evaluated at the left endpoints, then multiplied with each sub-interval. 
## The sub-intervals are calculated by subtracting the left endpoints by the right endpoints (all x_vals except the first)

def trapezoid(x_vals: np.ndarray, func:np.ufunc)->float: ## Approximating the trapezoid
    answer = np.sum((func(x_vals[:-1]) + func(x_vals[1:]))/2 * (x_vals[1:]-x_vals[:-1]))
    ## First the sum of the left and right endpoints are averaged. Then the sub-intervals are calculated. 
    ## We multiply this average (which is the height of the trapezoid) with the sub-interval width.
    return answer ## The function will sum all of these areas up to approximate the trapezoid.
    
def simpson(x_vals: np.ndarray, func: np.ufunc)->float: ## Employing Simpson's method
    h = x_vals[1] - x_vals[0] ## Computes the sub-interval width (b-a)
    answer = (h/6) * np.sum((func(x_vals[:-1]) + (4*func((x_vals[1:] + x_vals[:-1])/2) + func(x_vals[1:]))))
    ## h/6 is first part of Simpson's method (b-a/6)
    ## Uses Simpson's formula, which involves find the midpoints of each sub-interval and multiplying those by 4. 
    ## Also adds the left and right endpoint values, and sums this entire second half of the equation up
    return answer ## Outputs the answer using this formula
