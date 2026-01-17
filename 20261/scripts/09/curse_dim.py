"""
Module to generate figures for Class_09 (illustration of the curse of dimensionality).

Author: Máximo Flores Valenzuela <https://github.com/maxfloresv>
"""

import os
import sys
import numpy as np

from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import plotly_defaults
import plotly.graph_objects as go
from plotly.subplots import make_subplots

os.makedirs("out/", exist_ok=True)

np.random.seed(42)
num_points = 100
center_val = 0.5

x_coords = np.random.rand(num_points)
y_coords = np.random.rand(num_points)
z_coords = np.random.rand(num_points)

dist_2d = np.sqrt((x_coords - center_val)**2 + (y_coords - center_val)**2)
closest_idx_2d = np.argmin(dist_2d)

dist_3d = np.sqrt((x_coords - center_val)**2 + (y_coords - center_val)**2 + (z_coords - center_val)**2)
closest_idx_3d = np.argmin(dist_3d)

fig = make_subplots(
  rows=1, 
  cols=2,
  specs=[[{'type': 'xy'}, {'type': 'scene'}]],
  subplot_titles=(
    f'2D: La "pista de baile" (d<sub>mín</sub> = {dist_2d[closest_idx_2d]:.3f})', 
    f'3D: El "rascacielos" (d<sub>mín</sub> = {dist_3d[closest_idx_3d]:.3f})'
  ),
  horizontal_spacing=1e-5
)

# 2D Data Plot
fig.add_trace(
  go.Scatter(
    x=x_coords, 
    y=y_coords, 
    mode='markers', 
    name='Data', 
    marker=dict(color='darkblue', opacity=1.0)
  ), 
  row=1, 
  col=1
)

fig.add_trace(
  go.Scatter(
    x=[center_val], 
    y=[center_val], 
    mode='markers', 
    name='Center',
    marker=dict(color='red', size=12, symbol='diamond')
  ), 
  row=1, 
  col=1
)

fig.add_trace(
  go.Scatter(
    x=[x_coords[closest_idx_2d]], 
    y=[y_coords[closest_idx_2d]], 
    mode='markers', 
    name='Nearest Neighbor',
    marker=dict(color='green', size=10)
  ), 
  row=1, 
  col=1
)

# 3D Data Plot
fig.add_trace(
  go.Scatter3d(
    x=x_coords, 
    y=y_coords, 
    z=z_coords, 
    mode='markers', 
    name='Data',
    marker=dict(color='darkblue', size=4, opacity=1.0)
  ), 
  row=1, 
  col=2
)

fig.add_trace(
  go.Scatter3d(
    x=[center_val], 
    y=[center_val], 
    z=[center_val], 
    mode='markers', 
    name='Center',
    marker=dict(color='red', size=8, symbol='diamond')
  ), 
  row=1, 
  col=2
)

fig.add_trace(
  go.Scatter3d(
    x=[x_coords[closest_idx_3d]], 
    y=[y_coords[closest_idx_3d]], 
    z=[z_coords[closest_idx_3d]], 
    mode='markers', 
    name='Nearest Neighbor',
    marker=dict(color='green', size=6)
  ), 
  row=1, 
  col=2
)

fig.update_layout(
  title_text="Ilustración de la maldición de la dimensionalidad",
  showlegend=False,
  width=1200,
  height=600
)

fig.update_annotations(font_size=22)

fig.update_scenes(
  xaxis=dict(
    showline=True, 
    linewidth=2, 
    linecolor='black', 
    gridcolor='lightgray',
    showticklabels=False,
  ),
  yaxis=dict(
    showline=True, 
    linewidth=2, 
    linecolor='black', 
    gridcolor='lightgray',
    showticklabels=False,
  ),
  zaxis=dict(
    showline=True, 
    linewidth=2, 
    linecolor='black', 
    gridcolor='lightgray',
    showticklabels=False,
  ),
  camera=dict(eye=dict(x=1.31, y=1.31, z=1.31))
)

fig.write_image("out/curse_dim.pdf", width=1200, height=600)