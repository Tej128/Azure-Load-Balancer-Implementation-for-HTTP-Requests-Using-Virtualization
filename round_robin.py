from flask import Flask, request
import requests

app = Flask(__name__)

# List of servers to balance between
servers = ['http://98.71.102.147:8080/', 'http://98.71.102.234:8080/']
current_server = 0  # Index to track the current server to use

@app.route('/')
def balancer():
    global current_server
    selected_server = servers[current_server]
    
    # Forward incoming request to the selected server
    response = requests.get(selected_server + request.path)
    
    # Rotate to the next server for the next request
    current_server = (current_server + 1) % len(servers)
    
    return response.content, response.status_code, response.headers.items()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
