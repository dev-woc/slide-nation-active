HTML = """
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Two Sum CSV Solver</title>
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

  .card {
    background: #fff;
    border-radius: 24px;
    box-shadow: 0 20px 60px rgba(0,0,0,.18);
    padding: 2.5rem 2.5rem 2rem;
    width: 100%;
    max-width: 480px;
  }

  .card h1 {
    font-size: 1.8rem;
    text-align: center;
    margin-bottom: 1.5rem;
    color: #333;
  }

  /* ---- file upload area ---- */
  .upload-area {
    border: 3px dashed #c084fc;
    border-radius: 16px;
    padding: 1.5rem;
    text-align: center;
    cursor: pointer;
    transition: background .2s, border-color .2s;
    margin-bottom: 1.25rem;
    position: relative;
  }
  .upload-area:hover { background: #faf5ff; border-color: #7b2ff7; }
  .upload-area input[type="file"] {
    position: absolute; inset: 0; opacity: 0; cursor: pointer;
  }
  .upload-area .icon { font-size: 2rem; }
  .upload-area p { color: #888; margin-top: .4rem; font-size: .95rem; }

  /* ---- target input ---- */
  label.field-label {
    display: block;
    font-weight: 600;
    color: #555;
    margin-bottom: .35rem;
    font-size: .95rem;
  }
  input[type="number"] {
    width: 100%;
    padding: .7rem 1rem;
    border: 2px solid #e0d4f5;
    border-radius: 12px;
    font-size: 1rem;
    outline: none;
    transition: border-color .2s;
  }
  input[type="number"]:focus { border-color: #7b2ff7; }

  /* ---- solve button ---- */
  .btn-solve {
    margin-top: 1.5rem;
    width: 100%;
    padding: .85rem;
    border: none;
    border-radius: 14px;
    background: linear-gradient(135deg, #7b2ff7, #e94990);
    color: #fff;
    font-size: 1.1rem;
    font-weight: 700;
    cursor: pointer;
    transition: transform .15s, box-shadow .15s;
  }
  .btn-solve:hover {
    transform: scale(1.04);
    box-shadow: 0 8px 24px rgba(123,47,247,.35);
  }
  .btn-solve:active { transform: scale(.97); }

  /* ---- error banner ---- */
  .error-banner {
    background: linear-gradient(135deg, #fee2e2, #fecdd3);
    color: #b91c1c;
    border-radius: 14px;
    padding: 1rem 1.25rem;
    margin-top: 1.5rem;
    font-weight: 600;
    text-align: center;
  }

  /* ---- result section ---- */
  .result-section { margin-top: 1.75rem; }
  .result-section h2 {
    text-align: center;
    font-size: 1.25rem;
    color: #555;
    margin-bottom: .35rem;
  }
  .col-tag {
    display: block;
    text-align: center;
    font-size: .85rem;
    color: #999;
    margin-bottom: 1rem;
  }

  .match-row {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: .75rem;
    flex-wrap: wrap;
  }
  .item-card {
    flex: 1 1 160px;
    max-width: 200px;
    background: linear-gradient(135deg, #ede9fe, #fce7f3);
    border-radius: 16px;
    padding: 1.15rem;
    text-align: center;
  }
  .item-card .item-name {
    font-weight: 700;
    color: #6d28d9;
    font-size: 1rem;
    margin-bottom: .3rem;
  }
  .item-card .item-price {
    font-size: 1.35rem;
    font-weight: 800;
    color: #e94990;
  }
  .plus {
    font-size: 1.5rem;
    font-weight: 800;
    color: #7b2ff7;
  }

  .total-badge {
    margin-top: 1rem;
    text-align: center;
    display: inline-block;
    width: 100%;
  }
  .total-badge span {
    display: inline-block;
    background: linear-gradient(135deg, #7b2ff7, #e94990);
    color: #fff;
    font-size: 1.1rem;
    font-weight: 700;
    padding: .55rem 1.5rem;
    border-radius: 30px;
  }
</style>
</head>
<body>

<div class="card">
  <h1>🧮 Two-Sum CSV Solver</h1>

  <form method="post" enctype="multipart/form-data">
    <div class="upload-area">
      <input type="file" name="csvfile" required>
      <div class="icon">📂</div>
      <p>Drop a CSV or click to browse</p>
    </div>

    <label class="field-label" for="target">Target Value</label>
    <input type="number" step="any" name="target" id="target" placeholder="e.g. 914.00" required>

    <button class="btn-solve" type="submit">✨ Solve</button>
  </form>

  {% if error %}
  <div class="error-banner">⚠️ {{ error }}</div>
  {% endif %}

  {% if result %}
  <div class="result-section">
    <h2>🎉 Match Found!</h2>
    <span class="col-tag">Detected column: {{ column }}</span>

    <div class="match-row">
      <div class="item-card">
        <div class="item-name">{{ result[0]["name"] }}</div>
        <div class="item-price">${{ result[0]["price"] }}</div>
      </div>
      <div class="plus">+</div>
      <div class="item-card">
        <div class="item-name">{{ result[1]["name"] }}</div>
        <div class="item-price">${{ result[1]["price"] }}</div>
      </div>
    </div>

    <div class="total-badge"><span>Total: ${{ total }}</span></div>
  </div>
  {% endif %}
</div>

<script>
  document.querySelector('.upload-area input').addEventListener('change', function() {
    var name = this.files[0] ? this.files[0].name : 'No file chosen';
    this.closest('.upload-area').querySelector('p').textContent = name;
  });
</script>

</body>
</html>
"""
