FROM ubuntu

RUN apt-get update \
&& apt-get -y install sshpass \
&& apt-get install -y python3 \
&& apt install -y python3-pip \
&& pip install --no-input google-cloud-storage

# Creating Application Source Code Directory
RUN mkdir -p /k8s_python/src

# Setting Home Directory for containers
WORKDIR /k8s_python/src

# Copying src code to Container
COPY . /k8s_python/src

# Application Environment variables
ENV APP_ENV development

# Setting Persistent data
VOLUME ["/app-data"]

# Running Python Application
CMD ["python3", "controller.py"]
