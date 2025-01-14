# -*- coding: utf-8 -*-
"""submission-timeSeries.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NrYEjIb4F0A2PBwHfTkl61zah_Ixb6yB

## **Submission Kedua Kelas Machine Learning Intermediate**

Nama: Muhammad Fayzul Haq <br>
Tahun Pengerjaan: Januari 2024

dataset : https://www.kaggle.com/datasets/meetnagadia/apple-stock-price-from-19802021
"""

import numpy as np
import pandas as pd
import seaborn as sb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
import tensorflow as tf

data_train = pd.read_csv('appleStock.csv')
data_train.head()

"""### Informasi tambahan
- Open: It is the price at which the financial security opens in the market when trading begins.
- High : The high is the highest price at which a stock traded during a period.
- Low : The low is the lowest price at which a stock traded during a period.
- CLose : Closing price generally refers to the last price at which a stock trades during a regular trading session.
- Adj Close : The adjusted closing price amends a stock's closing price to reflect that stock's value after accounting.
- Volume : Volume measures the number of shares traded in a stock or contracts traded in futures or options
"""

dates = data_train['Date'].values
volume  = data_train['Volume'].values


plt.figure(figsize=(15,5))
plt.plot(dates, volume)
plt.title('Volume average',
          fontsize=20);

plt.figure(figsize=(15,5))
plt.plot(dates, data_train['Open'].values, linestyle="-", marker="o", label="Open")
plt.legend()
plt.title('Open',fontsize=20);
plt.show()

plt.figure(figsize=(15,5))
plt.plot(dates, data_train['Close'].values, linestyle="-", marker="o", label="Close")
plt.legend()
plt.title('Close',fontsize=20);
plt.show()

newdf = pd.read_csv('appleStock.csv', index_col="Date", parse_dates=True)
newdf.head(3)

"""## **Grafik Rata-rata di setiap bulan**"""

plt.figure(figsize=(15,5))
df_monthly_means = newdf.groupby(pd.Grouper(level="Date", freq="M")).mean()

fig, axes = plt.subplots(5, 1, figsize=(15, 20))

# Plot data untuk setiap kolom
axes[0].plot(df_monthly_means["Open"], label="Open")
axes[1].plot(df_monthly_means["Close"], label="Close")
axes[2].plot(df_monthly_means["High"], label="High")
axes[3].plot(df_monthly_means["Low"], label="Low")
axes[4].plot(df_monthly_means["Volume"], label="Volume")

for ax in axes:
    ax.set_xlabel("Month")
    ax.set_ylabel("Value")
    ax.legend()

plt.show()

data_train['Date'] = pd.to_datetime(data_train['Date'])

tanggal_awal = pd.to_datetime('2024-01-27')
data_train['Date'] = (data_train['Date'] - tanggal_awal).dt.days

data_train.head(3)

data_train.info()

min_max_scaler = MinMaxScaler()
data_train_normalized = min_max_scaler.fit_transform(data_train)

"""fungsi di bawah yang dapat mengubah data kita menjadi format yang dapat diterima oleh model. Fungsi di bawah menerima sebuah series/atribut kita yang telah di konversi menjadi tipe numpy, lalu mengembalikan label dan atribut dari dataset dalam bentuk batch."""

data_train_normalized_df = pd.DataFrame(data_train_normalized, columns=data_train.columns)

threshold_mae = (data_train_normalized_df['Open'].max() - data_train_normalized_df['Open'].min()) * 10/100
print(threshold_mae)

class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        if(logs.get('mae') < threshold_mae and logs.get('val_mae') >= 0.34):
            print("\nMAE telah mencapai <10%!")
            self.model.stop_training = True

callbacks = myCallback()

def windowed_dataset(series, window_size, batch_size, shuffle_buffer):
    series = tf.expand_dims(series, axis=-1)
    ds = tf.data.Dataset.from_tensor_slices(series)
    ds = ds.window(window_size + 1, shift=1, drop_remainder=True)
    ds = ds.flat_map(lambda w: w.batch(window_size + 1))
    ds = ds.shuffle(shuffle_buffer)
    ds = ds.map(lambda w: (w[:-1], w[-1:]))
    return ds.batch(batch_size).prefetch(1)

WINDOW_SIZE = 60
BATCH_SIZE = 100
SHUFFLE_BUFFER = 1000

X_train_normalized, X_val_normalized, y_train, y_val = train_test_split(data_train_normalized_df['Open'], data_train_normalized_df['Date'], test_size=0.2, shuffle=False)

X_train_windowed_normalized = windowed_dataset(X_train_normalized, WINDOW_SIZE, BATCH_SIZE, SHUFFLE_BUFFER)
X_val_windowed_normalized = windowed_dataset(X_val_normalized, WINDOW_SIZE, BATCH_SIZE, SHUFFLE_BUFFER)

model = tf.keras.models.Sequential([
  tf.keras.layers.LSTM(60, return_sequences=True, input_shape=(WINDOW_SIZE, 1)),
  tf.keras.layers.LSTM(30),
  tf.keras.layers.Dense(30, activation="relu"),
  tf.keras.layers.Dense(10, activation="relu"),
  tf.keras.layers.Dense(1),
])

model.summary()

optimizer = tf.keras.optimizers.SGD(learning_rate=1.0000e-04, momentum=0.9)
model.compile(loss=tf.keras.losses.Huber(),
              optimizer=optimizer,
              metrics=["mae"])

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import time
# %matplotlib inline

start_time = time.time()

history = model.fit(X_train_windowed_normalized, epochs=10, validation_data=X_val_windowed_normalized)
# history = model.fit(X_train_windowed_normalized, epochs=10, validation_data=X_val_windowed_normalized, callbacks=[callbacks])

end_time = time.time()
training_time = end_time - start_time

print(f"Waktu pelatihan: {training_time / 60:.2f} menit")

#Membuat accuracy plot
plt.plot(history.history['mae'], label='Training MAE')
plt.plot(history.history['val_mae'], label='Validation MAE')
plt.title(f"MAE Plot")
plt.ylabel('Value')
plt.xlabel('Epoch')
plt.legend(loc="lower right")
plt.show()

# Membuat loss plot
plt.plot(history.history["loss"], label='Training Acc')
plt.plot(history.history["val_loss"], label='Validation Acc')
plt.title(f"Loss Plot")
plt.ylabel('Value')
plt.xlabel('Epoch')
plt.legend(loc="lower right")
plt.show()

