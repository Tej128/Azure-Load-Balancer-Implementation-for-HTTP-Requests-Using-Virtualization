from flask import Flask, request, jsonify
import requests
import random

app = Flask(__name__)

servers = ['public ip of server1', 'public ip of server2']

@app.route('/')
def balancer():
    selected_server = random.choice(servers)
    response = requests.get(selected_server + request.full_path)
    return response.content, response.status_code, response.headers.items()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
