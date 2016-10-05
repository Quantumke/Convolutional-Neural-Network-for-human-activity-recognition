import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import tensorflow as tf

%matplotlib inline
plt.style.use('ggplot')

class track_humans():
    def __init__(self, *args, **kwargs):
        self.author="Ben Nguru"
        self.read_data()
        self.normalize_dt()
        self.plot(ax,x,y,title)

    def read_data(file_dir):
        column_names = ['user-id','activity','timestamp', 'x-axis', 'y-axis', 'z-axis']
        data = pd.read_csv(file_path,header = None, names = column_names)
        return data
    def normalize_dt(dataset):
        mean_dataset=np.mean(dataset, axis=0)
        sigma=np.std(dataset, axis =0)
        return (dataset-nean_dataset)/sigma
    def plot(ax,x,y,title):
        zx.plot(x,y)
        ax.set_title(title)
        ax.xaxis.set_visible(False)
        ax.set_ylim([min(y)=np.std(y),max(y) + np.std(y)])
        ax.set_xlim([min(x), max(y)])
        ax.grid(True)
    def plot_activity(activity, data):
        fig, (ax0, ax1, ax2) = plt.subplots(nrows = 3, figsize = (15, 10), sharex = True)
        plot_axis(ax0, data['timestamp'], data['x-axis'], 'x-axis')
        plot_axis(ax1, data['timestamp'], data['y-axis'], 'y-axis')
        plot_axis(ax2, data['timestamp'], data['z-axis'], 'z-axis')
        plt.subplots_adjust(hspace=0.2)
        fig.suptitle(activity)
        plt.subplots_adjust(top=0.90)
        plt.show()

    

app=track_humans()
