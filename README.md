# Sunairio Add API

Simple REST API that adds two integers. Built as a take-home task.

**Endpoint:**  
`GET /add?left=5&right=2` → `200 OK` + `{"sum": 7}`

## Features
- Python + Flask web server
- Query parameters validation (required, integers only)
- Basic input sanitization & error handling
- Sanity check for excessive query parameters (prevents potential abuse)
- Unit tests with pytest
- Dockerized (multi-stage build for small image)
- CI pipeline with GitHub Actions: tests → build → push to GHCR

## Tech Stack
- Python 3.11
- Flask
- pytest
- Docker
- GitHub Actions + GHCR (GitHub Container Registry)

## Run locally

```bash
docker pull ghcr.io/veljko-milosavljevic/sunairio:latest
docker run -p 5000:5000 ghcr.io/veljko-milosavljevic/sunairio:latest

# Test
curl "http://localhost:5000/add?left=6&right=3"   # → {"sum":9}
