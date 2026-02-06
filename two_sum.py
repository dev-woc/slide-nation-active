from flask import Flask, request, render_template_string
import csv
import io
import re

app = Flask(__name__)

HTML = """
<!doctype html>
<title>Two Sum CSV Solver</title>
<h2>Two Sum CSV Solver</h2>

<form method="post" enctype="multipart/form-data">
  <label>Upload CSV:</label><br>
  <input type="file" name="csvfile" required><br><br>

  <label>Target Value:</label><br>
  <input type="number" step="any" name="target" required><br><br>

  <button type="submit">Solve</button>
</form>

{% if error %}
  <p style="color:red">{{ error }}</p>
{% endif %}

{% if result %}
  <h3>Result</h3>
  <p><strong>Detected price column:</strong> {{ column }}</p>
  <ul>
    <li>{{ result[0]["name"] }} — ${{ result[0]["price"] }}</li>
    <li>{{ result[1]["name"] }} — ${{ result[1]["price"] }}</li>
  </ul>
  <p><strong>Total:</strong> ${{ total }}</p>
{% endif %}
"""

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

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = round(target - num, 2)
        if complement in seen:
            return seen[complement], i
        seen[round(num, 2)] = i
    return None

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            file = request.files["csvfile"]
            target = float(request.form["target"])

            stream = io.StringIO(file.stream.read().decode("utf-8"))
            reader = csv.DictReader(stream)
            rows = list(reader)

            if not rows:
                return render_template_string(HTML, error="CSV is empty")

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

            match = two_sum(prices, target)

            if not match:
                return render_template_string(HTML, error="No matching pair found")

            i, j = match

            return render_template_string(
                HTML,
                result=[items[i], items[j]],
                total=round(items[i]["price"] + items[j]["price"], 2),
                column=price_col
            )

        except Exception as e:
            return render_template_string(HTML, error=str(e))

    return render_template_string(HTML)

app.run(host="0.0.0.0", port=3000)
