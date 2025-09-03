import pandas as pd, sys

# Simple imbalance check by a protected attribute column name
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python tools/dataset_bias_audit.py <csv> <column>")
        sys.exit(2)
    csv, col = sys.argv[1], sys.argv[2]
    df = pd.read_csv(csv)
    counts = df[col].value_counts(normalize=True)
    print("Distribution", counts.to_dict())
    # Flag if any group < 5% or > 80%
    bad = any(v < 0.05 or v > 0.80 for v in counts.values)
    sys.exit(1 if bad else 0)
