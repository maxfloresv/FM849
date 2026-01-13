"""
Module to generate figures for Class_06 (gradient descent).

Author: Máximo Flores Valenzuela <https://github.com/maxfloresv>
"""

import os
import sys
import numpy as np

from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import plotly_defaults
import plotly.graph_objects as go

os.makedirs("out/", exist_ok=True)

def f(x): return x**2
def df(x): return 2*x

x_init = 4
lr = 0.3
iter = 5

hist_x = [x_init]
hist_y = [f(x_init)]

curr_x = x_init
for _ in range(iter):
  gradient = df(curr_x)
  curr_x = curr_x - lr * gradient
  hist_x.append(curr_x)
  hist_y.append(f(curr_x))

x_curve = np.linspace(-5, 5, 100)
y_curve = f(x_curve)

fig = go.Figure()

fig.add_trace(go.Scatter(x=x_curve, y=y_curve, name='Función', line=dict(color='blue')))

fig.add_trace(go.Scatter(
    x=hist_x, y=hist_y,
    mode='markers+lines+text',
    name='Pasos del gradiente',
    textposition="top center",
    marker=dict(size=12, color='red', symbol='x')
))

fig.update_layout(
  title="Simulación de gradiente descendente (5 iteraciones)",
  xaxis_title=r"Valor de x",
  yaxis_title="Error (costo)",
  width=900,
  height=600
)

fig.write_image("out/gd.pdf", width=700, height=600)