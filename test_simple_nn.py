import tensorflow as tf
import numpy as np

x = np.random.random(size=(16384, 3))
y = 3 * x[:, 0] ** 2 + 2 * x[:, 1] - x[:, 2]

mod = tf.keras.models.Sequential()
mod.add(tf.keras.layers.Dense(10, input_shape=(3,)))
mod.add(tf.keras.layers.Activation("relu"))
mod.add(tf.keras.layers.Dense(1))
mod.compile(loss="mse", optimizer="adam")
mod.fit(x, y, epochs=10, batch_size=128)
