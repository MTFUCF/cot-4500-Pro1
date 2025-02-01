import numpy as np

def approximation_algorithm(x0=1.5, tol=1e-6):
    """
    Approximate the square root of 2 using an iterative numerical method.
    """
    iter_count = 0
    diff = x0
    x = x0
    
    print(f"{iter_count} : {x}")
    
    while diff >= tol:
        iter_count += 1
        y = x
        x = (x / 2) + (1 / x)
        print(f"{iter_count} : {x}")
        
        diff = abs(x - y)
    
    print(f"\nConvergence after {iter_count} iterations")
    return x

def bisection_method(f, left, right, tol=1e-6, max_iter=100):
    """
    Find root of function f in interval [left, right] using Bisection Method.
    """
    iter_count = 0
    
    while abs(right - left) > tol and iter_count < max_iter:
        iter_count += 1
        p = (left + right) / 2
        
        if (f(left) < 0 and f(p) > 0) or (f(left) > 0 and f(p) < 0):
            right = p
        else:
            left = p
    
    return p

def fixed_point_iteration(g, p0, tol=1e-6, max_iter=100):
    """
    Solve x = g(x) using Fixed-Point Iteration.
    """
    i = 1
    while i <= max_iter:
        p = g(p0)
        if abs(p - p0) < tol:
            print(f"SUCCESS: Converged to {p}")
            return p
        i += 1
        p0 = p
    print("FAILURE: Method did not converge")
    return None

def newton_raphson(f, df, p_prev, tol=1e-6, max_iter=100):
    """
    Find root of function f using Newton-Raphson Method.
    """
    i = 1
    while i <= max_iter:
        if df(p_prev) == 0:
            print("FAILURE: Derivative is zero, cannot proceed")
            return None
        
        p_next = p_prev - f(p_prev) / df(p_prev)
        if abs(p_next - p_prev) < tol:
            print(f"SUCCESS: Converged to {p_next}")
            return p_next
        
        i += 1
        p_prev = p_next
    
    print("FAILURE: Maximum iterations reached, method did not converge")
    return None

if __name__ == "__main__":
    approximation_algorithm()
    
    # Example use of bisection method
    f = lambda x: x**2 - 2  
    root = bisection_method(f, 0, 2)
    print(f"Bisection Method Root: {root}")
    
    # Example use of fixed-point iteration
    g = lambda x: (x + 2/x) / 2  
    fixed_point_iteration(g, 1)
    
    # Example use of Newton-Raphson method
    df = lambda x: 2*x  
    newton_raphson(f, df, 1)
