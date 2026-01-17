"""
Module to generate figures for Class_09 (illustration of t-SNE).

Author: Máximo Flores Valenzuela <https://github.com/maxfloresv>
"""

import os
import sys
from sklearn import datasets
from sklearn.manifold import TSNE

from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import plotly_defaults
import plotly.express as px

os.makedirs("out/", exist_ok=True)

digits = datasets.load_digits()
X = digits.data
y = digits.target

tsne = TSNE(n_components=2, perplexity=30, random_state=42, init='pca', learning_rate='auto')
X_embedded = tsne.fit_transform(X)

fig = px.scatter(
  x=X_embedded[:, 0],
  y=X_embedded[:, 1],
  color=y.astype(str),
  title="t-SNE en MNIST: de 64 dimensiones a 2",
  labels={'color': 'Dígito real'},
  width=600,
  height=600
)

fig.update_traces(marker=dict(size=6))
fig.write_image("out/t-sne.pdf", width=600, height=600)