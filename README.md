# FreshCart Pipelines

End-to-end Data Engineering assignment covering Git, CI/CD, FreshCart ELT on Snowflake, Mage Iris ML, and RabbitMQ event streaming.

## Project Structure

- `elt/` - FreshCart ELT pipeline and supporting SQL
- `iris_project/` - Mage Iris ML pipeline
- `stream/` - RabbitMQ dispatcher and driver
- `tests/` - Automated tests
- `.github/workflows/` - GitHub Actions CI workflow

## Technologies

- Python
- Git and GitHub
- Snowflake and SQL
- Mage
- RabbitMQ
- pytest

## Setup

Use Python 3.12.

### Windows

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest -q


## Author

Mohammed Zaki Malick

## Important

Never commit passwords, API keys, `.env` files, or other credentials.
