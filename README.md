# 476_573_plate_recognition
preprocessing olarak input olarak verilecek folder'ın içerisinde bir kereliğine terminal üzerinden **mogrify -resize 200X200 .\*.** komutunu çalıştırın.
python3 plaka_tanima.py --folder <folder_name>
folder_name should end with "/"

## OCR-Training adımları
Hazırlık: git clone https://github.com/openalpr/train-ocr
### 1- Karakter sınıflandırmak için aşağıdaki komutu çalıştırın
<br> openalpr-utils-classifychars [countrycode] [input image directory] [empty output directory]
<br> Örnek komut: openalpr-utils-classifychars eu font1/ output_font1/
#### Input dosyasındaki her plakanın karakterlerini sınıflandırabileceğiniz bir GUI açılınca bu adımları uygulayın:
<br> 1.1- Açılan ilk resimde enter'a basın. 
<br> 1.2- Her karakter için o karakteri klavyeden yazın. 
<br> 1.3- Boşluk tuşuna basarak fotoğrafın etrafındaki mavi çerçeveyi görün.
<br> 1.4- Bir sonraki çerçeveye geçmek için sağ ok tuşunu kullanın. 
<br> 1.5- 3. çerçeve tanımlanmadıysa 1. adıma geri dönün.
<br> 1.6- 3. çerçeve tanımlandıysa tanımlanan karakterleri kaydetmek için 'S' tuşuna basın.
<br> 1.7- Bir sonraki plakaya geçmek için 'n' tuşuna basın, önceki plakaya gitmek için'p' tuşuna basın.

### 2- .tif ve .box dosyalarını üretmek için aşağıdaki komutu çalıştırın
<br> openalpr-utils-prepcharsfortraining [output directory from above]
<br> Çıktı combined.box ve combined.tif olmalıdır.
<br> 1.1- .box ve .tif dosyalarını Tesseract'ın isimlendirme kurallarına göre uzantıları değiştirmeden isimlendirin. Örnek :    leu.turkey.exp0.box, leu.turkey.exp1.box
<br> 1.2- Eğitmek istediğiniz Country code ile isimlendirilmiş klasörün içindeki input klasörüne önceki adımda ür
etilmiş .box ve .tif dosyalarını taşıyın.

### 3- Train etmek için aşağıdaki komutu çalıştırın
<br> python2 train.py [countrycode]
<br> Çıktı 'l[countrycode].traineddata' olmalıdır.
<br> Oluşan dosya'nın path'i '/usr/share/openalpr/runtime_data/ocr/leu.traineddata' olacak şekilde ayarlanmalıdır.

# installation
Ubuntu 18.04.2 LTS 64bit sistem üzerinden anlatılmıştır.
<br>- sudo apt-get update
<br>- sudo apt-get upgrade 
<br>- sudo apt-get install git
<br>- git clone https://github.com/bur-k/476_573_plate_recognition.git
<br>- sudo apt-get update && sudo apt-get install -y openalpr openalpr-daemon openalpr-utils libopenalpr-dev
<br>- sudo ln -s /usr/share/openalpr/runtime_data//ocr/tessdata/* /usr/share/openalpr/runtime_data//ocr/
<br>- wget https://github.com/tesseract-ocr/tesseract/archive/4.0.0.tar.gz
<br># extract tar.gz file
<br>- cd tesseract-4.0.0
<br># to build tesseract-ocr
<br>- sudo apt-get install g++
<br>- sudo apt-get install autoconf automake libtool
<br>- sudo apt-get install pkg-config libpng-dev
<br>- sudo apt-get install libjpeg8-dev libtiff5-dev zlib1g-dev
<br># to build training tools
<br>- sudo apt-get install libicu-dev libpango1.0-dev libcairo2-dev
<br>- sudo apt-get install libleptonica-dev
<br># building
<br>- ./autogen.sh
<br>- ./configure
<br>- make -j4
<br>- sudo make install
<br>- sudo ldconfig
<br>- make training
<br>- sudo make training-install
