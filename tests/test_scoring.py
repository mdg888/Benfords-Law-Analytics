"""
Tests for src/scoring.py -- Phase 8.

Run with: pytest tests/test_scoring.py -v
"""
import pytest
from src.scoring import compute_dataset_risk_score


def _make_inputs(mad_conformity='Close conformity', chi_significant=False,
                 duplicate_count=0, round_rate=0.02, n=1000):
    benford_first = {
        'mad': 0.004 if mad_conformity == 'Close conformity' else 0.018,
        'conformity_level': mad_conformity,
        'flagged': mad_conformity == 'Non-conformity',
        'p_value': 0.5 if not chi_significant else 0.001,
        'significant': chi_significant,
    }
    benford_second = dict(benford_first)
    rn_rate = {
        'round_rate': round_rate,
        'flagged': round_rate > 0.1,
    }
    return benford_first, benford_second, duplicate_count, rn_rate, n


def test_score_returns_required_keys():
    result = compute_dataset_risk_score(*_make_inputs())
    assert {'total_score', 'max_score', 'risk_level', 'signals'} <= result.keys()


def test_score_clean_data_is_low():
    result = compute_dataset_risk_score(*_make_inputs())
    assert result['risk_level'] == 'LOW'
    assert result['total_score'] <= 30


def test_score_fraud_signals_is_high():
    result = compute_dataset_risk_score(*_make_inputs(
        mad_conformity='Non-conformity',
        chi_significant=True,
        duplicate_count=50,
        round_rate=0.25,
        n=1000,
    ))
    assert result['risk_level'] in ('HIGH', 'CRITICAL')
    assert result['total_score'] >= 61


def test_score_max_is_100():
    result = compute_dataset_risk_score(*_make_inputs())
    assert result['max_score'] == 100


def test_score_signals_list_not_empty():
    result = compute_dataset_risk_score(*_make_inputs())
    assert len(result['signals']) > 0


def test_score_signals_have_required_keys():
    result = compute_dataset_risk_score(*_make_inputs())
    for signal in result['signals']:
        assert {'signal', 'score', 'max_score'} <= signal.keys()
