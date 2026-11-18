
"""Independent checks for candidate implementations."""

import math
from collections.abc import Callable


CandidateFunction = Callable[[list[float]], float]


def _expect_value_error(candidate_fn: CandidateFunction, values: list[float], case: str) -> None:
    """Raise AssertionError if the candidate does not raise ValueError."""
    try:
        candidate_fn(values)
    except ValueError:
        return
    raise AssertionError(f"{case}: expected ValueError, but no ValueError was raised.")


def verify(candidate_fn: CandidateFunction) -> None:
    """Verify normal, missing-value, and insufficient-window behaviour.

    The function returns None when all checks pass and raises AssertionError
    when the candidate violates the task requirements.
    """
    # Check 1: ordinary input with two complete windows.
    result = candidate_fn([10.0, 20.0, 30.0, 40.0, 50.0, 60.0])
    assert math.isclose(result, 200.0, rel_tol=0.0, abs_tol=1e-9), (
        f"Normal case: expected 200.0, received {result!r}."
    )

    # Check 2: a missing sentinel must invalidate a five-day window.
    _expect_value_error(
        candidate_fn,
        [10.0, 20.0, -999.0, 40.0, 50.0],
        "Negative missing-value sentinel case",
    )

    # Check 3: NaN must also invalidate a five-day window.
    _expect_value_error(
        candidate_fn,
        [10.0, 20.0, float("nan"), 40.0, 50.0],
        "NaN case",
    )

    # Check 4: fewer than five days cannot form a five-day window.
    _expect_value_error(
        candidate_fn,
        [10.0, 20.0, 30.0, 40.0],
        "Short-input case",
    )
