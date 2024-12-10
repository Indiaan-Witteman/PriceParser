# PriceParser 🚀

Welcome to **PriceParser**, an advanced tool designed to parse and extract pricing information with precision and efficiency. This project is tailored to meet the needs of developers looking to handle and process pricing data seamlessly.

Build for the Automation Group by Leo Hanhart for the job interview assigment.
---

## Table of Contents 📚


- [Introduction](#introduction)
- [Key Features](#key-features)
- [Dependencies](#dependencies)
- [Run with Docker](#run-with-docker-)
- [Run with Docker Compose](#run-with-docker-compose-)
- [Run without Docker](#run-without-docker-)

---


## Introduction

**PriceParser** is built to streamline the process of extracting and delivering pricing data across various systems. Whether you're integrating with external sources, processing raw data, or building dashboards, PriceParser provides a robust framework to handle these tasks efficiently.

---

## Key Features 🌟

- **Parses Price Out Of Plain Text**: Designed to handle unstructured data efficiently.
- **Docker Support**: Simplified deployment with containerization.
- **Easy-to-Use Interface**: Straightforward setup and execution process.

---

## Dependencies 📦

Ensure you have the following installed:

- Python 3.11+
- Docker (for containerized runs)
- Docker Compose (for Docker Compose runs)

---

## Run with Docker 🐳

**Build the Docker Image:**
```bash
docker build -t price-parser .
docker run -p 8050:8050 --name price-parser price-parser
```
Access the Application: Open your browser and navigate to http://localhost:8050.

Stop the Container: To stop the container, run:

```bash
docker stop price-parser
```

Remove the Container: If you want to remove the container, run:

```bash
docker rm price-parser
```

## Run with Docker Compose 🐳

If a `docker-compose.yml` is already included in the project:

**Start the Service:**
```bash
docker-compose --env-file .env up --build
```
Access the Application: Open your browser and navigate to http://localhost:8050.


## Run without Docker 🖥️
```bash
docker rm price-parser
```
Clone the Repository:

```bash

git clone https://github.com/your-repo/PriceParser.git
cd PriceParser
```
Set Up a Virtual Environment:

```bash

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
Install Dependencies:

```bash

pip install -e .
```
Run the Application:

```bash
python src/PriceParser/services/parser_demo.py
Access the Application: Open your browser and navigate to http://localhost:8050.
```

credits to : Leo Hanhart.
Build for the automation groupe
