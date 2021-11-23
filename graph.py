# Graphing functions
import os
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"

import matplotlib.pyplot as plt

# plot a 2d line graph
def plot_graph(data):
  plt.rcParams["figure.figsize"] = (6, 3)
  plt.rcParams['toolbar'] = 'None'
  plt.plot(data)
  plt.pause(0.001)