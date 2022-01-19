import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def seq_data_preprocessing(data):
    std_scaler = StandardScaler()
    data = pd.DataFrame(std_scaler.fit_transform(data), columns=list(data.columns))

    return data

def split_sequence_train_test(data, test_size, seq_len, batch_size, input_cols, target_cols, groupby_col='profile_id', random_state=42):
    data_grpd = {pid: df_ for pid, df_ in data.groupby(groupby_col)}

    sequential_data = []

    for group_id, group_df in data_grpd.items():
        batch = []
        group_df.index = np.arange(len(group_df))
        batch_no = 0

        group_df = seq_data_preprocessing(group_df)

        while True:
            start = np.random.choice(group_df.index)
            end = start + seq_len

            if end > len(group_df)-1:
                continue

            seq_X, seq_y = group_df.loc[start : end-1, input_cols].values, group_df.loc[end, target_cols].values
            sequential_data.append([seq_X, seq_y])
            batch_no += 1
#             print(f"--> batch no.{batch_no} for profile id {group_id} ready")

            if batch_no >= batch_size:
                break
    print("! Sequence build complete")

    X, y = zip(*sequential_data)
    X, y = np.array(X), np.array(y)


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    print("! Train test split complete")

    return (X_train, X_test, y_train, y_test)
