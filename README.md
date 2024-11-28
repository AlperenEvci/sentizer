
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

3. Modelin ilk farklı kullanım şekli vardır:
1) Local Kullanım  
   Bert-tr-sentiment adlı klasör modelin parametrelerini ve dosyalarını içeren klasör lokalde çalıştırmak için bu dosyaya ihtiyaç var
   Gerekli dosyaya https://huggingface.co/AlperenEvci/bert-tr-sentiment üzerinden ulaşıp klonlama yapabilirsiniz.
   Dosya boyutu yüksek olduğu için paylaşamadım

2) Transformersdan Pipeline yoluyla kullanım
   "sentizer.py" adlı dosyada kullanım şekli yorum satırlı olarak belirtilmiştir

   gerekli kütüphaneler "requirements.txt" adlı klasörde mevcuttur.
   terminal üzerinde "pip install -r requirements.txt" komutu ile gerekli kütüphanelerin yüklenmesi sağlanır

   modeli "sentiusage.ipynb" dosyası üzerinde ve terminalden "python sentizer.py" komutu ile çalıştırabilirsiniz
   kullanılacak verideki yorumlara eş gelen sütun ismi ile işleminizi gerçekleştirip çıktı dosyasını otomatik olarak indirebilirsiniz.


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
