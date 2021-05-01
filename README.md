# TensorflowLite_UBI  
Tensorflow implementation of object detections using tflite models.  
 - [Part 1: Environment setup](https://github.com/pete710592/TensorflowLite_UBI#part-1-environment-setup)  
 - [Part 2: Predict for single image](https://github.com/pete710592/TensorflowLite_UBI#part-2-predict-for-single-image)  

## Part 1: Environment setup  
This code was tested with Ubuntu 16.04 / Ubuntu 18.04 / WSL (Windows Subsystem for Linux).  
## 1-1. Update system & install requirement  
```shell
echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" | sudo tee /etc/apt/sources.list.d/coral-edgetpu.list
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
sudo apt-get update
sudo apt-get -y install python3-pip
sudo apt-get -y dist-upgrade
```  

## 1-2. Setup tensorflow-lite virtual environment & install requirement  
```shell
sudo apt-get -y install python3-venv
python3 -m venv tflite-env
echo "source tflite-env/bin/activate" >> ~/.bashrc
source ~/.bashrc
pip3 install tqdm
pip3 install --upgrade pip
pip3 install --extra-index-url https://google-coral.github.io/py-repo/ tflite_runtime
```  

## 1-3. Download this repository from GitHub  
```shell
git clone https://github.com/pete710592/TensorflowLite_UBI.git
```  
Setup requirements for tensorflow-lite.
```shell
cd TensorflowLite_UBI
bash get_pi_requirements.sh
```  

## Part 2: Predict for single image  
```shell
python3 TFLite_detection_image.py --modeldir="TFLite_model/08-daytime" --image="images/test_01.jpg"
```  
then, you will see ```08-test_01.jpg``` at ```images```.
