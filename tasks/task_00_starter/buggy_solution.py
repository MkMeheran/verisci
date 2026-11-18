
"""Intentionally incorrect implementation used to test the verifier."""


def rolling_5day_max_precip(daily_mm: list[float]) -> float:
    """BUG: sums every five-day window without checking missing values."""
    window_size = 5

    if len(daily_mm) < window_size:
        raise ValueError("At least five values are required.")

    totals = []
    for start in range(len(daily_mm) - window_size + 1):
        # BUG: -999.0 and other negative sentinels are treated as real values.
        # BUG: NaN is not checked and may contaminate the result.
        totals.append(sum(daily_mm[start : start + window_size]))

    return float(max(totals))
