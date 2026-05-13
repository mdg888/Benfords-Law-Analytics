"""
Tests for src/statistics.py -- Phase 4.

Run with: pytest tests/test_statistics.py -v
"""
import math
import pytest
import numpy as np
import pandas as pd
from src.statistics import chi_square_test, mean_absolute_deviation, z_score_by_digit
from src.benford import expected_benford_distribution, first_digit_distribution


def _benford_series(n: int = 5000, seed: int = 42) -> pd.Series:
    rng = np.random.default_rng(seed)
    return pd.Series(10 ** rng.uniform(0, 4, n))


def _uniform_series(n: int = 5000, seed: int = 42) -> pd.Series:
    rng = np.random.default_rng(seed)
    digits = rng.integers(1, 10, n)
    remainders = rng.uniform(0, 1, n)
    return pd.Series(digits + remainders)


def test_mad_returns_required_keys():
    dist = first_digit_distribution(_benford_series())
    result = mean_absolute_deviation(dist['observed_freq'], dist['expected_freq'])
    assert {'mad', 'conformity_level', 'flagged'} <= result.keys()


def test_mad_benford_data_close_conformity():
    dist = first_digit_distribution(_benford_series(10_000))
    result = mean_absolute_deviation(dist['observed_freq'], dist['expected_freq'])
    assert result['conformity_level'] in ('Close conformity', 'Acceptable conformity')
    assert result['flagged'] is False


def test_mad_uniform_data_non_conformity():
    dist = first_digit_distribution(_uniform_series(5000))
    result = mean_absolute_deviation(dist['observed_freq'], dist['expected_freq'])
    assert result['conformity_level'] == 'Non-conformity'
    assert result['flagged'] is True


def test_chi_square_returns_required_keys():
    dist = first_digit_distribution(_benford_series())
    result = chi_square_test(dist['observed_freq'], dist['expected_freq'], n=5000)
    assert {'statistic', 'p_value', 'significant', 'interpretation'} <= result.keys()


def test_chi_square_benford_data_not_significant():
    dist = first_digit_distribution(_benford_series(10_000))
    result = chi_square_test(dist['observed_freq'], dist['expected_freq'], n=10_000)
    assert result['p_value'] > 0.01


def test_chi_square_uniform_data_significant():
    dist = first_digit_distribution(_uniform_series(5000))
    result = chi_square_test(dist['observed_freq'], dist['expected_freq'], n=5000)
    assert result['significant'] is True
    assert result['p_value'] < 0.05


def test_z_score_returns_required_columns():
    dist = first_digit_distribution(_benford_series())
    result = z_score_by_digit(dist['observed_freq'], dist['expected_freq'], n=5000)
    assert {'digit', 'z_score', 'flagged'} <= set(result.columns)


def test_z_score_benford_data_few_flagged():
    dist = first_digit_distribution(_benford_series(10_000))
    result = z_score_by_digit(dist['observed_freq'], dist['expected_freq'], n=10_000)
    assert result['flagged'].sum() <= 2


def test_z_score_sorted_descending():
    dist = first_digit_distribution(_uniform_series(5000))
    result = z_score_by_digit(dist['observed_freq'], dist['expected_freq'], n=5000)
    assert list(result['z_score']) == sorted(result['z_score'], reverse=True)
