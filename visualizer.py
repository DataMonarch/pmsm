import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("darkgrid")
plt.style.use('seaborn')

def train_test_visualizer(X_test, y_test, history, n_cols):

    epochs = np.arange(1, len(history.history['loss']) + 1)
    y_pred = history.model.predict(X_test)
    n_rows = int(np.ceil(y_pred.shape[-1] / n_cols))


    mse = history.history['mean_squared_error']
    val_mse = history.history['val_mean_squared_error']

    fig1, ax = plt.subplots(figsize=(4 * n_cols, 3))

    ax.plot(epochs, mse, 'go', label='Training MSE', alpha=0.5)
    ax.plot(epochs, val_mse, 'r-', label='Validation MSE')
    ax.set_ylabel('MSE')
    ax.set_xlabel('No. epoch')
    ax.legend()

    fig1.suptitle('Training Stage')



    fig2, axes = plt.subplots(n_rows, n_cols, figsize=(4 * n_cols, 3 * n_rows))
    r2_total = r2_score(y_test, y_pred)


    for i, (ax, col) in enumerate(zip(axes.flatten(), target_features)):

        r2_col = r2_score(y_test[:, i], y_pred[:, i])
        mse = mean_squared_error(y_test[:, i], y_pred[:, i])
        rmse = np.sqrt(mse)

        sns.scatterplot(x=y_pred[:, i], y=y_test[:, i], label=f'R2: {r2_col:.2}\nMSE: {mse:.2}\nRMSE: {rmse:.2}', ax=ax, alpha=0.3)
    #     if i % n_cols == 0:
    #         ax.set_ylabel('Ground Truth')
    #     else:
    #         ax.set_ylabel('')
        ax.set_ylabel('Ground Truth')
        ax.set_xlabel('Predicted')
        ax.set_title(col)
        ax.legend()

    fig2.suptitle(f'Testing Stage --> total R2={r2_total:.5}')


    plt.tight_layout()
