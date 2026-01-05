from flask import Flask, render_template_string, request
from agents.document_agent import run as run_document_agent
from agents.support_agent import run as run_support_agent
import json

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>AI Agent Framework Dashboard</title>
    <style>
        body { font-family: Arial; background: #0f172a; color: #e5e7eb; padding: 20px; }
        h1 { color: #38bdf8; }
        button { padding: 10px 20px; margin: 10px 0; background: #22c55e; border: none; cursor: pointer; }
        pre { background: #020617; padding: 15px; overflow-x: auto; }
        .box { margin-top: 20px; }
    </style>
</head>
<body>
    <h1>AI Agent Framework – Execution Dashboard</h1>

    <form method="post">
        <button name="agent" value="document">Run Document Analysis Agent</button><br>
        <button name="agent" value="support">Run Customer Support Agent</button>
    </form>

    {% if result %}
    <div class="box">
        <h2>Execution Output</h2>
        <pre>{{ result }}</pre>
    </div>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        agent = request.form.get("agent")

        if agent == "document":
            output = run_document_agent("invoice_2025.pdf")
        elif agent == "support":
            output = run_support_agent("where is my order?")
        else:
            output = {}

        result = json.dumps(output, indent=4)

    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == "__main__":
    app.run(debug=True)
