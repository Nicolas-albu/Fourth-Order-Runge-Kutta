
import matplotlib.pyplot as plt
import numpy as np

def runge_kutta_fourth_order(derived_function: object, x0: float, t0: float, h: float, n: int) -> tuple:
  x: list = [x0]
  t: list = [t0]

  for i in range(1, n-1):
    t.append(t[i-1] + h) # t = t0 + 0.05 => t = 0.05
    K1: float = derived_function(t[i-1], x[i-1])
    K2: float = derived_function(t[i-1] + h/2, x[i-1] + (h/2) * K1)
    K3: float = derived_function(t[i-1] + h/2, x[i-1] + (h/2) * K2)
    K4: float = derived_function(t[i-1] + h, x[i-1] + h * K3)

    x.append(x[i-1] + (h/6) * (K1 + 2*K2 + 2*K3 + K4))
  
  return x, t
