import numpy as np
import pandas as pd
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file

stock=input("Choose the dataset: tcs or infy \n")
stockdata=pd.read_csv(stock+'.csv')
def datetime(x):
    return np.array(x, dtype=np.datetime64)

p1 = figure(x_axis_type="datetime", title="Stock Closing Price")
p1.grid.grid_line_alpha=0.3
p1.xaxis.axis_label = 'Date'
p1.yaxis.axis_label = 'Closing Price'

p1.line(datetime(stockdata['Date']), stockdata['Close'], color='#A6CEE3', legend=stockdata)

p1.legend.location = "top_left"


show(p1)
