# from matplotlib.figure import Figure
# from matplotlib import cm
# from matplotlib.backends.backend_agg import FigureCanvas 
import pandas as pd
from bokeh.palettes import Category20c, Category20
from bokeh.plotting import figure
from bokeh.transform import cumsum
from math import pi

# make pie chart showing portfolio asset distribution
def make_pie(data):
    data = data.copy()
    # data = data.reset_index().rename(columns={'index': 'stock'})
    data['angle'] = data['weight']/data['weight'].sum() * 2*pi
    data['color'] = Category20c[data.shape[0]]
    data['percent'] = data['weight'] * 100

    p = figure(plot_height=350, title="Portfolo Distribution", toolbar_location=None,
               tools="hover", tooltips="@category: @percent%", x_range=(-0.5, 1.0))

    r = p.wedge(x=0, y=1, radius=0.4,
            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
            line_color="white", fill_color='color', legend_field='category', source=data)

    p.axis.axis_label=None
    p.axis.visible=False
    p.grid.grid_line_color = None
    return p

def make_weight_chart(weight):
    w = weight.copy()
    w['Percent Allocation'] = w['weight'] * 100
    w = w.reset_index().drop(['weight', 'index'], axis=1).set_index('category')
    #w = w.drop(['weight', 'category'], axis=1)
    return w
