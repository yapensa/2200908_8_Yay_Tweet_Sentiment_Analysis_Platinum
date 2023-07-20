# TweetSentimentAnalysis
Pembuatan Api Dengan Pemodelan Machine Learning Dan Deep Learning Dan Analisa Data

# Data
2 jenis data sekunder yang kami gunakan untuk menyelesaikan proyek ini, yaitu:

1. Daya untuk membuat model (train_preprocess.tsv.txt), yang terdiri dari 11.000 baris dan 2 kolom.
2. Data untuk melakukan klasifikasi atau menguji model, yang mana file utama (data.csv) terdiri dari 13.169 baris dan 15 kolom, kolom yang akan diuji adalah “tweet” dan beberapa data pendukung lainnya:
![image](https://github.com/yapensa/TweetSentimentAnalysis/assets/8088664/dfd5bcb5-766d-4e66-be22-a44af0b38656)

# Tujuan
1. Mendapatkan nilai sentiment dari tweet para pengguna twitter.
2. Mendapatkan model dengan performa terbaik antara Neural Netwok dan Long Short-Term Memory (LSTM) untuk memprediksi sentimen. 
3. Membuat mesin/API yang dapat mengklasifikasikan sentimen dari data yang ada.
![image](https://github.com/yapensa/TweetSentimentAnalysis/assets/8088664/d58e9ca0-e434-4d8b-b91c-f677a3060deb)


# Kesimpulan
1. Sentimen analisis memberikan wawasan yang berharga bagi pengguna. Khusus untuk perusahaan dan organisasi, dapat menjadi acuan dalam mengambil keputusan yang lebih baik, merespons dengan cepat terhadap perubahan pasar atau opini masyarakat, serta meningkatkan interaksi dan hubungan dengan pelanggan. 
2. Model LSTM memiliki performa yang lebih baik dibandingkan dengan model NN, meskipun model cenderung menampilka grafik overfitting, tetapi hasil sentiment cukup baik.
3. API yang dibuat setiap model memiliki 2 endpoint (untuk memproses teks dan data file csv) yang dapat menampilkan label positif, negatif, atau netral berdasarkan hasil dari proses modelnya.
![image](https://github.com/yapensa/TweetSentimentAnalysis/assets/8088664/fb008e42-e918-46bc-a800-4055e0baaa2e)
