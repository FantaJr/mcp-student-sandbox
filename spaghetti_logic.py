from pathlib import Path
from typing import Iterable, List, Union

Number = Union[int, float]


def compute_totals(data: Iterable[Number], multiplier: float = 1.15) -> List[float]:
    """Compute multiplied totals from an iterable of numbers.

    Converts items to float and applies the multiplier. Raises TypeError
    if any item cannot be converted to float.
    """
    totals: List[float] = []
    for i, item in enumerate(data):
        try:
            value = float(item) * multiplier
        except (TypeError, ValueError) as exc:
            raise TypeError(f"Item at index {i} is not a number: {item!r}") from exc
        totals.append(value)
    return totals


def format_total(value: float, prefix: str = "Total: ") -> str:
    """Return a nicely formatted total string for a single value."""
    return f"{prefix}{value:.2f}"


def print_totals(totals: Iterable[float], prefix: str = "Total: ") -> None:
    """Print formatted totals, one per line."""
    for t in totals:
        print(format_total(t, prefix))


def append_log(totals: Iterable[float], log_path: Union[str, Path] = "log.txt") -> None:
    """Append the list of totals to a log file safely.

    The totals are written using repr(list(totals)) so the file contains
    a recoverable Python-like representation.
    """
    p = Path(log_path)
    try:
        # Ensure parent directory exists (no-op if in CWD)
        p.parent.mkdir(parents=True, exist_ok=True)
        with p.open("a", encoding="utf-8") as f:
            f.write(repr(list(totals)) + "\n")
    except OSError as exc:
        raise RuntimeError(f"Failed to write log to {p}") from exc


def process_data(
    data: Iterable[Number],
    multiplier: float = 1.15,
    log_path: Union[str, Path] = "log.txt",
    print_out: bool = True,
) -> List[float]:
    """Orchestrate computing totals, printing, and logging.

    Returns the list of computed totals.
    """
    totals = compute_totals(data, multiplier)
    if print_out:
        print_totals(totals)
    append_log(totals, log_path)
    return totals


if __name__ == "__main__":
    # Simple demonstration when run as a script. Avoids side-effects on import.
    example = [10, 20.5, 30]
    try:
        result = process_data(example)
        print("Processed totals:", result)
    except Exception as exc:
        print("Error while processing data:", exc)
