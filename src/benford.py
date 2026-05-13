import pandas as pd


# -- Phase 2: First Digit -----------------------------------------------------

def expected_benford_distribution() -> dict[int, float]:
    """
    Return expected first-digit probabilities under Benford's Law.
    Formula: P(d) = log10(1 + 1/d) for d in 1..9.

    Sanity check: values must sum to 1.0. Write a test for this.
    Hint: use math.log10 or numpy.log10.
    """
    raise NotImplementedError


def extract_first_digit(amount: float) -> int | None:
    """
    Return the leading significant digit (1-9) of amount.

    Use absolute value first -- negative amounts are valid transactions.
    Return None for zero and NaN. Document this exclusion: an auditor will ask.
    Hint: convert to str and find the first character that is a non-zero digit.
    """
    raise NotImplementedError


def first_digit_distribution(amounts: pd.Series) -> pd.DataFrame:
    """
    Compute observed vs expected first-digit frequencies for a Series of amounts.

    Steps:
    1. Apply extract_first_digit across the Series.
    2. Use value_counts(normalize=True) to get observed proportions.
    3. Reindex to ensure all digits 1-9 appear (fill missing with 0).
    4. Join with expected_benford_distribution().

    Return columns: ['digit', 'observed_count', 'observed_freq', 'expected_freq', 'difference']
    where difference = observed_freq - expected_freq.
    Positive difference means the digit appears MORE than expected.
    """
    raise NotImplementedError


# -- Phase 3: Second Digit ----------------------------------------------------

def expected_second_digit_distribution() -> dict[int, float]:
    """
    Return expected second-digit probabilities (digits 0-9).
    Formula: for each d in 0..9, sum log10(1 + 1/(10*d1 + d)) for d1 in 1..9.

    Note: second digits include 0, unlike first digits.
    Sanity check: values must sum to 1.0.
    """
    raise NotImplementedError


def extract_second_digit(amount: float) -> int | None:
    """
    Return the second significant digit of amount.

    'Second digit' in Benford context = second digit of the significand.
    Think through edge cases: single-digit numbers, 10, 100, 0.0056.
    Return None when there is no second digit (e.g. single-digit integers).
    """
    raise NotImplementedError


def second_digit_distribution(amounts: pd.Series) -> pd.DataFrame:
    """
    Same structure as first_digit_distribution but for second digits 0-9.
    Return columns: ['digit', 'observed_count', 'observed_freq', 'expected_freq', 'difference']
    """
    raise NotImplementedError
