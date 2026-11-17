import os
import time

import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=int(os.getenv("REDIS_PORT", "6379")),
)


def get_hit_count():
    # Redis may still be starting when the first request lands, so retry briefly
    retries = 5
    while True:
        try:
            return cache.incr("hits")
        except redis.exceptions.ConnectionError:
            if retries == 0:
                raise
            retries -= 1
            time.sleep(0.5)


@app.route("/")
def hello():
    count = get_hit_count()
    return f"Hello from balena! I have been seen {count} time(s).\n"
