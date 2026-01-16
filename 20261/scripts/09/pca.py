"""
Module to generate figures for Class_09 (illustration of PCA).

Author: Máximo Flores Valenzuela <https://github.com/maxfloresv>
"""

import os
import sys
import numpy as np
from sklearn.decomposition import PCA

from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import plotly_defaults
import plotly.graph_objects as go

os.makedirs("out/", exist_ok=True)

np.random.seed(42)
n_students = 30

# Random Math scores between 100 and 1000 (PAES range)
math_scores = np.random.uniform(800, 1000, n_students)
# Physics scores strongly correlated with Math + some random noise
physics_scores = math_scores * 0.95 + 50 + np.random.normal(0, 15, n_students)

X = np.column_stack((math_scores, physics_scores))

pca = PCA(n_components=1)
X_pca = pca.fit_transform(X)
X_reconstructed = pca.inverse_transform(X_pca)

fig = go.Figure()

x_lines = []
y_lines = []
for i in range(n_students):
  x_lines.extend([X[i, 0], X_reconstructed[i, 0], None])
  y_lines.extend([X[i, 1], X_reconstructed[i, 1], None])

fig.add_trace(go.Scatter(
  x=x_lines,
  y=y_lines,
  mode='lines',
  name='Pérdida de información',
  line=dict(color='gray', width=1, dash='dash'),
  hoverinfo='skip'
))

x_min, x_max = X_reconstructed[:, 0].min(), X_reconstructed[:, 0].max()
y_min, y_max = X_reconstructed[:, 1].min(), X_reconstructed[:, 1].max()

extension_factor = 10
slope = (y_max - y_min) / (x_max - x_min)
x_start = x_min - extension_factor
y_start = y_min - slope * extension_factor
x_end = x_max + extension_factor
y_end = y_max + slope * extension_factor

fig.add_trace(go.Scatter(
  x=[x_start, x_end],
  y=[y_start, y_end],
  mode='lines',
  name='Componente principal',
  line=dict(color='black', width=3)
))

fig.add_trace(go.Scatter(
  x=X[:, 0],
  y=X[:, 1],
  mode='markers',
  name='Datos originales',
  marker=dict(size=10, color='blue', opacity=0.6)
))

fig.add_trace(go.Scatter(
  x=X_reconstructed[:, 0],
  y=X_reconstructed[:, 1],
  mode='markers',
  name='Datos proyectados',
  marker=dict(size=10, color='red', symbol='x')
))

fig.update_layout(
  title=f"Visualizando PCA en una transición 2D → 1D <br><sup>Varianza explicada: {pca.explained_variance_ratio_[0]:.1%}</sup>",
  xaxis_title="Puntaje de Matemáticas",
  yaxis_title="Puntaje de Física",
  width=800,
  height=800,
  yaxis=dict(scaleanchor="x", scaleratio=1),
  legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01, borderwidth=1)
)

fig.write_image('out/pca.pdf', width=800, height=800)