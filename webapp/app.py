from flask import Flask
import hvac
import requests
import json

app = Flask(__name__)

# Vault client
client = hvac.Client(url='http://127.0.0.1:8200')
client.token = 'root'
secret = client.secrets.kv.v2.read_secret_version(path='webapp/config')

username = secret['data']['data']['username']
password = secret['data']['data']['password']

@app.route('/')
def index():
    return f"Username: {username}, Password: {password}"

def register_service():
    # Register service with Consul
    service_payload = {
        "Name": "web",
        "Tags": ["web"],
        "Port": 80,
        "Address": "127.0.0.1"
    }
    requests.put("http://127.0.0.1:8500/v1/agent/service/register", data=json.dumps(service_payload))

if __name__ == '__main__':
    register_service()
    app.run(host='0.0.0.0', port=80)

