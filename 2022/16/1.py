def get_data(filename):
    with open(filename, encoding="utf-8") as f:
        return f.read().split("\n")
