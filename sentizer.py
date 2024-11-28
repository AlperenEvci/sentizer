from flask import Flask, render_template, request, redirect, url_for, send_file
import pandas as pd
import numpy as np
from transformers import TFAutoModelForSequenceClassification, AutoTokenizer
import tensorflow as tf
import os
import chardet

app = Flask(__name__) 

# Model ve tokenizer'ı yükleyelim   #localde çalıştırırken bu şekilde çalıştırabilirsiniz
model_name = "bert-tr-sentiment"
model = TFAutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

#modeli trasnformers kütüphanesinden çekiyoruz #online olarak çalıştırırken bu şekilde çalıştırabilirsiniz
# Load model directly
#from transformers import AutoTokenizer, AutoModelForSequenceClassification
#tokenizer = AutoTokenizer.from_pretrained("AlperenEvci/bert-tr-sentiment")
#model = AutoModelForSequenceClassification.from_pretrained("AlperenEvci/bert-tr-sentiment")

# Sentiment analiz fonksiyonu
def process_comments(filename, column_name):
    # 'processed' klasörünün varlığını kontrol et, yoksa oluştur
    if not os.path.exists('processed'):
        os.makedirs('processed')

    # Veriyi yükle
    df = pd.read_csv(filename)
    
    # Yorumlar için tahmin yapma fonksiyonu
    def predict(text):
        inputs = tokenizer(text, return_tensors="tf", truncation=True, max_length=512)
        output = model(**inputs)
        return output.logits.numpy()

    # Modeli kullanarak tahminleri yap ve sentiment kolonu ekle
    df["sentiment"] = df[column_name].apply(lambda x: predict(x))
    df["sentiment"] = df["sentiment"].apply(lambda x: np.argmax(x, axis=1))
    df["sentiment"] = df["sentiment"].apply(lambda x: "positive" if x == 1 else ("negative" if x == -1 else "neutral"))
    
    # Sadece sentiment ve yorum kolonlarını içeren bir tablo oluştur
    df = df[["sentiment", column_name]]
    
    # Yeni bir CSV dosyasına kaydet
    output_filename = filename.replace(".csv", "_sentiment.csv")
    output_path = os.path.join('processed', os.path.basename(output_filename))  # Dosya yolu 'processed' klasörüne olacak
    df.to_csv(output_path, index=False,encoding='utf-8-sig')
    
    return output_path

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # Dosya ve sütun ismini al
        file = request.files['file']
        column_name = request.form['column_name']
        
        if not file or not column_name:
            return "Lütfen dosya ve sütun ismini giriniz!"
        


        # Dosyayı kaydet
        upload_folder = 'uploads'
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
        filepath = os.path.join(upload_folder, file.filename)
        file.save(filepath)  # Dosya 'uploads' klasörüne kaydediliyor

        # Dosyanın karakter kodlamasını algıla
        with open(filepath, 'rb') as f:
            result = chardet.detect(f.read())
            encoding = result['encoding']

        # Dosyayı uygun karakter kodlaması ile oku (utf-8, iso-8859-9 ya da windows-1254)
        try:
            df = pd.read_csv(filepath, encoding=encoding)
            df.to_csv(filepath, index=False, encoding='utf-8-sig')
        except UnicodeDecodeError:
            # Eğer okuma hatası alırsanız, diğer kodlamayı deneyin
            df = pd.read_csv(filepath, encoding='ISO-8859-9')
            df.to_csv(filepath, index=False, encoding='utf-8-sig')

        # Sentiment analiz işlemini yap
        output_filename = process_comments(filepath, column_name)
        
        # İşlem tamamlandığında dosyayı kullanıcıya indirme linkiyle göster
        return redirect(url_for('download_file', filename=output_filename ,encoding='utf-8-sig'))

@app.route('/download/<path:filename>')
def download_file(filename):
    try:
        return send_file(filename, as_attachment=True)
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)
