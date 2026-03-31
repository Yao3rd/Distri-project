workers = [
    {"id": 1, "url": "http://localhost:9001", "capabilities": ["word_count", "keyword_search"], "status": "ALIVE"},
    {"id": 2, "url": "http://localhost:9002", "capabilities": ["sort_numbers", "prime_search"], "status": "ALIVE"},
    {"id": 3, "url": "http://localhost:9003", "capabilities": ["word_count", "keyword_search", "sort_numbers", "prime_search"], "status": "ALIVE"},
]

def get_workers():
    return workers
