## Catatan Dari Reviewer

Hallo fayzul!, Selamat! Kamu telah berhasil menyelesaikan tugas untuk Proyek Kedua : Membuat Model Machine Learning dengan Data Time Series. Dengan demikian Anda telah memahami bagaimana mengimplementasikan model untuk prediksi Time Series dengan Tensorflow dan Keras.

Terima kasih telah sabar menunggu. Kami membutuhkan waktu untuk bisa memberikan feedback yang komprehensif. Untuk meningkatkan kualitas project submission yang dikirimkan, kamu dapat menerapkan beberapa saran berikut:

**Overall Review**

Well done! Penerapan yang kamu lakukan pada submission ini sangatlah bagus. Selain itu, MAE yang dihasilkan oleh model juga memiliki hasil yang bagus dengan menggunakan >10k dataset.

**Code Review**

Pada proses pembuatan model, menggunakan optimizer SGD. Kamu dapat mencoba optimizer yang lain seperti Adam atau RMSprop untuk membandingkan performanya.

**Saran**

- Selain menggunakan helper function windowed_dataset, kamu juga dapat mempelajari penggunaan TimeSeriesGenerator untuk mempersiapkan data time series agar dapat diterima oleh model
- Kamu juga dapat menggunakan fungsi TimeSeriesSplit untuk membagi dataset
Dataset timeseries tidak boleh di-shuffle karena memiliki urutan waktu yang terus berurutan. Jika dataset time series di-shuffle, maka urutan waktu dari data tersebut akan hilang dan tidak dapat digunakan untuk analisis.
- Kamu dapat memberikan insight terhadap dataset dengan melakukan visualisasi data timeseries time series data visualizations
Untuk menurunkan MAE, kamu dapat Mengatur Hyperparameter LSTM pada Time Series dan Menggunakan Bidirectional LSTM
- Kamu dapat download dataset dari Kaggle dengan menggunakan Kaggle API dan download datasets from Kaggle to Google Colab dan cara menghubungkan drive ke colab
- Kamu juga dapat mempelajari model yang kamu buat apakah sudah good fit atau belum Perbedaan Goodfit, Overfit dan Underfit
- Kamu bisa mempelajari beberapa hal berikut untuk memperluas pengetahuan   tentang machine learning:
    - Menerapkan Custom Callback
    - Memahami Impact Learning Rate



**Additional Tips**

- Kamu bisa menghapus text cell, code cell, atau komentar kode yang tidak digunakan dalam notebook agar penulisan kode dan text lebih rapi.

- Agar penulisan kode lebih rapi pada proses debugging (preprocess data, membuat model, dan melakukan testing), kamu bisa menyimpan seluruh import pada Code Cell yang paling atas untuk meningkatkan kualitas keterbacaan kode.

- Google Collaboratory memiliki fitur untuk menggunakan GPU. Kamu dapat memanfaatkan GPU gratis pada google collaboratory agar proses training yang dilakukan lebih cepat.

- Setelah proses training selesai, kamu bisa menambahkan plot loss dan akurasi untuk mempermudah evaluasi model secara grafik dengan menggunakan:
    - Matplotlib
    - Tensorboard

- Kamu dapat menggunakan fitur markdown/text cell untuk menjelaskan bagian code cell yang telah kamu buat pada interactive python notebook. Sehingga, notebook kamu lebih informatif.

## Rating: 5/5