"""
Forensic Accounting Anomaly Detector -- CLI entry point.

Usage:
    python main.py --file data/sample/fraud_seeded.csv --amount amount
    python main.py --file data/sample/fraud_seeded.csv --amount amount \
        --vendor vendor_id --date date --output ./output --format text
"""
import argparse


def parse_args() -> argparse.Namespace:
    """
    Define CLI arguments.

    Required:
      --file      Path to the CSV or Excel transaction file
      --amount    Name of the amount column (after normalisation)

    Optional:
      --vendor    Vendor column name (enables per-vendor risk scoring)
      --date      Date column name (enables duplicate detection)
      --output    Directory to write charts and report (default: ./output)
      --format    Output format: 'text' or 'json' (default: 'text')
      --min-amount  Minimum transaction amount to include (default: 1.0)
    """
    raise NotImplementedError


def run_pipeline(args: argparse.Namespace) -> dict:
    """
    Orchestrate the full analysis pipeline:
    1. Load and normalise data          (src/ingestion.py)
    2. First + second digit Benford     (src/benford.py)
    3. Statistical tests                (src/statistics.py)
    4. Duplicate detection (if --date)  (src/detectors.py)
    5. Round number detection           (src/detectors.py)
    6. Visualisations                   (src/visualisation.py)
    7. Risk scoring                     (src/scoring.py)
    8. Print or save report

    Return the scoring dict so it can be asserted in integration tests.
    """
    raise NotImplementedError


if __name__ == '__main__':
    args = parse_args()
    run_pipeline(args)
