import requests

WORKER_URL = "http://127.0.0.1:9000/execute"

def send_task_to_worker(task):
    try:
        response = requests.post(WORKER_URL, json=task)
        return response.json()
    except Exception as e:
        return {"error": str(e)}
