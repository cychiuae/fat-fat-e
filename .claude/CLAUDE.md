# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
make setup      # Install dependencies (uv sync)
make format     # Format code with Ruff
make lint       # Run Ruff linter
make typecheck  # Run MyPy with Pydantic plugin
make secrets    # Copy .env.example to .env
python main.py  # Run application
```

## Architecture

Python 3.14 application using UV for package management.

- `fatfate/` - Main package, exports `main()` entry point
- `fatfate/settings/` - Pydantic Settings configuration, loads from `.env` file
- `main.py` - Application entry point with logging setup

## Code Style

- Formatter/Linter: Ruff
- Type checker: MyPy with Pydantic plugin
- Use type hints on all functions
