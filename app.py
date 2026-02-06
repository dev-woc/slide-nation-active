from flask import Flask, render_template_string
from solutions.two_sum import bp as two_sum_bp

app = Flask(__name__)
app.register_blueprint(two_sum_bp)

LANDING_HTML = """
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Solution Hub</title>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(135deg, #7b2ff7, #e94990, #f5a623);
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    padding: 2rem;
  }

  .container {
    width: 100%;
    max-width: 720px;
    text-align: center;
  }

  .container h1 {
    font-size: 2.4rem;
    color: #fff;
    margin-bottom: .5rem;
    text-shadow: 0 2px 12px rgba(0,0,0,.15);
  }

  .container p.subtitle {
    color: rgba(255,255,255,.85);
    font-size: 1.1rem;
    margin-bottom: 2.5rem;
  }

  .grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 1.5rem;
  }

  .solution-card {
    background: #fff;
    border-radius: 20px;
    box-shadow: 0 12px 40px rgba(0,0,0,.14);
    padding: 2rem 1.5rem;
    text-decoration: none;
    color: inherit;
    transition: transform .18s, box-shadow .18s;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: .6rem;
  }

  .solution-card:hover {
    transform: translateY(-6px) scale(1.03);
    box-shadow: 0 18px 50px rgba(0,0,0,.2);
  }

  .solution-card .icon {
    font-size: 2.4rem;
  }

  .solution-card .name {
    font-size: 1.15rem;
    font-weight: 700;
    color: #333;
  }

  .solution-card .desc {
    font-size: .88rem;
    color: #888;
    line-height: 1.4;
  }
</style>
</head>
<body>

<div class="container">
  <h1>Solution Hub</h1>
  <p class="subtitle">Pick a problem to solve</p>

  <div class="grid">
    <a class="solution-card" href="/two-sum">
      <div class="icon">🧮</div>
      <div class="name">Two Sum</div>
      <div class="desc">Upload a CSV and find two items that add up to a target value.</div>
    </a>
  </div>
</div>

</body>
</html>
"""


@app.route("/")
def landing():
    return render_template_string(LANDING_HTML)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
