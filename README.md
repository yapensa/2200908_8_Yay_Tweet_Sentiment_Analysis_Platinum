# Tweet Sentiment Analysis
![image](https://github.com/yapensa/TweetSentimentAnalysis/assets/8088664/366acd2b-9018-45c4-9b21-3f4a01a4a8f0)
Pembuatan Api Dengan Pemodelan Machine Learning Dan Deep Learning Dan Analisa Data

# Data
2 jenis data sekunder yang kami gunakan untuk menyelesaikan proyek ini, yaitu:

1. Data untuk membuat model (train_preprocess.tsv.txt), yang terdiri dari 11.000 baris dan 2 kolom.
2. Data untuk melakukan klasifikasi atau menguji model, yang mana file utama (data.csv) terdiri dari 13.169 baris dan 15 kolom, kolom yang akan diuji adalah “tweet”.

# Tujuan
1. Mendapatkan nilai sentiment dari tweet para pengguna twitter.
2. Mendapatkan model dengan performa terbaik antara Neural Netwok dan Long Short-Term Memory (LSTM) untuk memprediksi sentimen. 
3. Membuat mesin/API yang dapat mengklasifikasikan sentimen dari data yang ada.

# Hasil Berdasarkan Sentimen
![image](https://github.com/yapensa/TweetSentimentAnalysis/assets/8088664/26716029-7c6c-4491-a015-3c7ee4eeef1d)

# Kesimpulan
1. Sentimen analisis memberikan wawasan yang berharga bagi pengguna. Khusus untuk perusahaan dan organisasi, dapat menjadi acuan dalam mengambil keputusan yang lebih baik, merespons dengan cepat terhadap perubahan pasar atau opini masyarakat, serta meningkatkan interaksi dan hubungan dengan pelanggan. 
2. Model LSTM memiliki performa yang lebih baik dibandingkan dengan model NN, meskipun model cenderung menampilka grafik overfitting, tetapi hasil sentiment cukup baik.
3. API yang dibuat setiap model memiliki 2 endpoint (untuk memproses teks dan data file csv) yang dapat menampilkan label positif, negatif, atau netral berdasarkan hasil dari proses modelnya.
