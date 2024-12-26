import hashlib

from utils.f import readinput

entries = readinput(__file__)


for i in range(1, 10000000):
    s = f"{entries}{str(i)}"
    h = hashlib.md5(s.encode()).hexdigest()
    if h.startswith("000000"):
        print(i)
        break
