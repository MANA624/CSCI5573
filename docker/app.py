from flask import Flask, request, jsonify
import os
import socket
import requests
import heartbeat
import docker

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello():
    # Spin off new container
    client = docker.from_env()
    seed = request.form.get("seed")
    result = client.containers.run("dockertest_pi", seed)
    return jsonify(results=result.decode().rstrip())

@app.route("/heartbeat", methods=["GET"])
def heart():
    results = heartbeat.collect_heartbeat()
    return jsonify(results)

if __name__ == "__main__":
    print(heartbeat.collect_heartbeat())
    app.run(host='0.0.0.0', port=4010)
