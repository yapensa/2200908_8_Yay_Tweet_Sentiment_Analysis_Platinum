# TweetSentimentAnalysis
![image](https://github.com/yapensa/TweetSentimentAnalysis/assets/8088664/366acd2b-9018-45c4-9b21-3f4a01a4a8f0)
Pembuatan Api Dengan Pemodelan Machine Learning Dan Deep Learning Dan Analisa Data

# Data
2 jenis data sekunder yang kami gunakan untuk menyelesaikan proyek ini, yaitu:

1. Daya untuk membuat model (train_preprocess.tsv.txt), yang terdiri dari 11.000 baris dan 2 kolom.
2. Data untuk melakukan klasifikasi atau menguji model, yang mana file utama (data.csv) terdiri dari 13.169 baris dan 15 kolom, kolom yang akan diuji adalah “tweet” dan beberapa data pendukung lainnya:
![image](https://github.com/yapensa/TweetSentimentAnalysis/assets/8088664/9e78e722-2f6b-4d94-a003-014ea8bd7d7c)


# Tujuan
1. Mendapatkan nilai sentiment dari tweet para pengguna twitter.
2. Mendapatkan model dengan performa terbaik antara Neural Netwok dan Long Short-Term Memory (LSTM) untuk memprediksi sentimen. 
3. Membuat mesin/API yang dapat mengklasifikasikan sentimen dari data yang ada.

# Hasil Berdasarkan Sentimen
![image](https://github.com/yapensa/TweetSentimentAnalysis/assets/8088664/34a79608-4a71-4242-8dcb-fb6e251a4a1c)

# Kesimpulan
1. Sentimen analisis memberikan wawasan yang berharga bagi pengguna. Khusus untuk perusahaan dan organisasi, dapat menjadi acuan dalam mengambil keputusan yang lebih baik, merespons dengan cepat terhadap perubahan pasar atau opini masyarakat, serta meningkatkan interaksi dan hubungan dengan pelanggan. 
2. Model LSTM memiliki performa yang lebih baik dibandingkan dengan model NN, meskipun model cenderung menampilka grafik overfitting, tetapi hasil sentiment cukup baik.
3. API yang dibuat setiap model memiliki 2 endpoint (untuk memproses teks dan data file csv) yang dapat menampilkan label positif, negatif, atau netral berdasarkan hasil dari proses modelnya.
