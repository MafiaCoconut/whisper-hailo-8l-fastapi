FROM ubuntu:22.04
ENV TZ=UTC
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

LABEL authors="MafiaCoconut"

RUN mkdir /home/usr/whisper-hailo-8l-fastapi
WORKDIR /home/usr/whisper-hailo-8l-fastapi

COPY ./app ./app
COPY ./hailort_requirements_files ./hailort_requirements_files
COPY ./download_resources.sh ./download_resources.sh
COPY ./poetry.lock ./poetry.lock
COPY ./pyproject.toml ./pyproject.toml
COPY ./setup.py ./setup.py



RUN apt-get update && apt-get install -y \
    python3.11.7 \
    python3-pip \
    python3-venv \
    ffmpeg \
    libportaudio2 \
    wget \
    make


RUN dpkg --install hailort_requirements_files/hailort-pcie-driver_4.21.0_all.deb
RUN python3 setup.py
ENV PATH="/home/wyoming_hailo_whisper/.venv/bin:$PATH"
RUN pip install hailort_requirements_files/hailort-4.21.0-cp311-cp311-linux_aarch64.whll

RUN ./download_resources.sh

WORKDIR ./app

CMD ["make", "run"]