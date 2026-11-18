
# Task 00: Maximum Rolling Five-Day Precipitation

## Problem

Implement a Python function named `rolling_5day_max_precip` that calculates the
maximum total precipitation across all consecutive five-day windows.

## Function signature

```python
def rolling_5day_max_precip(daily_mm: list[float]) -> float:
    ...
```

## Requirements

1. The input is a one-dimensional sequence of daily precipitation values in millimeters.
2. Treat every negative value (including the missing-value sentinel `-999.0`) as missing.
3. Treat `NaN` as missing.
4. A five-day window is valid only when all five values are non-missing.
5. Calculate the sum for every valid consecutive five-day window.
6. Return the largest valid five-day total.
7. Raise `ValueError` when the input contains no valid five-day window. This includes
   inputs shorter than five values and inputs where every five-day window contains
   at least one missing value.

## Example

Input:

```python
[10, 20, 30, 40, 50, 60]
```

The two five-day totals are `150` and `200`. The expected result is `200.0`.

## Important

Do not treat a missing-value sentinel as a real precipitation measurement.
Do not calculate a partial window when fewer than five valid consecutive days exist.
