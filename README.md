<<<<<<< HEAD
# FreshCart Pipelines

End-to-end Data Engineering assignment: Git/CI, FreshCart ELT on Snowflake,
Mage Iris ML pipeline, and RabbitMQ event streaming.

## Project structure

- `elt/` — FreshCart Snowflake ELT notebook and supporting SQL.
- `iris_project/` — Mage Iris ML pipeline.
- `stream/` — RabbitMQ dispatcher and driver.
- `tests/` — automated tests.
- `.github/workflows/ci.yml` — GitHub Actions CI workflow.

## Setup

Use Python 3.12.

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\\Scripts\\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest -q
```

Do not commit credentials, `.env` files, generated CSV files, model files, or logs.
See `.gitignore`.
=======
# freshcart-pipelines
>>>>>>> 806ffc2b15e355cffbfae685eca4346ac880e7a0
