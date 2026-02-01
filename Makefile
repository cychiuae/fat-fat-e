.PHONY: setup
setup:
	uv sync

.PHONY: secrets
secrets:
	cp .env.example .env

.PHONY: format
format:
	uv run ruff format .

.PHONY: lint
lint:
	uv run ruff check
