blacklisted_ips=[
 "192.168.1.22",
 "10.2.1.9"
]

def detect_fraud(ip):
    if ip in blacklisted_ips:
        return "Fraud Suspected"

    return "Clean"

print(detect_fraud("192.168.1.22"))
