from xmlrpc.server import SimpleXMLRPCServer

def execute_task(task):
    task_type = task["type"]

    if task_type == "word_count":
        result = "word count = 100"
    elif task_type == "sort_numbers":
        result = "sorted result"
    else:
        result = "default"

    return {"status": "SUCCESS", "result": result}

def start_server(port):
    server = SimpleXMLRPCServer(("localhost", port))
    print(f"Worker running on {port}")
    server.register_function(execute_task, "execute_task")
    server.serve_forever()
