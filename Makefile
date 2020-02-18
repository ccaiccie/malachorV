DOCKER_IMG = packetferret/malachorv
DOCKER_TAG = latest

build:
	docker build -t $(DOCKER_IMG):$(DOCKER_TAG) .

run:
	docker run -i \
	--name nornir_backup \
	-v ${PWD}/backup:/home/nornir/backup:z \
	--rm \
	$(DOCKER_IMG):$(DOCKER_TAG)
