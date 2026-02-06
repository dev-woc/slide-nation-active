import csv
import io
import re

PRICE_KEYWORDS = ["price", "cost", "amount", "value", "usd"]


def clean_number(value):
    return float(re.sub(r"[^\d.-]", "", value))


def detect_price_column(rows):
    scores = {}
    headers = rows[0].keys()

    for header in headers:
        score = 0
        for row in rows:
            try:
                clean_number(row[header])
                score += 1
            except:
                pass

        if any(k in header.lower() for k in PRICE_KEYWORDS):
            score += 10

        scores[header] = score

    return max(scores, key=scores.get)


def parse_csv(file):
    stream = io.StringIO(file.stream.read().decode("utf-8"))
    reader = csv.DictReader(stream)
    rows = list(reader)

    if not rows:
        return None, None, "CSV is empty"

    price_col = detect_price_column(rows)

    prices = []
    items = []

    for row in rows:
        price = clean_number(row[price_col])
        prices.append(price)
        items.append({
            "name": row.get("Name") or row.get("Item") or "Row " + str(len(items)),
            "price": price
        })

    return prices, items, price_col
