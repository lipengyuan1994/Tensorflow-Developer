from tensorflow import keras
import numpy as np

# The Hello World of Deep Learning with Neural Networks

# fit  Y=2X-1 in neural network

# Define and Compile the Neural Network
model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')

xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-3, -1, 1, 3, 5, 7], dtype=float)
# Training the Neural Network
model.fit(xs, ys, epochs=500)

print(model.predict([10.0]))
