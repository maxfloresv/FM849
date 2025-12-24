"""
Customizes Plotly's default template and provides utility functions for consistent styling.

Author: Máximo Flores Valenzuela <https://github.com/maxfloresv>
"""

import plotly.io as pio
import utils.constants as constants
from plotly.graph_objects import Figure

pio.templates["cmu"] = pio.templates["plotly_white"]
pio.templates["cmu"]["layout"]["font"]["family"] = "CMU Sans Serif"
pio.templates["cmu"]["layout"]["font"]["size"] = 20
pio.templates["cmu"]["layout"]["title"] = {
  "x": 0.5,
  "xanchor": "center"
}
pio.templates["cmu"]["layout"].update(
  xaxis=dict(
    showgrid=False,
    zeroline=False,
    showline=True,
    linewidth=1,
    linecolor="black",
    ticks="outside",
    ticklen=8
  ),
  yaxis=dict(
    showgrid=False,
    zeroline=False,
    showline=True,
    linewidth=1,
    linecolor="black",
    ticks="outside",
    ticklen=8
  )
)

pio.templates["cmu"].layout.font.color = "black"
pio.templates["cmu"].layout.xaxis.color = "black"
pio.templates["cmu"].layout.yaxis.color = "black"

pio.templates.default = "cmu"

def update_fig_props(fig: Figure) -> None:
  """
  Update default properties for Plotly figures.

  Parameters
  ----------
  fig : plotly.graph_objects.Figure
      The figure to update.
  """
  fig.update_traces(
    marker_color=constants.EDV_DARK_GREEN,
    textposition='outside'
  )