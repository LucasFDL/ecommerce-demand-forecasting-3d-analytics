from pathlib import Path

import pandas as pd

from src.config import PROCESSED_DATA_DIR, RAW_DATA_DIR


def load_raw_data(filename: str) -> pd.DataFrame:
    """
    Load a raw CSV file from data/raw.
    """
    filepath = RAW_DATA_DIR / filename
    return pd.read_csv(filepath)


def load_processed_data(filename: str) -> pd.DataFrame:
    """
    Load a processed CSV or Parquet file from data/processed.
    """
    filepath = PROCESSED_DATA_DIR / filename

    if filepath.suffix == ".parquet":
        return pd.read_parquet(filepath)

    return pd.read_csv(filepath)
