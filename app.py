import logging
import os

from azure.monitor.opentelemetry import configure_azure_monitor
from flask import Flask, jsonify

# Configure Azure Monitor if connection string is available
if os.environ.get("APPLICATIONINSIGHTS_CONNECTION_STRING"):
    configure_azure_monitor()

logger = logging.getLogger(__name__)

app = Flask(__name__)

# Store allocated memory blocks so they aren't garbage collected
memory_blocks = []

PAGE = """<!DOCTYPE html>
<html>
<head>
    <title>Memory Demo</title>
    <style>
        body { font-family: sans-serif; max-width: 600px; margin: 60px auto; text-align: center; }
        button { padding: 12px 24px; font-size: 18px; cursor: pointer; border: none; border-radius: 6px; color: #fff; }
        #allocate { background: #e53e3e; }
        #free { background: #38a169; }
        #status { margin-top: 24px; font-size: 16px; color: #555; }
    </style>
</head>
<body>
    <h1>Memory Stress Demo</h1>
    <p>Each click allocates ~500 MB of memory.</p>
    <button id="allocate" onclick="allocate()">Allocate 500 MB</button>
    <button id="free" onclick="free_mem()">Free All</button>
    <div id="status">Allocated: 0 MB</div>
    <script>
        async function allocate() {
            const res = await fetch('/allocate', { method: 'POST' });
            const data = await res.json();
            document.getElementById('status').textContent = 'Allocated: ' + data.total_mb + ' MB';
        }
        async function free_mem() {
            const res = await fetch('/free', { method: 'POST' });
            const data = await res.json();
            document.getElementById('status').textContent = 'Allocated: ' + data.total_mb + ' MB';
        }
    </script>
</body>
</html>"""


@app.route("/")
def index():
    return PAGE


@app.route("/allocate", methods=["POST"])
def allocate():
    # Allocate ~500 MB (500 * 1024 * 1024 bytes)
    block = bytearray(500 * 1024 * 1024)
    memory_blocks.append(block)
    total_mb = len(memory_blocks) * 500
    logger.warning("Memory allocated: %d MB total", total_mb)
    return jsonify(total_mb=total_mb)


@app.route("/free", methods=["POST"])
def free():
    memory_blocks.clear()
    logger.info("All memory freed")
    return jsonify(total_mb=0)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
