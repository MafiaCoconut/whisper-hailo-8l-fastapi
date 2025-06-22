run:
SHELL := /bin/bash

DOTENV := .env

.PHONY: run

run:
	cd app && poetry run uvicorn main:app --reload --port 10300 --log-config infrastructure/config/logging_config.json

run\:ngrok:
	@export $$(grep -v '^\s*#' $(DOTENV) | xargs) && \
	ngrok http --url=chief-mosquito-eagerly.ngrok-free.app --authtoken $$NGROK_TOKEN 8000