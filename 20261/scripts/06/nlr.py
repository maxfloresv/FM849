"""
Module to generate figures for Class_06 (non-linear regression).

Author: Máximo Flores Valenzuela <https://github.com/maxfloresv>
"""

import os
import sys
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import plotly_defaults
import plotly.graph_objects as go

os.makedirs("out/", exist_ok=True)

np.random.seed(42)
hours = np.linspace(0, 24, 50)

def logistic_model(t, L=1000, k=0.5, t0=12):
  """
  Defines a logistic function to simulate real-world saturation of likes.
  """
  return L / (1 + np.exp(-k * (t - t0)))

n_likes = logistic_model(hours) + np.random.normal(0, 25, len(hours))
n_likes = np.maximum(n_likes, 0)

X = hours.reshape(-1, 1)

# Linear regression model
linear_reg = LinearRegression().fit(X, n_likes)
linear_pred = linear_reg.predict(X)

def fit_polynomial_regression(X, y, degree):
  poly_features = PolynomialFeatures(degree=degree)
  X_poly = poly_features.fit_transform(X)
  poly_reg = LinearRegression().fit(X_poly, y)
  return X_poly, poly_reg

# Polynomial regression model (degree 2)
X_poly_2, poly_reg_2 = fit_polynomial_regression(X, n_likes, degree=2)
pred_poly_2 = poly_reg_2.predict(X_poly_2)

# Polynomial regression model (degree 3)
X_poly_3, poly_reg_3 = fit_polynomial_regression(X, n_likes, degree=3)
pred_poly_3 = poly_reg_3.predict(X_poly_3)

fig = go.Figure()

fig.add_trace(go.Scatter(
  x=hours, y=n_likes,
  mode='markers',
  name='Datos reales (<i>post</i> viral)',
  marker=dict(color='rgba(152, 0, 0, .8)', size=8)
))

fig.add_trace(go.Scatter(
  x=hours, y=linear_pred,
  mode='lines',
  name='Predicción lineal (simple)',
  line=dict(color='royalblue', width=4, dash='dash')
))

fig.add_trace(go.Scatter(
  x=hours, y=pred_poly_2,
  mode='lines',
  name='Predicción polinomial (grado 2)',
  line=dict(color='forestgreen', width=3),
  opacity=0.4
))

fig.add_trace(go.Scatter(
  x=hours, y=pred_poly_3,
  mode='lines',
  name='Predicción polinomial (grado 3)',
  line=dict(color='mediumpurple', width=3)
))

fig.update_layout(
  title='Transición de modelos: predicción de <i>likes</i> en redes sociales',
  xaxis_title='Horas desde la publicación',
  yaxis_title='Cantidad de <i>likes</i>',
  legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01, borderwidth=1),
  width=1000,
  hovermode='x unified'
)

fig.write_image('out/nlr.pdf', width=800)