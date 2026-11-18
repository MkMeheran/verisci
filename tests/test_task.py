
"""Dual-pass tests: the reference passes and the intentionally buggy code fails."""

import pytest

from tasks.task_00_starter.solution import (
    rolling_5day_max_precip as reference_fn,
)
from tasks.task_00_starter.buggy_solution import (
    rolling_5day_max_precip as buggy_fn,
)
from tasks.task_00_starter.verifier import verify


def test_reference_passes():
    """The correct reference implementation must satisfy the verifier."""
    verify(reference_fn)


def test_buggy_fails():
    """The verifier must detect the intentionally incorrect implementation."""
    with pytest.raises(AssertionError):
        verify(buggy_fn)
