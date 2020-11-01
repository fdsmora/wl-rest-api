FAUSTO_IMAGE=faustodsm/wz-rest-api:main

all: help

run-app: ## Starts the microservice in localhost:5000 on Docker on your localhost 
	@echo "+ $@"
	@docker run --rm -d -p 5000:5000 ${FAUSTO_IMAGE}

hello-world: ## Test the simple 'Hello, world!' endpoint
	@echo "+ $@"
	@curl http://localhost:5000/hello
 
weather: ## Test the weather report per city. Usage: make city=<your city> weather
	@echo "+ $@"
	@curl http://localhost:5000/weather/${city}/

help:
	@echo "Before testing make sure you run 'make run-app' to start the microservice"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
