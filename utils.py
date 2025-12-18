from typing import List
from pathlib import Path


def read(filename) -> List[str]:
    filepath = resolve_path(filename)
    try:
        with open(filepath) as file:
            lines = [line.rstrip() for line in file]
            return lines
    except Exception as e:
        raise e


def write(filepath, content) -> None:
    try:
        with open(filepath, "w") as f:
            f.write(content)
    except Exception as e:
        raise e


def resolve_path(filename: str) -> Path:
    path = Path(filename)
    if path.is_absolute():
        return path
    return Path(__file__).parent / path
