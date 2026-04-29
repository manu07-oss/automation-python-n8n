# (ServiceNow API Example)
import requests

url="https://instance.service-now.com/api/now/table/incident"

payload={
 "short_description":"Critical Feed Failure",
 "priority":"1"
}

headers={
 "Content-Type":"application/json"
}

r=requests.post(
 url,
 json=payload,
 headers=headers,
 auth=("user","password")
)

print(r.status_code)
