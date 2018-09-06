import numpy as np
import pandas as pd
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file

stock=input("Choose the dataset: tcs or infy \n")
stockdata=pd.read_csv(stock+'.csv')

def datetime(x):
    return np.array(x, dtype=np.datetime64)


p2 = figure(x_axis_type="datetime", title="Pricing shock without volume shock")
p2.grid.grid_line_alpha=0.3
p2.xaxis.axis_label = 'Date'
p2.yaxis.axis_label = 'Closing Price Shock Without Volume Shock'

p2.square(datetime(stockdata['Date']), stockdata['Close'], color='#A6CEE3', legend='TCS')

p2.legend.location = "top_left"
