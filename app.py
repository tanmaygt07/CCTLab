from flask import Flask
import socket
import redis

app = Flask(__name__)

# Get container/server hostname
hostname = socket.gethostname()

# Connect to Redis service
redis_client = redis.Redis(
    host='redis',
    port=6379,
    decode_responses=True
)

@app.route("/")
def home():
    # Increment global counter
    count = redis_client.incr("global_counter")

    return f"""
    <html>
        <body style="font-family: Arial; text-align: center; padding-top:60px;">
            <h2>Cloud Computing Demo Application</h2>
            <p><b>Server Instance:</b> {hostname}</p>
            <p><b>Total Visitors:</b> {count}</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)