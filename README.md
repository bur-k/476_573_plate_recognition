# 476_573_plate_recognition
python3 plaka_tanima.py --folder <folder_name>
folder_name should end with "/"

# installation
   54  sudo gedit /etc/apt/sources.list (add "deb http://archive.ubuntu.com/ubuntu bionic universe" to the bottom of the page)
   11  sudo apt-get update
   12  sudo apt-get upgrade
    2  sudo apt-get install git
    4  git clone https://github.com/bur-k/476_573_plate_recognition.git
    6  cd 476_573_plate_recognition/
    9  sudo apt-get update && sudo apt-get install -y openalpr openalpr-daemon openalpr-utils libopenalpr-dev
   13  sudo apt-get install libopencv-dev libtesseract-dev git cmake build-essential libleptonica-dev
   14  sudo apt-get install --assume-yes libpng12-dev libjpeg62-dev libtiff4-dev zlib1g-dev (try below if you get an error)
   18  sudo apt-get install --assume-yes libpng-dev libjpeg-turbo8-dev libtiff5-dev zlib1g-dev
   19  sudo apt-get install --assume-yes build-essential
   20  sudo apt-get install --assume-yes autoconf automake libtool
   21  sudo apt-get install --assume-yes git-core
   22  sudo apt-get install --assume-yes cmake
   26  sudo apt-get install build-essential cmake unzip pkg-config
   27  sudo apt-get install libjpeg-dev libpng-dev libtiff-dev
   35  wget https://bootstrap.pypa.io/get-pip.py
   42  sudo apt-get install python3-distutils
   45  sudo python3 get-pip.py 
   49  sudo apt-get install libopencv-dev python3-opencv
   52  sudo pip3 install opencv-python
       sudo apt-get install tesseract-ocr
       sudo apt-get install libleptonica-dev
   66  tar xf leptonica-1.78.0.tar.gz
    8  python3 plaka_tanima.py --folder araba/
