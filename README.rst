AI4Change Yolo Device
=============================

AWK IoT Python SDK: https://github.com/aws/aws-iot-device-sdk-python
Movidius SDK: https://developer.movidius.com/start

Install AWS IoT Python SDK (from pip)
________________


.. code-block:: sh

    pip install AWSIoTPythonSDK


Install Movidius SDK (as root)
________________


.. code-block:: sh

    mkdir -p ~/movidius

    cd ~/movidius

    wget https://ncs-forum-uploads.s3.amazonaws.com/ncsdk/ncsdk-01_12_00_01-full/ncsdk-1.12.00.01.tar.gz

    tar xzf ncsdk-1.12.00.01.tar.gz

    cd ncsdk-1.12.00.01

    make install

    pip install AWSIoTPythonSDK
