FROM centos/python-36-centos7:latest

### -------------------------------------------------
### Metadata information
### -------------------------------------------------
LABEL name="Malachor V"
LABEL maintainer="packetferret@gmail.com"
LABEL description="nornir config backup tool"
LABEL license="GPLv2"
LABEL url="https://github.com/packetferret/malachorV"
LABEL build-date="20200218"

### -------------------------------------------------
### Install system Package
### -------------------------------------------------
USER root
RUN rm -rf /tmp/* /var/tmp/*

### -------------------------------------------------
### Change directory to /home/tmp
### -------------------------------------------------
WORKDIR /home/tmp/files

### -------------------------------------------------
### Add and install python packages
### -------------------------------------------------
ADD files/requirements.txt requirements.txt
RUN pip install -r requirements.txt

### -------------------------------------------------
### Copy local files to container
### -------------------------------------------------
COPY nornir /home/nornir

### -------------------------------------------------
### Change directory to /home/nornir
### -------------------------------------------------
WORKDIR /home/nornir

### -------------------------------------------------
### Environmentals
### -------------------------------------------------
ENV HAPPY True
ENV SHELL /bin/sh
ENV NORNIR_CORE_NUM_WORKERS 40

ENTRYPOINT [ "python", "/home/nornir/save_config.py" ]