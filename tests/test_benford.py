"""
Tests for src/benford.py -- Phases 2 & 3.

Run with: pytest tests/test_benford.py -v
"""
import math
import pytest
import numpy as np
import pandas as pd
from src.benford import (
    expected_benford_distribution,
    extract_first_digit,
    first_digit_distribution,
    expected_second_digit_distribution,
    extract_second_digit,
    second_digit_distribution,
)


def test_benford_probabilities_sum_to_one():
    dist = expected_benford_distribution()
    assert math.isclose(sum(dist.values()), 1.0, rel_tol=1e-9)


def test_benford_digit_one_is_most_probable():
    dist = expected_benford_distribution()
    assert dist[1] == max(dist.values())


def test_benford_digit_one_approx_301():
    dist = expected_benford_distribution()
    assert math.isclose(dist[1], 0.30103, rel_tol=1e-4)


def test_benford_covers_digits_1_to_9():
    dist = expected_benford_distribution()
    assert set(dist.keys()) == set(range(1, 10))


def test_extract_first_digit_basic():
    assert extract_first_digit(1234.56) == 1
    assert extract_first_digit(987.0) == 9
    assert extract_first_digit(0.0056) == 5


def test_extract_first_digit_negative_amount():
    assert extract_first_digit(-500.0) == 5


def test_extract_first_digit_zero_returns_none():
    assert extract_first_digit(0) is None


def test_extract_first_digit_nan_returns_none():
    assert extract_first_digit(float('nan')) is None


def test_first_digit_distribution_columns():
    amounts = pd.Series([123, 456, 789, 111, 222])
    result = first_digit_distribution(amounts)
    assert set(result.columns) >= {'digit', 'observed_freq', 'expected_freq', 'difference'}


def test_first_digit_distribution_covers_all_digits():
    amounts = pd.Series([100, 200])
    result = first_digit_distribution(amounts)
    assert set(result['digit']) == set(range(1, 10))


def test_first_digit_distribution_observed_freq_sums_to_one():
    rng = np.random.default_rng(42)
    amounts = pd.Series(10 ** rng.uniform(0, 4, 1000))
    result = first_digit_distribution(amounts)
    assert math.isclose(result['observed_freq'].sum(), 1.0, rel_tol=1e-6)


def test_first_digit_distribution_benford_data_close_to_expected():
    rng = np.random.default_rng(42)
    amounts = pd.Series(10 ** rng.uniform(0, 4, 10_000))
    result = first_digit_distribution(amounts)
    max_diff = result['difference'].abs().max()
    assert max_diff < 0.05


def test_second_digit_probabilities_sum_to_one():
    dist = expected_second_digit_distribution()
    assert math.isclose(sum(dist.values()), 1.0, rel_tol=1e-9)


def test_second_digit_covers_digits_0_to_9():
    dist = expected_second_digit_distribution()
    assert set(dist.keys()) == set(range(0, 10))


def test_second_digit_zero_approx_120():
    dist = expected_second_digit_distribution()
    assert math.isclose(dist[0], 0.11968, rel_tol=1e-3)


def test_extract_second_digit_basic():
    assert extract_second_digit(1234.56) == 2
    assert extract_second_digit(9876.0) == 8


def test_extract_second_digit_single_digit_returns_none():
    assert extract_second_digit(7.0) is None


def test_extract_second_digit_small_decimal():
    assert extract_second_digit(0.0056) == 6
