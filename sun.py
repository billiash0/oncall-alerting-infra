import urllib.request, json

data = json.dumps({
    "stack_id": 1,
    "org_id": 1,
    "grafana_url": "http://oncall-grafana:3000",
    "grafana_token": "test"
}).encode()

req = urllib.request.Request(
    "http://localhost:8080/api/internal/v1/plugin/v2/install",
    data=data,
    headers={"Content-Type": "application/json"},
    method="POST"
)

try:
    resp = urllib.request.urlopen(req)
    print("OK:", resp.read())
except Exception as e:
    print("ERROR:", e.read())