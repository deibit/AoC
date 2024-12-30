from pathlib import Path


def _read(f, filename):
    f = Path(f).parent
    input_path = f / filename
    return input_path.open("r", encoding="utf-8").read()


def readinput(f):
    return _read(f, "input.txt")


def readtest(f):
    return _read(f, "test.txt")
