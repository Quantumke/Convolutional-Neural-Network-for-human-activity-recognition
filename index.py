import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import tensorflow as tf

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
        ax.set_ylim([min(y) - np.std(y), max(y) + np.std(y)])
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
        for activity in np.unique(dataset["activity"]):
            subset = dataset[dataset["activity"] == activity][:180]
            plot_activity(activity,subset)
    def windows(data, size):
        start = 0
        while start < data.count():
            yield start, start + size
            start += (size / 2)
    def segment_signal(data,window_size = 90):
        segments = np.empty((0,window_size,3))
        labels = np.empty((0))
        for (start, end) in windows(data["timestamp"], window_size):
            x = data["x-axis"][start:end]
            y = data["y-axis"][start:end]
            z = data["z-axis"][start:end]
            if(len(dataset["timestamp"][start:end]) == window_size):
                segments = np.vstack([segments,np.dstack([x,y,z])])
                labels = np.append(labels,stats.mode(data["activity"][start:end])[0][0])
        return segments, labels
    input_height = 1
    input_width = 90
    num_labels = 6
    num_channels = 3
    batch_size = 10
    kernel_size = 60
    depth = 60
    num_hidden = 1000
    learning_rate = 0.0001
    training_epochs = 5
    total_batchs = reshaped_segments.shape[0] // batch_size
    def weight_variable(shape):
        initial = tf.truncated_normal(shape, stddev = 0.1)
        return tf.Variable(initial)
    def bias_variable(shape):
        initial = tf.constant(0.0, shape = shape)
        return tf.Variable(initial)
    def depthwise_conv2d(x, W):
        return tf.nn.depthwise_conv2d(x,W, [1, 1, 1, 1], padding='VALID')
    def apply_depthwise_conv(x,kernel_size,num_channels,depth):
        weights = weight_variable([1, kernel_size, num_channels, depth])
        biases = bias_variable([depth * num_channels])
        return tf.nn.relu(tf.add(depthwise_conv2d(x, weights),biases))
    def apply_max_pool(x,kernel_size,stride_size):
        return tf.nn.max_pool(x, ksize=[1, 1, kernel_size, 1],
                              strides=[1, 1, stride_size, 1], padding='VALID')
    cost_history = np.empty(shape=[1],dtype=float)
    with tf.Session() as session:
        tf.initialize_all_variables().run()
        for epoch in range(training_epochs):
            for b in range(total_batchs):
                offset = (b * batch_size) % (train_y.shape[0] - batch_size)
                batch_x = train_x[offset:(offset + batch_size), :, :, :]
                batch_y = train_y[offset:(offset + batch_size), :]
                c = session.run([optimizer, loss],feed_dict={X: batch_x, Y : batch_y})
                cost_history = np.append(cost_history,c)
                print "Epoch: ",epoch," Training Loss: ",c," Training Accuracy: ",
                session.run(accuracy, feed_dict={X: train_x, Y: train_y})
            print "Testing Accuracy:", session.run(accuracy, feed_dict={X: test_x, Y: test_y})


    

app=track_humans()
dataset = read_data('actitracker_raw.txt')
dataset['x-axis'] = feature_normalize(dataset['x-axis'])
dataset['y-axis'] = feature_normalize(dataset['y-axis'])
dataset['z-axis'] = feature_normalize(dataset['z-axis'])
