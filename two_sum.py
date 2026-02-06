from flask import Flask, request, render_template_string
from template import HTML
from csv_helpers import parse_csv

app = Flask(__name__)


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

            prices, items, price_col = parse_csv(file)

            if prices is None:
                return render_template_string(HTML, error=price_col)

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
