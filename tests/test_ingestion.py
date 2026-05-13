"""
Tests for src/ingestion.py -- Phase 1.

Run with: pytest tests/test_ingestion.py -v
"""
import pytest
import pandas as pd
from src.ingestion import load_file, normalise_columns, parse_amount_column, validate_schema


def test_normalise_columns_lowercases():
    df = pd.DataFrame(columns=['Invoice Amount', 'Vendor ID', 'Date'])
    result = normalise_columns(df)
    assert list(result.columns) == ['invoice_amount', 'vendor_id', 'date']


def test_normalise_columns_strips_whitespace():
    df = pd.DataFrame(columns=['  amount  ', ' vendor '])
    result = normalise_columns(df)
    assert 'amount' in result.columns
    assert 'vendor' in result.columns


def test_validate_schema_passes_when_columns_present():
    df = pd.DataFrame(columns=['amount', 'vendor_id', 'date'])
    validate_schema(df, ['amount', 'vendor_id'])


def test_validate_schema_raises_on_missing_column():
    df = pd.DataFrame(columns=['amount'])
    with pytest.raises(ValueError, match='vendor_id'):
        validate_schema(df, ['amount', 'vendor_id'])


def test_parse_amount_strips_currency_symbols():
    df = pd.DataFrame({'amount': ['$1,234.56', '$500.00']})
    cleaned, errors = parse_amount_column(df, 'amount')
    assert cleaned['amount'].tolist() == pytest.approx([1234.56, 500.0])
    assert len(errors) == 0


def test_parse_amount_handles_accounting_negatives():
    df = pd.DataFrame({'amount': ['(500.00)', '$200.00']})
    cleaned, errors = parse_amount_column(df, 'amount')
    assert cleaned['amount'].iloc[0] == pytest.approx(-500.0)


def test_parse_amount_flags_unparseable_rows():
    df = pd.DataFrame({'amount': ['$100.00', 'not_a_number', '']})
    cleaned, errors = parse_amount_column(df, 'amount')
    assert len(errors) > 0


def test_load_file_raises_for_missing_path():
    with pytest.raises(FileNotFoundError):
        load_file('data/sample/does_not_exist.csv')


def test_load_file_raises_for_unsupported_extension():
    with pytest.raises(ValueError):
        load_file('data/sample/file.txt')
