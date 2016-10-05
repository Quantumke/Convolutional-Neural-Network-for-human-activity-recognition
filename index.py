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

    def read_data(file_dir):
        column_names = ['user-id','activity','timestamp', 'x-axis', 'y-axis', 'z-axis']
        data = pd.read_csv(file_path,header = None, names = column_names)
        return data

    

app=track_humans()
