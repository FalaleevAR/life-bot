.PHONY: help build deploy-ecr deploy

.DEFAULT: help

help:
	@echo "make build"
	@echo "     build docker"
	@echo "make run"
	@echo "     run docker"
	@echo "make deploy-ecr"
	@echo "     deploy to AWS ECR"
	@echo "make deploy"
	@echo "     build, deploy to ECR, deploy to ElasticBeanstalk"

build:
	docker build -t life_bot .

deploy-ecr: build
	aws ecr get-login-password --region eu-central-1 | docker login --username AWS --password-stdin 317869137751.dkr.ecr.eu-central-1.amazonaws.com
	docker tag life_bot:latest 317869137751.dkr.ecr.eu-central-1.amazonaws.com/life_bot:latest
	docker push 317869137751.dkr.ecr.eu-central-1.amazonaws.com/life_bot:latest

deploy: deploy-ecr
	eb deploy

