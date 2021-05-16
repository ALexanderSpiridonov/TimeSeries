import os
import matplotlib.pyplot as plt

# full path to the project directory
ROOT_DIR = os.path.dirname(__file__)

# plot time series data
def plot_series(time, series, format="-", start=0, end=None):
    plt.figure(figsize=(15, 5))
    plt.plot(time[start:end], series[start:end], format)
    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.grid(True)