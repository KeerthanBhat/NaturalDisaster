import tensorflow as tf
from keras import optimizers
from keras.models import load_model
import numpy as np


model = load_model('Model.h5')

optimizer = tf.train.RMSPropOptimizer(0.002)

model.compile(loss='mse',
            optimizer=optimizer,
            metrics=['accuracy'])

#pridection = np.array([minitemp,maxitemp,windgust,wind9,wind3,humid9,humid3,pressure9,pressure3,temp9,temp3])
pridection = np.array([20.9,23.3,65,37,31,96,96,1006.8,1004.2,21.5,21.3])
#pridection = np.array([2,1,100,100,1,1,1,1,1,1,1])

mean = np.array([12.068963,23.009951,37.19739,13.88135,18.25159,67.70561,49.9628,911.645197,909.72206092,16.76982,21.128429])

std = np.array([6.47953722,7.41225215,16.68598056,9.01179628,9.14530111,20.95509877,22.34781323,310.98021687,309.95752359,6.71328472,7.64915217])

pridection = (pridection - mean) / std

if (pridection.ndim == 1):
    pridection = np.array([pridection])

rainfall = model.predict(pridection)

floods = (rainfall - 5) * 5

if (floods > 100):
    floods = 100

print(rainfall)
