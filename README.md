# Whisper+Hailo-8 Microservice on FastApi 
### Modification of the [Speech Recognition](https://github.com/hailo-ai/Hailo-Application-Code-Examples/tree/main/runtime/hailo-8/python/speech_recognition) from [Hailo Application Code Examples](https://github.com/hailo-ai/Hailo-Application-Code-Examples/tree/main)

It was created and tested on:
- Raspberry Pi 5 8Gb ORM 
- Ubuntu Server 25.04
- HailoRT v4.21
- Hailo8L

### Requirements
- Hailo8 / Hailo8L
- HailoRT 4.21 (not tested on 4.20)
- HailoRT PCIe driver
- PyHailoRT (.whl file; Can be downloaded https://hailo.ai/developer-zone/software-downloads; You need file HailoRT – Python package (whl) for Python 3.11, aarch64)
- Python 3.11.*
- Poetry 

### Pre-Installation
IMPORTANT STEP

You need to install all requirements from official documentation.

Some files from the `developer-zone` that need to be installed are located in hailort_requirements_files folder

https://hailo.ai/developer-zone/documentation/hailort-v4-21-0/?sp_referrer=install/install.html

### Installation
1. Clone repository
    ```shell
    git clone https://github.com/MafiaCoconut/whisper-hailo-8l-fastapi.git
    cd whisper-hailo-8l-fastapi
    ```

2. Run the setup script
    ```shell
    python3 setup.py
    ```
   
3. Activate environment 
    ```shell
    source .venv/bin/activate
    ```

4. Install .whl in environment
    ```shell
    pip install hailort_requirements_files/hailort-4.21.0-cp311-cp311-linux_aarch64.whl
    ```
   
    The PyHailoRT version must match the installed HailoRT version. NOTE: This step is not necessary for Raspberry Pi 5 users who installed the hailo-all package, since the venv will inherit the system package.

### Run
#### Docker-compose
Using docker-compose instead of Docker will make it much easier to launch the service.

1. If you have "Hailo-8" you need to open docker-compose.yaml and change ENV value `HAILO_VERSION`

2. Run service
    ```shell
    docker-compose up --build
    ```



#### Local
1. Change .env file
    ```
    IS_HAILO_ON_DEVICE="TRUE" # if you want to run service not it RP5, you need to change this value on "FALSE"
    HAILO_VERSION="HAILO8L" # This value can be only "HAILO8L" or "HAILO8"
    ```

2. In file app/application/pipelines/hailo_whisper_pipeline you need to comment out `line 11`
    ```
    from hailo_platform import (HEF, VDevice, HailoSchedulingAlgorithm, FormatType)
    ```

3. Run service
    ```shell
    make run
    ```


### EXTRA

If you need another .deb and .whl files, you can add them in hailort_requirements_files folder and change pathes

Here is also simple example of how to send voice_files to this service
    
```py
import requests

url = "http://<device-host>:10300/transcribe"
files = {'file': open('male.wav', 'rb')}
resp = requests.post(url, files=files)
print(resp.json())
```

If you have this error, you should reinstall your .venv, because something went wrong due to your installation/configuration
```
[] [] [HailoRT] [error] [infer_model.cpp:868] [validate_bindings] CHECK failed - Input buffer size 0 is different than expected 320000 for input 'tiny-whisper-encoder-10s/input_layer1'
[] [] [HailoRT] [error] [infer_model.cpp:932] [run_async] CHECK_SUCCESS failed with status=HAILO_INVALID_OPERATION(6)
[] [] [HailoRT] [info] [async_infer_runner.cpp:86] [shutdown] Pipeline was aborted. Shutting it down
[] [] [HailoRT] [error] [infer_model.cpp:651] [run_async] CHECK_SUCCESS failed with status=HAILO_INVALID_OPERATION(6)
```
