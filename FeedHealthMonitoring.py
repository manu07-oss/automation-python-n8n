import requests

CRITICAL_FEEDS = [
    "https://api.service1.com/health",
    "https://api.service2.com/health"
]

def monitor_feeds():
    for feed in CRITICAL_FEEDS:
        try:
            r = requests.get(feed, timeout=5)
            if r.status_code != 200:
                raise Exception("Feed unhealthy")

            print(f"{feed} Healthy")

        except Exception:
            print(f"{feed} Down")
            create_ticket(feed)

def create_ticket(feed):
    print(f"Incident created for {feed}")

monitor_feeds()
