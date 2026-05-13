"""
Generate synthetic sample datasets for testing and development.

Run from the project root:
    python scripts/generate_sample_data.py

Produces:
  data/sample/clean_transactions.csv   -- Benford-conforming, no fraud
  data/sample/dirty_transactions.csv   -- same data but messy formatting
  data/sample/fraud_seeded.csv         -- clean data + planted fraud signals
"""
import numpy as np
import pandas as pd
from pathlib import Path

SEED = 42
OUTPUT_DIR = Path(__file__).parent.parent / 'data' / 'sample'


def generate_clean(n: int = 500, rng: np.random.Generator = None) -> pd.DataFrame:
    """
    Generate n transactions with Benford-conforming amounts.

    Hint: amounts drawn from 10 ** rng.uniform(0, 4, n) follow Benford's Law
    naturally because they span several orders of magnitude.

    Columns: amount, vendor_id, date
    - vendor_id: 20 distinct vendors (V001-V020), randomly assigned
    - date: random dates within 2024

    TODO: implement this function.
    """
    raise NotImplementedError


def make_dirty(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add formatting noise to a clean DataFrame to simulate real ERP exports:
    - Rename 'amount' column to 'Invoice Amount' (space in name)
    - Format amounts as strings: '$1,234.56'
    - Format some amounts as accounting negatives: '(500.00)'
    - Mix date formats: some 'YYYY-MM-DD', some 'DD/MM/YYYY'
    - Insert one blank row
    - Add a stray currency column

    TODO: implement this function.
    """
    raise NotImplementedError


def seed_fraud(df: pd.DataFrame, rng: np.random.Generator) -> pd.DataFrame:
    """
    Plant fraud signals into a clean DataFrame:
    1. 14 exact duplicate pairs (same amount, vendor, date)
    2. 20 transactions at $9,999 (threshold avoidance - just under $10k approval limit)
    3. 30 transactions from vendor 'V_FRAUD' with amounts uniformly distributed
       across digits 1-9 (violates Benford's Law)

    TODO: implement this function.
    """
    raise NotImplementedError


if __name__ == '__main__':
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(SEED)

    # TODO: call generate_clean, make_dirty, seed_fraud and save to CSV
    print("TODO: implement the generator functions above, then uncomment the lines below.")

    # clean = generate_clean(500, rng)
    # clean.to_csv(OUTPUT_DIR / 'clean_transactions.csv', index=False)
    # print(f"Saved clean_transactions.csv ({len(clean)} rows)")

    # dirty = make_dirty(clean.copy())
    # dirty.to_csv(OUTPUT_DIR / 'dirty_transactions.csv', index=False)
    # print(f"Saved dirty_transactions.csv ({len(dirty)} rows)")

    # fraud = seed_fraud(generate_clean(500, rng), rng)
    # fraud.to_csv(OUTPUT_DIR / 'fraud_seeded.csv', index=False)
    # print(f"Saved fraud_seeded.csv ({len(fraud)} rows)")
