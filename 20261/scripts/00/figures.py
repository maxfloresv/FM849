"""
Module to generate figures for Class_00.

Author: Máximo Flores Valenzuela <https://github.com/maxfloresv>
"""

import os
import sys
import pandas as pd

from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import plotly_defaults as pltd
import plotly.express as px

os.makedirs("out/", exist_ok=True)

# Controls the upper tolerance to avoid cutting labels above bars
FIGURE_UPPER_TOLERANCE = 0.1

sex = pd.DataFrame({
  'Categoría': ['Hombres', 'Mujeres'],
  'Cantidad': [25, 13]
})

em = pd.DataFrame({
  'Curso': ['1.° Medio', '2.° Medio', '3.° Medio', '4.° Medio'],
  'Cantidad': [17, 11, 10, 0]
})

# Sex distribution
fig = px.bar(
  sex,
  x='Categoría',
  y='Cantidad',
  text='Cantidad'
)

fig.update_layout(
  xaxis_title='Sexo biológico',
  yaxis_title='Frecuencia',
  yaxis_range=[0, (1 + FIGURE_UPPER_TOLERANCE) * sex['Cantidad'].max()],
  title='Distribución por sexo biológico'
)

pltd.update_fig_props(fig)
fig.write_image('out/sex_distribution.pdf')

# Education level distribution
fig = px.bar(
  em,
  x='Curso',
  y='Cantidad',
  text='Cantidad'
)

fig.update_layout(
  xaxis_title='Curso',
  yaxis_title='Frecuencia',
  yaxis_range=[0, (1 + FIGURE_UPPER_TOLERANCE) * em['Cantidad'].max()],
  title='Distribución por curso escolar'
)

pltd.update_fig_props(fig)
fig.write_image('out/course_distribution.pdf')