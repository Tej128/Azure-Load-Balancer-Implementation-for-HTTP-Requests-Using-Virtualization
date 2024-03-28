from flask import Flask, request
import os
import requests

app = Flask(__name__)

ip_server1 = "+=+=+="  # Replace with your server 1 IP and port
ip_server2 = "+=+=+="  # Replace with your server 2 IP and port

@app.route('/')
def load_sense():
    load_response1 = requests.get(f'http://{ip_server1}/load').text
    load_response2 = requests.get(f'http://{ip_server2}/load').text
    
    # Extracting the numeric value from the response
    load_server1 = float(load_response1.split(': ')[1])
    load_server2 = float(load_response2.split(': ')[1])
    
    if load_server1 <= load_server2:
        load_result = requests.get(f'http://{ip_server1}')
        chosen_server = "Server 1"
        return load_result.text
    else:
        load_result = requests.get(f'http://{ip_server2}')
        chosen_server = "Server 2"
        return load_result.text

@app.route('/load')
def show_load():
    load_server1 = float(requests.get(f'http://{ip_server1}/load').text.split(': ')[1])
    load_server2 = float(requests.get(f'http://{ip_server2}/load').text.split(': ')[1])
    return f'load on server1={load_server1}, load on server2={load_server2}'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000)
