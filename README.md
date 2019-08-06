# 476_573_plate_recognition
preprocessing olarak input olarak verilecek folder'ın içerisinde bir kereliğine terminal üzerinden **```mogrify -resize 200X200 .*.```** komutunu çalıştırın. <br>
```python3 plaka_tanima.py --folder <folder_name>```
<br>Note: folder_name should end with "/"
<br>**results.html** must be created in repo directory.

## OCR-Training adımları
Hazırlık: ```git clone https://github.com/openalpr/train-ocr```
### 1- Karakter sınıflandırmak için aşağıdaki komutu çalıştırın
Bu işlemi Windows ortamında gerçekleştirmek için [bu](https://github.com/glleung/LPReader) linkteki repo klonlanarak openalpr_64bit klasörü altındaki executable **openalpr-utils-classifychars.exe** kullanılabilir. Bu işlem yapılırken  input folder'ındaki tüm dosyaların uzantılarını küçük harflere çevirmek gerekebilir. (.JPG->.jpg gibi) <br>
```openalpr-utils-classifychars [countrycode] [input image directory] [empty output directory]```
<br> Örnek komut: openalpr-utils-classifychars eu font1/ output_font1/
#### Input dosyasındaki her plakanın karakterlerini sınıflandırabileceğiniz bir GUI açılınca bu adımları uygulayın:
1.1- Açılan ilk resimde enter'a basın. 
<br> 1.2- Her karakter için o karakteri klavyeden yazın. 
<br> 1.3- Boşluk tuşuna basarak fotoğrafın etrafındaki mavi çerçeveyi görün.
<br> 1.4- Bir sonraki çerçeveye geçmek için sağ ok tuşunu kullanın. 
<br> 1.5- 3. çerçeve tanımlanmadıysa 1. adıma geri dönün.
<br> 1.6- 3. çerçeve tanımlandıysa tanımlanan karakterleri kaydetmek için **S** tuşuna basın.
<br> 1.7- Bir sonraki plakaya geçmek için **n** tuşuna basın, önceki plakaya gitmek için **p** tuşuna basın.
<br> Bu işlemler tamamlandığında [linkteki](https://github.com/bur-k/476_573_plate_recognition/blob/master/output.zip) dosyaya benzer klasör ve içeriği elde edilmelidir.

### 2- .tif ve .box dosyalarını üretmek için aşağıdaki komutu çalıştırın
```openalpr-utils-prepcharsfortraining [output directory from above]```
<br> Çıktı combined.box ve combined.tif olmalıdır.
<br> 1.1- .box ve .tif dosyalarını Tesseract'ın isimlendirme kurallarına göre uzantıları değiştirmeden isimlendirin. Örnek: leu.turkey.exp0.box, leu.turkey.exp1.box
<br> 1.2- Eğitmek istediğiniz Country code ile isimlendirilmiş klasörün içindeki input klasörüne önceki adımda üretilmiş .box ve .tif dosyalarını taşıyın.
<br> Bu işlemler tamamlandığında [linkteki](https://github.com/bur-k/476_573_plate_recognition/blob/master/leu.turkey_tif_n_box_files.zip) dosyaya benzer klasör ve içeriği elde edilmelidir. 

### 3- Train etmek için aşağıdaki komutu çalıştırın
```python2 train.py [countrycode]```
<br> Not: **train.py** içerisindeki path'ler uygun şekilde ayarlanmalıdır.
<br> Çıktı 'l[countrycode].traineddata' olmalıdır.
<br> Oluşan dosya'nın path'i '/usr/share/openalpr/runtime_data/ocr/leu.traineddata' olacak şekilde ayarlanmalıdır.
<br> Bu işlemler tamamlandığında [linkteki](https://github.com/bur-k/476_573_plate_recognition/blob/master/traineddata.zip) dosyaya benzer bir dosya elde edilmelidir. 

# installation
Ubuntu 18.04.2 LTS 64bit sistem üzerinden anlatılmıştır.
<br> ```sudo apt-get update```
<br> ```sudo apt-get upgrade```
<br> ```sudo apt-get install git```
<br> ```git clone https://github.com/bur-k/476_573_plate_recognition.git```
<br> ```sudo apt-get update && sudo apt-get install -y openalpr openalpr-daemon openalpr-utils libopenalpr-dev```
<br> ```sudo ln -s /usr/share/openalpr/runtime_data//ocr/tessdata/* /usr/share/openalpr/runtime_data//ocr/```
<br> ```wget https://github.com/tesseract-ocr/tesseract/archive/4.0.0.tar.gz```
<br> extract tar.gz file
<br> ```cd tesseract-4.0.0```
<br> to build tesseract-ocr
<br> ```sudo apt-get install g++```
<br> ```sudo apt-get install autoconf automake libtool```
<br> ```sudo apt-get install pkg-config libpng-dev```
<br> ```sudo apt-get install libjpeg8-dev libtiff5-dev zlib1g-dev```
<br> to build training tools
<br> ```sudo apt-get install libicu-dev libpango1.0-dev libcairo2-dev```
<br> ```sudo apt-get install libleptonica-dev```
<br> building
<br> ```./autogen.sh```
<br> ```./configure```
<br> ```make -j4```
<br> ```sudo make install```
<br> ```sudo ldconfig```
<br> ```make training```
<br> ```sudo make training-install```

# Parametreler & Değişkenler
**plaka_tanıma.py**
<br> 38. satırdaki ```alpr.set_top_n(n)``` parametre olarak her bir plaka için bulunması gereken max tahmin sayısını almaktadır.
<br> 39. satırdaki ```plateRegEx``` değişkeni plakaların uyması gereken regex'i tutmaktadır. 
**/usr/share/openalpr/config/openalpr.defaults.conf** (Dosyada değişken açıklamaları mevcut olduğundan sadece projede değiştirilen değerler belirtilecektir.)
<br> 29. satır  ```detection_strictness = 2```
<br> 59. satır  ```analysis_count = 12```
<br> 63. satır  ```contrast_detection_threshold = 0.4```
<br> 70. satır  ```postprocess_min_confidence = 35```
<br> 74. satır  ```postprocess_confidence_skip_level = 60```
