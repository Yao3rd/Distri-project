import time
import threading
from coordinator.worker_registry import workers, mark_down

TIMEOUT = 8  # 秒

def monitor_heartbeats():
    while True:
        now = time.time()
        for wid, info in workers.items():
            if now - info["last_heartbeat"] > TIMEOUT:
                mark_down(wid)
                print(f"{wid} marked DOWN")
        time.sleep(2)

def start_monitor():
    t = threading.Thread(target=monitor_heartbeats, daemon=True)
    t.start()
