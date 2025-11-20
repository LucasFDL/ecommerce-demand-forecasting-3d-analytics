from pathlib import Path

# Root do projeto (arquivo config.py está em src/)
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Pastas de dados
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# Pastas de reports
REPORTS_DIR = PROJECT_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"
TABLES_DIR = REPORTS_DIR / "tables"
