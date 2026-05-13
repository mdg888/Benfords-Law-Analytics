"""
Tests for src/detectors.py -- Phases 5 & 6.

Run with: pytest tests/test_detectors.py -v
"""
import pytest
import pandas as pd
from src.detectors import (
    find_exact_duplicates,
    find_near_duplicates,
    detect_round_numbers,
    round_number_rate,
)


def _sample_df():
    return pd.DataFrame({
        'amount': [1000.0, 1000.0, 500.0, 1247.83, 9999.0, 5000.0, 250.0],
        'vendor_id': ['V001', 'V001', 'V002', 'V003', 'V001', 'V002', 'V003'],
        'date': pd.to_datetime([
            '2024-01-10', '2024-01-10', '2024-02-01',
            '2024-02-15', '2024-03-01', '2024-03-15', '2024-04-01'
        ]),
    })


def test_exact_duplicates_finds_pair():
    df = _sample_df()
    result = find_exact_duplicates(df, key_columns=['amount', 'vendor_id', 'date'])
    assert len(result) == 2


def test_exact_duplicates_has_group_id():
    df = _sample_df()
    result = find_exact_duplicates(df, key_columns=['amount', 'vendor_id', 'date'])
    assert 'duplicate_group_id' in result.columns


def test_exact_duplicates_no_duplicates_returns_empty():
    df = _sample_df().drop_duplicates(subset=['amount', 'vendor_id', 'date'])
    result = find_exact_duplicates(df, key_columns=['amount', 'vendor_id', 'date'])
    assert len(result) == 0


def test_round_numbers_flags_exact_thousands():
    df = _sample_df()
    result = detect_round_numbers(df, amount_column='amount')
    flagged_amounts = result['amount'].tolist()
    assert 1000.0 in flagged_amounts
    assert 5000.0 in flagged_amounts


def test_round_numbers_does_not_flag_precise_amounts():
    df = _sample_df()
    result = detect_round_numbers(df, amount_column='amount')
    assert 1247.83 not in result['amount'].tolist()


def test_round_numbers_has_round_level_column():
    df = _sample_df()
    result = detect_round_numbers(df, amount_column='amount')
    assert 'round_level' in result.columns


def test_round_numbers_round_level_is_largest_threshold():
    df = pd.DataFrame({'amount': [5000.0]})
    result = detect_round_numbers(df, amount_column='amount',
                                   thresholds=[100, 500, 1000, 5000])
    assert result.iloc[0]['round_level'] == 5000


def test_round_number_rate_returns_required_keys():
    df = _sample_df()
    result = round_number_rate(df, amount_column='amount')
    assert {'total_transactions', 'round_count', 'round_rate', 'flagged'} <= result.keys()


def test_round_number_rate_all_round():
    df = pd.DataFrame({'amount': [1000.0, 2000.0, 3000.0]})
    result = round_number_rate(df, amount_column='amount', threshold=1000)
    assert result['round_rate'] == pytest.approx(1.0)
