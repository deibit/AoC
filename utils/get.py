# based on https://github.com/loganmeetsworld/advent-of-code-utils/blob/main/aoc_utils/aoc_utils.py

import os
import sys
from pathlib import Path

import requests

# from bs4 import BeautifulSoup
from colorama import Fore, Style

COOKIE = os.environ["AOC_COOKIE"]

if COOKIE == None:
    print(f"{Fore.RED}")

HEADERS = {
    "cookie": f"session={COOKIE}",
}

if len(sys.argv) < 3:
    print(f"{Fore.BLUE}Uso: get.py year day")
    quit()

year, day = [sys.argv[1], sys.argv[2]]
if int(day) < 10:
    day = f"0{day}"

path = Path(f"{Path.cwd()}/../{year}/{day}")


def handle_error_status(code):
    if code == 404:
        print(
            f"{Fore.RED}{code}: No existe el problema del día indicado{Style.RESET_ALL}"
        )
        quit()
    elif code == 400:
        print(
            f"{Fore.RED}{code}: Mira la cookie porque algo ha fallado con la auth{Style.RESET_ALL}"
        )
        quit()
    elif code > 400:
        print(f"{Fore.RED}{code}: Error no definido{Style.RESET_ALL}")
        quit()


def save_input(year, day):
    global path
    if day.startswith("0"):
        day = day[1]
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    print(f"{Fore.BLUE}Bajando {url}")
    response = requests.get(url, headers=HEADERS)
    handle_error_status(response.status_code)
    txt = response.text.strip()
    input_file = Path(f"{path}/input.txt")
    if input_file.exists():
        print(f"{Fore.YELLOW} ya existe un input.txt en {input_file}")
        return
    with open(input_file, "w") as f:
        f.write(txt)
    print(f"{Fore.BLUE}Se ha escrito el archivo {input_file}")


def make_dir():
    global path
    try:
        path.mkdir()
        print(f"{Fore.BLUE}Creando directorio en {path}")
    except FileExistsError:
        print(f"{Fore.BLUE}Ya existe el {path}")


if __name__ == "__main__":
    make_dir()
    save_input(year, day)
