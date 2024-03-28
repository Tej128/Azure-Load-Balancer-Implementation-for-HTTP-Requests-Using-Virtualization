from flask import Flask, request
import requests

app = Flask(__name__)

# List of servers to balance between with corresponding weights
servers = [
    {'url': 'public ip weight of server1': 7},
    {'url': 'public ip of server2', 'weight': 8}
]

# Generate a weighted server list
weighted_servers = []
for server in servers:
    weighted_servers.extend([server['url']] * server['weight'])

current_index = 0  # Index to track the current server to use

@app.route('/')
def balancer():
    global current_index
    selected_server = weighted_servers[current_index]
    
    # Forward incoming request to the selected server
    response = requests.get(selected_server + request.path)
    
    # Rotate to the next server for the next request
    current_index = (current_index + 1) % len(weighted_servers)
    
    return response.content, response.status_code, response.headers.items()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
