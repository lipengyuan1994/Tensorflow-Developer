import tensorflow as tf


# Preparing features and labels


dataset = tf.data.Dataset.range(10)
# dataset = dataset.window(5, shift=1 )
dataset = dataset.window(5, shift=1, drop_remainder=True)
dataset = dataset.flat_map(lambda window: window.batch(5))
for window_dataset in dataset:
    print(window_dataset.numpy())  # --> convert to numpy list

# split the data into features and labels.
dataset = dataset.map(lambda window: (window[:-1], window[-1:]))
for x, y in dataset:
    print(x.numpy(), y.numpy())

# look at batching the data
ddataset = dataset.shuffle(buffer_size=10)
dataset = dataset.batch(2).prefetch(1)
for x, y in dataset:
    print("x= ", x.numpy())
    print("y= ", y.numpy())
