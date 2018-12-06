from flask import Flask, request
import os
import socket
import requests
import numpy
import austinsfile

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello():
    error = 0
    
    source = request.form.get("source")
    print(source)

    # TODO: Spin off new container


    ### r = requests.post("http://192.168.0.16:5000", data={"output": "Hello world!"})    

    if not error:
        return "Hello world!", 200
    else:
        return "No", 500


@app.route("/heartbeat")
def heart():
    results = austinsfile.heart()
    return results

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)

