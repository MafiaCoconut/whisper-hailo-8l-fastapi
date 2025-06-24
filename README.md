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

### Pre-Installation
IMPORTANT STEP

You need to install all requirements from official documentation.

https://hailo.ai/developer-zone/documentation/hailort-v4-21-0/?sp_referrer=install/install.html

### Installation
1. Clone repository
    ```shell
    git clone <>
    cd <>
    ```

2. Copy hailort-<version>-cp31<>-cp31<>-linux_<>.whl file in repository
    ```shell 
    cp hailort-<version>-cp31<>-cp31<>-linux_<>.whl <>/hailort-<version>-cp31<>-cp31<>-linux_<>.whl
    ```

3. Run the setup script
    ```shell
    python3 setup.py
    ```
   
4. Activate environment 
    ```shell
    source .venv/bin/activate
    ```

5. Install .whl in environment
    ```shell
    pip install hailort-<version>-cp31<>-cp31<>-linux_<>.whl
    ```
   
    The PyHailoRT version must match the installed HailoRT version. NOTE: This step is not necessary for Raspberry Pi 5 users who installed the hailo-all package, since the venv will inherit the system package.


6. For local you can use Makefile commands

