import pandas as pd
import plotly.figure_factory as ff
import csv

df = pd.read_csv("moble_data.csv")

figure = ff.create_distplot([df["Avg Rating"].tolist()], ["Average"], show_hist = False)
figure.show()
