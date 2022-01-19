import numpy as np
import pandas as pd
from tensorflow.keras.layers import Dense , Input, Dropout, Flatten
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Conv1D, MaxPool1D, add
from tensorflow.keras import layers
import tensorflow as tf
from tensorflow.keras import models, optimizers as opts

def cnn_model_builder(seq_len, n_features, n_targets, kernel_size, activation=None):

    x = Input((seq_len, n_features), name='input_62')
    y = Conv1D(filters=1024, kernel_size=kernel_size, padding='same', activation='relu')(x)

    y = Conv1D(filters=512, kernel_size=kernel_size, padding='same',
                      dilation_rate=2, activation='relu')(y)

    shortcut = Conv1D(filters=512, kernel_size=1,
                             dilation_rate=2, padding='same')(x)
    y = add([shortcut, y])

    y = MaxPool1D(pool_size=64)(y)
    y = Flatten()(y)
    y = Dense(128, name='dense_64', activation=activation)(y)
    y = Dropout(rate=0.05)(y)
    y = Dense(n_targets, name=f'dense_{n_targets}', activation=activation)(y)

    model = models.Model(inputs=x, outputs=y)
    model.compile(optimizer=opts.Adam(), loss='mse', metrics=['MeanSquaredError', 'mae'])

    return model
