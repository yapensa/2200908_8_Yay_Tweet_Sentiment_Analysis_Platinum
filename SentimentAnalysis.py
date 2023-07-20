import re
import sqlite3
import pandas as pd
import pickle
import numpy as np
from flask import Flask, jsonify, request
from flasgger import Swagger, LazyString, LazyJSONEncoder, swag_from
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from sklearn.neural_network import MLPClassifier
from sklearn.feature_extraction.text import TfidfVectorizer


app = Flask(__name__)
app.json_encoder = LazyJSONEncoder

# Swagger setup
swagger_template = dict(
    info={
        'title': LazyString(lambda: 'API Documentation BINAR PLATINUM CHALLENGE'),
        'version': LazyString(lambda: '1.0.0 // BETA'),
        'description': LazyString(lambda: 'API Documentation for Text Processing'),
    },
    host=LazyString(lambda: request.host)
)

swagger_config = {
    'headers': [],
    'specs': [
        {
            'endpoint': 'docs',
            'route': '/docs.json',
        }
    ],
    'static_url_path': '/flasgger_static',
    'swagger_ui': True,
    'specs_route': '/'
}

swagger = Swagger(app, template=swagger_template, config=swagger_config)

# Text preprocessing functions
def lowercase(text):
    return text.lower()

def perbaiki_kalimat(text):
    text = re.sub('((www\.[^\s]+)|(https?://[^\s]+)|(http?://[^\s]+))', ' ', text)
    text = re.sub(r'https://t.co/\w+', ' ', text)
    text = re.sub('\n', ' ', text)
    text = re.sub('rt', ' ', text)
    text = re.sub('  +', ' ', text)
    text = re.sub(r'pic.twitter.com.[\w]+', '', text)
    text = re.sub('user', ' ', text)
    text = re.sub(r"\bx\w{2}\b", "", text)
    text = re.sub(r'‚Ä¶', '', text)
    text = re.sub('[^0-9a-zA-Z]+', ' ', text)
    return text

# Mendapatkan path lengkap ke file database
database_path = r'C:\Users\AGRI07\Platinum-Challenge\database.db'

# Membuka koneksi ke database
baca_db = sqlite3.connect(database_path, check_same_thread=False)
tampil_tk = pd.read_sql_query('SELECT * FROM tkamus_alay', baca_db)
tampil_ta = pd.read_sql_query('SELECT * FROM tkata_kasar', baca_db)

alay_dict = dict(zip(tampil_tk['kata_alay'], tampil_tk['kata_normal']))

def alay_to_normal(huruf):
    result = []
    for word in huruf.split():
        if word in alay_dict:
            result.append(alay_dict[word])
        else:
            result.append(word)
    return ' '.join(result)

l_abusive = tampil_ta['kata_kasar'].str.lower().tolist()

def normalize_abusive(huruf):
    list_word = huruf.split()
    normalized_words = []
    for word in list_word:
        if word in l_abusive:
            # Mengganti kata kasar dengan kata sensor
            normalized_word = re.sub(r'\w', '*', word)
            normalized_words.append(normalized_word)
        else:
            normalized_words.append(word)
    return ' '.join(normalized_words)

def text_cleansing(text):
    text = lowercase(text)
    text = perbaiki_kalimat(text)
    text = alay_to_normal(text)
    text = normalize_abusive(text)
    text = text.replace("gue", "saya")

    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    text = stemmer.stem(text)

    factory = StopWordRemoverFactory()
    stopword = factory.create_stop_word_remover()
    text = stopword.remove(text)
    return text

# Loading LSTM model and tokenizer
model_lstm = load_model('lstm_model/model.h5')
file_lstm = open('lstm_resources/x_pad_sequences.pickle', 'rb')
feature_file_from_lstm = pickle.load(file_lstm)
file_lstm.close()

with open('lstm_resources/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

sentiment_labels = ['negative', 'neutral', 'positive']

def predict_sentiment(text):
    cleaned_text = text_cleansing(text)
    input_text = [cleaned_text]

    input_sequences = tokenizer.texts_to_sequences(input_text)
    input_sequences = pad_sequences(input_sequences, maxlen=feature_file_from_lstm.shape[1])

    sentiment_probabilities = model_lstm.predict(input_sequences)[0]
    sentiment_label = sentiment_labels[np.argmax(sentiment_probabilities)]

    return sentiment_label


# Load Neural Network model
with open('Neural Netwok/model.p', 'rb') as model_file:
    model_neural_network = pickle.load(model_file)

# Load the feature vectors from file
with open('Neural Netwok/feature.p', 'rb') as feature_file:
    feature_vectors = pickle.load(feature_file)

# Function to predict sentiment using the MLPClassifier model
def predict_sentiment_neural_network(text):
    cleaned_text = text_cleansing(text)
    input_text = [cleaned_text]

    input_vector = feature_vectors.transform(input_text)
    sentiment_label = model_neural_network.predict(input_vector)[0]

    return sentiment_label


# LSTM
# New endpoint for analyzing sentiment from LSTM input text
@app.route('/input_dataLSTM', methods=['POST'])
@swag_from("docs/input_dataLSTM.yml", methods=['POST'])
def test():
    input_txt = str(request.form["input_dataLSTM"])
    output_txt = text_cleansing(input_txt)
    sentiment_label = predict_sentiment(output_txt)

    # Store the input, output, and sentiment in the database if needed
    with sqlite3.connect("database.db") as conn:
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS tinput_data (input_text TEXT, output_text TEXT, sentiment TEXT)')
        query_txt = 'INSERT INTO tinput_data (input_text, output_text, sentiment) VALUES (?,?,?)'
        val = (input_txt, output_txt, sentiment_label)
        c.execute(query_txt, val)
        conn.commit()

    return_txt = {
        "input": input_txt,
        "output": output_txt,
        "sentiment": sentiment_label
    }

    return jsonify(return_txt)

# New endpoint for analyzing sentiment LSTM from a CSV file
@app.route('/upload_dataLSTM', methods=['POST'])
@swag_from("docs/upload_dataLSTM.yml", methods=['POST'])
def upload_file():
    file = request.files["upload_dataLSTM"]
    df_csv = pd.read_csv(file, encoding="latin-1")
    df_csv['new_tweet'] = df_csv['Tweet'].apply(text_cleansing)
    df_csv['sentiment'] = df_csv['Tweet'].apply(predict_sentiment)

    # Store the dataframe in the database or return it as JSON response
    with sqlite3.connect("database.db") as conn:
        df_csv.to_sql("clean_tweet", con=conn, index=False, if_exists='append')

    cleansing_tweet = df_csv[['new_tweet', 'sentiment']].to_dict(orient='records')
    return jsonify({'output': cleansing_tweet})

# Neural Netwok
# New endpoint for analyzing sentiment Neural Network from input text
@app.route('/input_dataNN', methods=['POST'])
@swag_from("docs/input_dataNN.yml", methods=['POST'])
def analyze_sentiment_text_nn():
    input_txt = str(request.form["input_dataNN"])
    output_txt = text_cleansing(input_txt)
    sentiment_label = predict_sentiment_neural_network(output_txt)

    return_txt = {
        "input": input_txt,
        "output": output_txt,
        "sentiment": sentiment_label
    }

    return jsonify(return_txt)


# New endpoint for analyzing sentiment Neural Network from a CSV file
@app.route('/upload_dataNN', methods=['POST'])
@swag_from("docs/upload_dataNN.yml", methods=['POST'])
def analyze_sentiment_csv_nn():
    file = request.files["upload_dataNN"]
    df_csv = pd.read_csv(file, encoding="latin-1")
    df_csv['cleaned_tweet'] = df_csv['Tweet'].apply(text_cleansing)
    df_csv['sentiment'] = df_csv['cleaned_tweet'].apply(predict_sentiment_neural_network)

    sentiment_results = df_csv[['cleaned_tweet', 'sentiment']].to_dict(orient='records')
    return jsonify({'sentiment_results': sentiment_results})



if __name__ == '__main__':
    app.run()
