from flask import Flask
from commits import load, transform_api
import time
import threading


def update():
    while True:
        transform_api()
        time.sleep(60)


server = Flask(__name__)


@server.get("/numbers")
def upload_list():
    return load()


if __name__ == "__main__":
    threading.Thread(target=update).start()
    server.run()
