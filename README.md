# 476_573_plate_recognition
python3 plaka_tanima.py --folder <folder_name>
folder_name should end with "/"

# installation
<br>   54  sudo gedit /etc/apt/sources.list (add "deb http://archive.ubuntu.com/ubuntu bionic universe" to the bottom of the page)
<br>   11  sudo apt-get update
<br>   12  sudo apt-get upgrade
<br>    2  sudo apt-get install git
<br>    4  git clone https://github.com/bur-k/476_573_plate_recognition.git
<br>    6  cd 476_573_plate_recognition/
<br>    9  sudo apt-get update && sudo apt-get install -y openalpr openalpr-daemon openalpr-utils libopenalpr-dev
<br>   13  sudo apt-get install libopencv-dev libtesseract-dev git cmake build-essential libleptonica-dev
<br>   14  sudo apt-get install --assume-yes libpng12-dev libjpeg62-dev libtiff4-dev zlib1g-dev (try below if you get an error)
<br>   18  sudo apt-get install --assume-yes libpng-dev libjpeg-turbo8-dev libtiff5-dev zlib1g-dev
<br>   19  sudo apt-get install --assume-yes build-essential
<br>   20  sudo apt-get install --assume-yes autoconf automake libtool
<br>   21  sudo apt-get install --assume-yes git-core
<br>   22  sudo apt-get install --assume-yes cmake
<br>   26  sudo apt-get install build-essential cmake unzip pkg-config
<br>   27  sudo apt-get install libjpeg-dev libpng-dev libtiff-dev
<br>   35  wget https://bootstrap.pypa.io/get-pip.py
<br>   42  sudo apt-get install python3-distutils
<br>   45  sudo python3 get-pip.py 
<br>   49  sudo apt-get install libopencv-dev python3-opencv
<br>   52  sudo pip3 install opencv-python
<br>       sudo apt-get install tesseract-ocr
<br>       sudo apt-get install libleptonica-dev
<br>   66  tar xf leptonica-1.78.0.tar.gz
<br>    8  python3 plaka_tanima.py --folder araba/
