
# Evaluation Rubric: `rolling_5day_max_precip`

A candidate implementation is evaluated against the scientific requirements in
`prompt.md`.

| Criterion | What is checked | Weight |
|---|---|---:|
| Correct rolling calculation | Computes sums over consecutive windows of exactly five days | 30 |
| Maximum selection | Returns the largest valid five-day total | 20 |
| Negative-value handling | Treats negative values, including `-999.0`, as missing | 20 |
| NaN handling | Treats `NaN` as missing | 15 |
| Window completeness | Rejects windows containing any missing value; does not use partial windows | 10 |
| Error behaviour | Raises `ValueError` when no complete valid five-day window exists | 5 |
| **Total** | | **100** |

## Pass conditions

- The reference implementation must pass all verifier checks.
- An implementation that treats `-999.0` as a real measurement must fail.
- An implementation that accepts incomplete windows must fail.
- An implementation that does not raise `ValueError` when no valid window exists must fail.

## Evaluation note

The rubric describes the task's expected behaviour. It does not authorize deleting
or imputing missing observations. For this task, any five-day window containing
a negative value or `NaN` is excluded from the calculation.
