import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def seq_data_preprocessing(data):
    std_scaler = StandardScaler()
    data = pd.DataFrame(std_scaler.fit_transform(data), columns=list(data.columns))

    return data
