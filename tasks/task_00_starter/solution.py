
"""Reference implementation for the five-day precipitation task."""

import math


def rolling_5day_max_precip(daily_mm: list[float]) -> float:
    """Return the maximum sum among complete valid consecutive five-day windows.

    Negative values and NaN are treated as missing. Every value in a window
    must be valid; partial windows are not considered.
    """
    window_size = 5
    valid_window_totals = []

    for start in range(len(daily_mm) - window_size + 1):
        window = daily_mm[start : start + window_size]

        # A window is invalid if at least one value is negative or NaN.
        if any(value < 0 or math.isnan(value) for value in window):
            continue

        valid_window_totals.append(sum(window))

    if not valid_window_totals:
        raise ValueError("No valid consecutive five-day window exists.")

    return float(max(valid_window_totals))
