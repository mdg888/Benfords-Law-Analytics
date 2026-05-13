import pandas as pd
import matplotlib.pyplot as plt


def plot_digit_distribution(distribution_df: pd.DataFrame,
                             digit_type: str = 'first',
                             title: str = None,
                             save_path: str = None,
                             ax=None) -> None:
    """
    Bar chart of observed vs expected digit frequencies.

    distribution_df has columns: ['digit', 'observed_freq', 'expected_freq']
    (output of first_digit_distribution or second_digit_distribution).

    Use ax.bar() for observed (blue, semi-transparent alpha=0.7).
    Overlay expected as a red line with markers: ax.plot(..., 'ro-').

    If ax is None, create a new figure with fig, ax = plt.subplots().
    If ax is provided, draw into it (enables side-by-side in the notebook).
    If save_path provided -> plt.savefig(). If None -> plt.show().

    Label axes: 'Digit' and 'Frequency (proportion)'.
    Add a legend and a descriptive title.
    """
    raise NotImplementedError


def plot_anomaly_summary(scoring_df: pd.DataFrame,
                          save_path: str = None) -> None:
    """
    Horizontal bar chart showing each anomaly signal's contribution to
    the overall risk score.

    scoring_df has columns: ['signal', 'score', 'max_score']
    (from the 'signals' list in compute_dataset_risk_score output).

    Use a colour gradient: green for low contribution, red for high.
    Hint: normalise score/max_score to 0-1 and use plt.cm.RdYlGn_r.

    This is the executive summary visual -- the chart you'd show an
    audit committee to explain WHERE the risk is coming from.
    """
    raise NotImplementedError
