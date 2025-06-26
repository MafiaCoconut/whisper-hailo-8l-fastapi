FROM ubuntu:24.04
ENV TZ=UTC
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

LABEL authors="MafiaCoconut"


RUN apt-get update && apt-get install -y \
    # python3.11 \
    # python3-pip \
    # python3-venv \
    build-essential \
    libssl-dev \
    zlib1g-dev \
    libreadline-dev \
    libsqlite3-dev \
    libffi-dev \
    liblzma-dev \
    wget \
    curl \
    llvm \
    libncursesw5-dev \
    xz-utils \
    tk-dev \
    libxml2-dev \
    libxmlsec1-dev \
    libbz2-dev \
    ffmpeg \
    libportaudio2 \
    wget \
    make \
    git
    

# RUN git clone https://github.com/pyenv/pyenv.git .pyenv
    # ENV PYENV_ROOT="$/root/.pyenv"
    # ENV PATH="${PYENV_ROOT}/shims:${PYENV_ROOT}/bin:${PATH}"
# ENV HOME=/home/python_user
# ENV PYENV_ROOT=$HOME/.pyenv
# ENV PATH=$PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH

# RUN curl https://pyenv.run | bash

# RUN /bin/bash -c "export PYENV_ROOT=\"$PYENV_ROOT\" && export PATH=\"$PYENV_ROOT/bin:$PYENV_ROOT/shims:$PATH\" && \
#     pyenv install ${PYTHON_VERSION} && pyenv global ${PYTHON_VERSION}"
# ENV PYENV_ROOT="/root/.pyenv"
# ENV PATH="$PYENV_ROOT/bin:$PYENV_ROOT/shims:$PATH"
# RUN git clone --depth 1 https://github.com/pyenv/pyenv.git 

# RUN pyenv/.pyenv
RUN curl https://pyenv.run | bash
ENV PATH="/root/.pyenv/bin:/root/.pyenv/shims:${PATH}"
RUN echo 'eval "$(pyenv init --path)"' >> ~/.bashrc


ENV PYTHON_VERSION=3.11.9
RUN pyenv install ${PYTHON_VERSION}
RUN pyenv global ${PYTHON_VERSION}

RUN pip install poetry

RUN mkdir /home/usr
RUN mkdir /home/usr/whisper-hailo-8l-fastapi
WORKDIR /home/usr/whisper-hailo-8l-fastapi

COPY ./app ./app
COPY ./hailort_requirements_files ./hailort_requirements_files
COPY ./download_resources.sh ./download_resources.sh
COPY ./poetry.lock ./poetry.lock
COPY ./pyproject.toml ./pyproject.toml
COPY ./setup.py ./setup.py

RUN poetry install


RUN dpkg --unpack hailort_requirements_files/hailort-pcie-driver_4.21.0_all.deb
RUN dpkg --unpack hailort_requirements_files/hailort_4.21.0_arm64.deb

# COPY ./app ./app
# COPY ./hailort_requirements_files ./hailort_requirements_files
# COPY ./download_resources.sh ./download_resources.sh
# COPY ./poetry.lock ./poetry.lock
# COPY ./pyproject.toml ./pyproject.toml
# COPY ./setup.py ./setup.py



ENV PATH="/home/wyoming_hailo_whisper/.venv/bin:$PATH"
RUN poetry run pip install hailort_requirements_files/hailort-4.21.0-cp311-cp311-linux_aarch64.whl

RUN ./download_resources.sh

WORKDIR ./app

CMD ["make", "run"]