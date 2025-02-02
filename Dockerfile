# FROM nvidia/cuda:12.2.2-cudnn8-runtime-ubuntu22.04

# ENV PYTHON_VERSION=3.12 \
#     DEBIAN_FRONTEND=noninteractive

# # Install Python 3.12 and system dependencies
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     software-properties-common \
#     && add-apt-repository ppa:deadsnakes/ppa -y \
#     && apt-get install -y \
#     python${PYTHON_VERSION} \
#     python${PYTHON_VERSION}-dev \
#     python${PYTHON_VERSION}-venv \
#     build-essential \
#     # Create symbolic links
#     && ln -sf /usr/bin/python${PYTHON_VERSION} /usr/bin/python3 \
#     && ln -sf /usr/bin/python3 /usr/bin/python \
#     # Install pip directly using ensurepip
#     && python3 -m ensurepip --upgrade \
#     # Add pip to PATH
#     && ln -s /usr/local/bin/pip3 /usr/bin/pip \
#     && apt-get clean \
#     && rm -rf /var/lib/apt/lists/*

# WORKDIR /app

# # Copy model directory first to leverage Docker cache
# COPY insightface_model/ /app/insightface_model/
# # Set environment variable for model path
# ENV INSIGHTFACE_MODEL_DIR=/app/insightface_model

# COPY requirements.txt .

# # Use Python module syntax for pip
# RUN python3 -m pip install --no-cache-dir --upgrade pip \
#     && python3 -m pip install --no-cache-dir -r requirements.txt

# COPY . .
# EXPOSE 8501
# # CMD ["streamlit", "run", "src/main.py", "--server.port=8501", "--server.address=0.0.0.0"]
# CMD ["streamlit", "run", "src/login.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.sslCertFile=/app/server.crt", "--server.sslKeyFile=/app/server.key"]
# FROM nvidia/cuda:12.8.0-cudnn-runtime-ubuntu22.04

# ENV PYTHON_VERSION=3.12 \
#     DEBIAN_FRONTEND=noninteractive

# # Install Python 3.12 and system dependencies
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     software-properties-common \
#     && add-apt-repository ppa:deadsnakes/ppa -y \
#     && apt-get install -y \
#     python${PYTHON_VERSION} \
#     python${PYTHON_VERSION}-dev \
#     python${PYTHON_VERSION}-venv \
#     build-essential \
#     # Create symbolic links
#     && ln -sf /usr/bin/python${PYTHON_VERSION} /usr/bin/python3 \
#     && ln -sf /usr/bin/python3 /usr/bin/python \
#     # Install pip directly using ensurepip
#     && python3 -m ensurepip --upgrade \
#     # Add pip to PATH
#     && ln -s /usr/local/bin/pip3 /usr/bin/pip \
#     && apt-get clean \
#     && rm -rf /var/lib/apt/lists/*

# WORKDIR /app

# # Copy model directory first to leverage Docker cache
# COPY insightface_model/ /app/insightface_model/
# # Set environment variable for model path
# ENV INSIGHTFACE_MODEL_DIR=/app/insightface_model

# COPY requirements.txt .

# # Install dependencies and Streamlit
# RUN python3 -m pip install --no-cache-dir --upgrade pip \
#     && python3 -m pip install --no-cache-dir -r requirements.txt \
#     && python3 -m pip install --no-cache-dir streamlit

# COPY . .

# # Set CUDA environment variables
# ENV CUDA_HOME=/usr/local/cuda
# ENV LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
# ENV PATH=/usr/local/cuda/bin:$PATH

# EXPOSE 8501

# CMD ["streamlit", "run", "src/login.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.sslCertFile=/app/server.crt", "--server.sslKeyFile=/app/server.key"]
FROM nvidia/cuda:12.8.0-cudnn-runtime-ubuntu22.04

ENV PYTHON_VERSION=3.12 \
    DEBIAN_FRONTEND=noninteractive

# Install Python 3.12 and system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    software-properties-common \
    curl \
    ca-certificates \
    build-essential \
    && add-apt-repository ppa:deadsnakes/ppa -y \
    && apt-get install -y \
    python${PYTHON_VERSION} \
    python${PYTHON_VERSION}-dev \
    python${PYTHON_VERSION}-venv \
    && ln -sf /usr/bin/python${PYTHON_VERSION} /usr/bin/python3 \
    && ln -sf /usr/bin/python3 /usr/bin/python \
    && python3 -m ensurepip --upgrade \
    && ln -s /usr/local/bin/pip3 /usr/bin/pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy model directory first to leverage Docker cache
COPY insightface_model/ /app/insightface_model/
# Set environment variable for model path
ENV INSIGHTFACE_MODEL_DIR=/app/insightface_model

COPY requirements.txt .

# Install dependencies and Streamlit
RUN python3 -m pip install --no-cache-dir --upgrade pip \
    && (for i in {1..5}; do python3 -m pip install --no-cache-dir --timeout=300 -r requirements.txt && break || sleep 15; done) \
    && python3 -m pip uninstall -y onnxruntime-gpu \
    && python3 -m pip install --no-cache-dir onnxruntime-gpu==1.20.1

COPY . .

# Set CUDA environment variables
ENV CUDA_HOME=/usr/local/cuda
ENV LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
ENV PATH=/usr/local/cuda/bin:$PATH

EXPOSE 8501

CMD ["streamlit", "run", "src/login.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.sslCertFile=/app/server.crt", "--server.sslKeyFile=/app/server.key"]
