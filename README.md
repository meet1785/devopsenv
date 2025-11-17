# DevOps & MLOps Playground

Cloud-ready demo project to practice:

- GitHub Codespaces
- FastAPI-based "ML-style" API
- Docker image build
- GitHub Actions CI

## How to run in GitHub Codespaces

1. Open this repo in GitHub.
2. Click on **Code → Create codespace on main**.
3. Wait for the devcontainer to build and dependencies to install.
4. In the Codespace terminal, run:

   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

5. Use the forwarded port link to open the app in the browser.

## Example requests

### Health check

`GET /`

Response:

```json
{
  "status": "ok",
  "message": "DevOps & MLOps journey started."
}
```

### Prediction

`POST /predict`

Body:

```json
{
  "feature1": 0.6,
  "feature2": 0.3,
  "feature3": 0.8
}
```