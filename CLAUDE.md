# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python development environment using VS Code Dev Containers with Python 3.11. The environment includes pre-configured tools for formatting, linting, testing, and Jupyter notebook development.

## Common Commands

### Code Quality
```bash
# Format code
black .
isort .

# Lint code
flake8
pylint *.py
mypy .
```

### Testing
```bash
# Run tests
pytest

# Run tests with coverage
pytest --cov
```

### Jupyter Development
```bash
jupyter notebook
```

## Project Structure

- `.devcontainer/` - Contains Dev Container configuration, Dockerfile, and requirements.txt
- `hello.py` - Sample Python script
- `sample.csv` - Sample data file

## Development Setup

The Dev Container automatically installs all dependencies from `.devcontainer/requirements.txt` which includes:
- Formatters: black, isort
- Linters: flake8, pylint, mypy
- Testing: pytest, pytest-cov
- Jupyter: jupyter, ipykernel
- Debug tools: pdbpp, ipdb
- Other: requests, python-dotenv, sphinx

VS Code is configured to:
- Format on save
- Organize imports on save
- Use Pylint for linting
- Forward ports 8000 and 5000

## Important Notes

- Always respond in Japanese when requested (per previous instruction)
- The project uses Python 3.11-slim as base image
- All development happens in the `/workspace` directory within the container