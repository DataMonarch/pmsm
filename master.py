import pandas as pd
from data_preprocessing import seq_data_preprocessing, split_sequence_train_test
from cnn_builder import cnn_model_builder
from visualizer import train_test_visualizer

target_features = ['motor_speed', 'torque', 'stator_yoke', 'stator_tooth', 'stator_winding']
input_features = ['u_q', 'u_d', 'i_q', 'i_d', 'coolant', 'ambient']

seq_len = 256
batch_size = 500

# data can be found in this kaggle repo
# "https://www.kaggle.com/wkirgsn/electric-motor-temperature?select=measures_v2.csv"

cnn_model = cnn_model_builder(seq_len, n_features=6, n_targets=5, kernel_size=2)
cnn_model.summary()

training_history = []

epochs = 100

model_es_callback = tf.keras.callbacks.EarlyStopping(
#     filepath='../output/',
#     save_weights_only=True,
    monitor='val_mean_squared_error',
    min_delta = 0.0001,
    patience = 10,
    verbose = 1,
    mode='min',
    restore_best_weights=True)


history = cnn_model.fit(X_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.2, callbacks=[model_es_callback])
training_history.append(history)

train_test_visualizer(X_test, y_test, training_history[-1], 3)
