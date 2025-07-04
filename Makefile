run:
SHELL := /bin/bash

DOTENV := .env

.PHONY: run

run:
	cd app && poetry run uvicorn main:app --port 54322 --host 0.0.0.0 --log-config infrastructure/config/logging_config.json
