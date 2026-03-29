from typing import Iterable, Sequence, Union

Number = Union[int, float]


def average_ratios(numbers: Sequence[Number]) -> float:
    """Compute the average of 100 / n for each non-zero numeric n in numbers.

    - Skips zeros (to avoid ZeroDivisionError).
    - Raises ValueError if the input is empty or contains no valid (non-zero) numbers.
    """
    if not numbers:
        raise ValueError("'numbers' must not be empty")

    ratios = []
    for idx, n in enumerate(numbers):
        try:
            val = float(n)
        except (TypeError, ValueError):
            # Non-numeric values are ignored
            continue
        if val == 0.0:
            # skip zeros to avoid division error
            continue
        ratios.append(100.0 / val)

    if not ratios:
        raise ValueError("No valid non-zero numeric values to compute average")

    return sum(ratios) / len(ratios)


if __name__ == "__main__":
    # Quick smoke test for the reported failing case
    test_input = [10, 5, 0]
    try:
        print(average_ratios(test_input))
    except Exception as e:
        print("Error:", e)
