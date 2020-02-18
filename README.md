# Malachor V

![Malachor V](https://raw.githubusercontent.com/packetferret/malachorV/master/images/malachorV.jpg "Malachor V")

Malachor V is a configuration backup tool based on Nornir and wrapped in a Docker container. The configurations are stored on your local workstation, where you can opt to manage within Github for historical purposes. Each device has its own directory (stored in /backup) and the configurations are timestamped for posterity. 

`image: centos/python-36-centos7:latest`

## Operations

How to use this container

### Add your own inventory

Update the `inventory.yaml` file found in the `nornir` folder of this project. Replace the example devices with those of your own

### Update username and password

Update the `defaults.yaml` file found in the `nornir` folder of this project.

### Building the container

Clone this repository to your local machine and proceed to build the container:

`make build`

### Run the container

`make run`

Running this container will mount the backup folder from your local computer into the container, where Nornir will save the configurations locally. Simply run the command whenver you want a backup of your network, or place it in your crontab with an appropriate candence for automating the execution
