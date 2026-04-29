import json
import time

def collect_logs():
    logs = {
        "service": "network-gateway",
        "severity": "critical",
        "message": "Unauthorized access attempt",
        "timestamp": time.time()
    }

    with open("central_logs.json", "a") as f:
        f.write(json.dumps(logs) + "\n")

    print("Log forwarded to centralized storage")

collect_logs()
