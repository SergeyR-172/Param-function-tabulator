import numpy as np
from typing import Tuple

def function_compute(n: int, a: float, k1: float, k: float, kd: float) -> Tuple[np.ndarray, np.ndarray]:
    x1 = k1 * a
    dx = kd * a
    
    x_values = []
    y_values = []
    
    if x1 < k * a:
        y = np.arctan((1 + a * x1) / (a * a + x1 * x1))
    else:
        y = np.sqrt(a * a + x1 * x1) * np.exp(-a * x1)
        
    x_values.append(x1)
    y_values.append(y)
    
    for i in range(1, n):
        x1 = x1 + dx
        
        if x1 < k * a:
            y = np.arctan((1 + a * x1) / (a * a + x1 * x1))
        else:
            y = np.sqrt(a * a + x1 * x1) * np.exp(-a * x1)
            
        x_values.append(x1)
        y_values.append(y)
        
    return np.array(x_values), np.array(y_values)