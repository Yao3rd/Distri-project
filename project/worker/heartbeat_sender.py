import time
import requests

def send_heartbeat(worker_id):
    while True:
        try:
            requests.post(f"http://127.0.0.1:8000/heartbeat/{worker_id}")
        except:
            pass
        time.sleep(3)
