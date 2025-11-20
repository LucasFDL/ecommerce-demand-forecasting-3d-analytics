from pathlib import Path
import pandas as pd
from src.config import PROCESSED_DATA_DIR


def basic_cleaning(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply initial cleaning steps:
    - standardize column names
    - remove duplicates
    """
    df = df.copy()
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
    df = df.drop_duplicates()
    return df


def save_processed(df: pd.DataFrame, filename: str, as_parquet: bool = True) -> Path:
    """
    Save a processed dataset to data/processed as parquet (default) or CSV.
    """
    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
    filepath = PROCESSED_DATA_DIR / filename

    if as_parquet:
        if filepath.suffix != ".parquet":
            filepath = filepath.with_suffix(".parquet")
        df.to_parquet(filepath, index=False)
    else:
        if filepath.suffix != ".csv":
            filepath = filepath.with_suffix(".csv")
        df.to_csv(filepath, index=False)

    return filepath