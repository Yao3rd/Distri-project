def select_worker(task_type, workers):
    for worker in workers:
        if task_type in worker["capabilities"] and worker["status"] == "ALIVE":
            return worker
    return None
