import pandas as pd


def chi_square_test(observed_freq: pd.Series, expected_freq: pd.Series, n: int) -> dict:
    """
    Chi-square goodness-of-fit test: does the observed distribution match Benford's?

    observed_freq and expected_freq are proportions (each sums to 1.0).
    n is the total number of observations.

    scipy.stats.chisquare takes COUNTS not proportions -- multiply by n first.

    Return: {'statistic': float, 'p_value': float, 'significant': bool,
             'interpretation': str}

    Important caveat: chi-square is unreliable below ~1,000 transactions.
    Document this in the interpretation string when n < 1000.
    """
    raise NotImplementedError


def mean_absolute_deviation(observed_freq: pd.Series, expected_freq: pd.Series) -> dict:
    """
    Mean Absolute Deviation between observed and expected digit frequencies.
    MAD = mean(|observed_i - expected_i|) across all digits.

    ACFE Fraud Examiners Manual conformity thresholds (first-digit test):
      MAD < 0.006  -> 'Close conformity'
      MAD < 0.012  -> 'Acceptable conformity'
      MAD < 0.015  -> 'Marginally acceptable'
      MAD >= 0.015 -> 'Non-conformity'

    Return: {'mad': float, 'conformity_level': str, 'flagged': bool}
    flagged=True when conformity_level == 'Non-conformity'.
    """
    raise NotImplementedError


def z_score_by_digit(observed_freq: pd.Series, expected_freq: pd.Series,
                     n: int) -> pd.DataFrame:
    """
    Z-score for each digit to identify WHICH digits are most anomalous.

    Formula: Z = (|obs - exp| - 1/(2n)) / sqrt(exp * (1 - exp) / n)
    The 1/(2n) term is a continuity correction.

    flagged=True when |Z| > 1.96 (95% confidence).

    Return DataFrame: ['digit', 'z_score', 'flagged']
    Sort by z_score descending so the most anomalous digit is first.

    Why: chi-square tells you *something* is wrong with the distribution.
    Z-scores tell you *which digit* -- investigators then filter the ledger
    for transactions starting with that digit.
    """
    raise NotImplementedError
