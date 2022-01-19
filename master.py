import pandas as pd

target_features = ['motor_speed', 'torque', 'stator_yoke', 'stator_tooth', 'stator_winding']
input_features = ['u_q', 'u_d', 'i_q', 'i_d', 'coolant', 'ambient']

seq_len = 256
batch_size = 500

# data can be found in this kaggle repo
# "https://www.kaggle.com/wkirgsn/electric-motor-temperature?select=measures_v2.csv"
