# make help: See list of commands

REPO := pk
IMAGE := vaas
TAG := latest

all:
	@make -s up

help:
	@echo "\nmake [all]:    Install dependencies and launch docker world"
	@echo "make up:       Create and enter docker world"
	@echo "make buildup:  Build image, then create and enter docker world"
	@echo "make pullup:   Pull images then compose"
	@echo "make clean:    Remove all containers"

dbuild:
	$(info Make: Building docker image)
	@docker build . --tag $(REPO)/$(IMAGE):$(TAG) --no-cache

pull:
	@docker pull $(REPO)/$(IMAGE):$(TAG)

buildup:
	@make -s dbuild
	@make -s up

pullup:
	@make -s pull
	@make -s up

up:
	@make -s compose
	@make -s stop

compose:
	$(info Make: Launching docker environment)
	@TAG=$(TAG) docker-compose up -d
	@docker logs --follow $(IMAGE)
	@make -s stop

stop:
	@docker stop $(IMAGE)

clean:
	@docker system prune --force
