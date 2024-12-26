from pathlib import Path


def readinput(f):
    f = Path(f).parent
    input_path = f / "input.txt"
    return input_path.open("r", encoding="utf-8").read()
