AI4Change Yolo Device
=============================
It this repository you will find the code used directly on Rapsberry Pi with a Intel Movidius Neural Stick. For the backend/cloud component of the solution, see ai4change-yolo-backend repository.

The workflow of the solution is following:

1. RaspberryPi and Intel Movidius are used to recognize an item seen by a camera.

2. The name of recognized item is sent to AWS via MQTT (using "products" topic).

3. On AWS the recommendation is generated (using AWS Lambda).

4. The recommendation is sent back to RaspberryPi via MQTT (using "advice" topic).

5. Based on the reciveded recommendation, the image is displayed on the screen.

For deployment instructions see below.

## Screen
![Alt text](https://github.com/ai4change-yolo/ai4change-yolo-device/blob/master/_graphics/img1.jpg)

Install needed python libraries (from pip)
________________


.. code-block:: sh

    pip install AWSIoTPythonSDK
    pip install configparser
    pip install imutils
    pip install picamera
    pip install opencv-python


Install Movidius SDK (as root)
________________


.. code-block:: sh

    mkdir -p ~/movidius

    cd ~/movidius

    wget https://ncs-forum-uploads.s3.amazonaws.com/ncsdk/ncsdk-01_12_00_01-full/ncsdk-1.12.00.01.tar.gz

    tar xzf ncsdk-1.12.00.01.tar.gz

    cd ncsdk-1.12.00.01

    make install

    make examples


Troubleshooting
________________


If error while example compilation:

*RuntimeError: module compiled against API version 0xb but this version of numpy is 0xa*

Upgrade numpy package:

.. code-block:: sh

    pip3 install --upgrade numpy


Links
________________


AWK IoT Python SDK: https://github.com/aws/aws-iot-device-sdk-python

Movidius SDK: https://developer.movidius.com/start

Real-time object detection on the Raspberry Pi with the Movidius NCS: https://www.pyimagesearch.com/2018/02/19/real-time-object-detection-on-the-raspberry-pi-with-the-movidius-ncs/

Deploying Your Customized Caffe Models on Intel® Movidius™ Neural Compute Stick: https://movidius.github.io/blog/deploying-custom-caffe-models/
