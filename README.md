# 🏥 OSM Health Check

This repository contains a project for monitoring the health status of Open Source MANO (OSM). Through an API, it exposes the operational status of the different services that are part of OSM.

## 📋 Table of Contents

- [🏥 OSM Health Check](#-osm-health-check)
  - [📋 Table of Contents](#-table-of-contents)
  - [⚙️ Prerequisites](#️-prerequisites)
    - [Test Environment](#test-environment)
    - [Configuring `pre-commit`](#configuring-pre-commit)
  - [📝 TODO](#-todo)

## ⚙️ Prerequisites

Before getting started with OSM Health Check, ensure your development environment meets the following requirements and has the necessary tools configured.

### Test Environment

The project has been validated and tested with the following component versions:

| **Component** | **Version** |
| ------------- | ----------- |
| `python -V`   | `3.14+`     |

### Configuring `pre-commit`

Install the development dependencies from `pyproject.toml` which includes `pre-commit`. The `pre-commit` configuration is designed to enforce that all commit messages follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification.

> [!TIP]
> The following commands should be executed within a Python virtual environment.

```bash
poetry install --with dev
pre-commit autoupdate
pre-commit install --hook-type commit-msg --hook-type pre-push
```

## 📝 TODO

- Create a "How to Contribute?" section following the guidelines of a `CONTRIBUTING.md` file.
- Create a "Contact" section.
- Create a `LICENSE` file and associate it with the `pyproject.toml` file for the project.
