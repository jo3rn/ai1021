# factor 9: Disposability (fast startup and graceful shutdown)
from flask import Flask
import signal
import time

app = Flask(__name__)

@app.route('/')
def hello():
    time.sleep(5)
    return "Hello, AI1021!"

def handle_shutdown(signum, frame):
    print("Received shutdown signal, cleaning up...")

    # Perform any cleanup tasks here, e.g.
    # - close database connections and network sockets
    # - release file handles
    # - write logs
    # - finish in-progress requests

    time.sleep(10)  # Simulate graceful shutdown delay
    print("Cleanup complete, shutting down.")
    exit(0)

if __name__ == '__main__':
    # Register signal handlers for graceful shutdown
    signal.signal(signal.SIGINT, handle_shutdown)
    signal.signal(signal.SIGTERM, handle_shutdown)

    print("Starting the application...")
    app.run()
