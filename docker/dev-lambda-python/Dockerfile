FROM python:3.12.8

WORKDIR /workspace

# Create the user
ARG USERNAME=vscode
ARG USER_UID=1234
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m -s /bin/bash $USERNAME 

# pip install
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Install less
RUN apt update  && \
    apt install less

# Install AWS CLI
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install && \
    rm awscliv2.zip && \
    rm -rf aws
