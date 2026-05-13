@'
import pandas as pd
from pathlib import Path


def load_file(filepath) -> pd.DataFrame:
    """
    Load a CSV or Excel file into a DataFrame.
    Raise FileNotFoundError if the path does not exist.
    Raise ValueError if the extension is not .csv, .xlsx, or .xls.
    """
    raise NotImplementedError


def normalise_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Lowercase, strip whitespace, replace spaces with underscores."""
    raise NotImplementedError


def parse_amount_column(df: pd.DataFrame, column: str) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Strip $, handle (500.00) negatives. Return (cleaned_df, error_df)."""
    raise NotImplementedError


def validate_schema(df: pd.DataFrame, required_columns: list[str]) -> None:
    """Raise ValueError listing missing columns."""
    raise NotImplementedError