import csv
import sys
from collections import OrderedDict, defaultdict
from typing import Dict

import requests

API_URL = "https://ru.wikipedia.org/w/api.php"
CATEGORY = "Категория:Животные_по_алфавиту"

ALPHABET = list("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")


def fetch_category_members(category: str) -> Dict[str, int]:

    counts = defaultdict(int)
    params = {
        "action": "query",
        "format": "json",
        "list": "categorymembers",
        "cmtitle": category,
        "cmlimit": "max",
        "cmtype": "page",
    }

    session = requests.Session()

    while True:
        resp = session.get(API_URL, params=params, timeout=30)
        resp.raise_for_status()
        data = resp.json()

        for page in data["query"]["categorymembers"]:
            first = page["title"][0].upper()
            counts[first] += 1

        if "continue" not in data:
            break
        params["cmcontinue"] = data["continue"]["cmcontinue"]

    return counts


def write_csv(counts: Dict[str, int], path: str = "beasts.csv") -> None:
    ordered = OrderedDict((letter, counts.get(letter, 0))
                          for letter in ALPHABET)

    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        for letter, qty in ordered.items():
            writer.writerow([letter, qty])


def main() -> None:
    try:
        counts = fetch_category_members(CATEGORY)
        write_csv(counts)
        print("Готово!")
    except requests.RequestException as err:
        print("Сбой при обращении к Wikipedia API:", err, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
