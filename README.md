Görselde görüldüğü üzere uygulamanızda bir form mevcut ve kullanıcıdan CSV dosyası ile analiz yapılacak sütun adını alıyorsunuz. Ardından çıktı otomatik olarak indiriliyor. Bu işleyişe uygun bir düzenleme için README'yi şu şekilde güncelleyebiliriz:

---

### **Sentizer: Türkçe Duygu Analizi Aracı**

Sentizer, Türkçe metinlere özel geliştirilmiş bir duygu analizi uygulamasıdır. Kullanıcı dostu web arayüzü sayesinde kolayca CSV dosyası yükleyip belirtilen sütun üzerinden metin analizlerinizi gerçekleştirebilir ve sonucu anında indirebilirsiniz.

---

### **Özellikler**
- **Kolay Kullanım**: Basit ve sezgisel bir web arayüzü sunar.
- **Hızlı Çıktı**: Analiz edilen verileri otomatik olarak indirir.
- **Türkçe Desteği**: Türkçe metinler için optimize edilmiştir.
- **Doğruluk Odaklı**: BERT tabanlı modelle yüksek doğruluk sağlar.

---

### **Kurulum ve Çalıştırma**
1. **Gereksinimler:**
   - Python 3.8 veya üzeri
   - Flask, Pandas, NumPy, Transformers kütüphaneleri

2. **Kurulum:**
   ```bash
   git clone https://github.com/kullaniciadi/sentizer.git
   cd sentizer
   pip install -r requirements.txt
   ```

3. **Uygulamayı Başlatma:**
   ```bash
   python app.py
   ```
   Komut çalıştırıldıktan sonra uygulama, `http://127.0.0.1:5000` adresinde açılacaktır.

4. **Kullanım:**
   - Web arayüzüne gidin ve analiz edilecek CSV dosyasını yükleyin.
   - Analiz yapılacak sütun adını girin (örneğin: `Comments`).
   - "Gönder" butonuna tıkladığınızda analiz işlemi başlar ve sonuç dosyası otomatik olarak indirilir.

---

### **Sonuç Dosyası**
İndirilen dosyada, orijinal verilere ek olarak her metnin duygu analizi sonucu yer alır:
- **Sentiment**: Metnin olumlu, olumsuz veya nötr olduğunu belirtir.

---

### **Lisans**
Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasını inceleyin.

---

Bu düzenleme, hem görseldeki arayüzün hem de uygulamanın işleyişinin README dosyasına net bir şekilde yansıtılmasını sağlar.
