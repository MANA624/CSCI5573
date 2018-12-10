import requests
import json

machines = ["http://73.169.9.236:4000",
            "http://therealpi.net:80",
            "http://192.168.10.107:4010"]

def send_source(machine_addr):
    filename = "test_program.py"
    with open(filename, 'r') as reader:
        source = reader.read()
    r = requests.post(machine_addr, data={"source": source})
    return r

# Requests a heartbeat status from all known servers and returns a dictionary
# mapping machine addresses to their heartbeat struct
def request_heartbeats():
    machine_heartbeats = {}

    for machine in machines:
        r = requests.get(machine + "/heartbeat", {})
        machine_heartbeats[machine] = json.loads(r.content)

    return machine_heartbeats

def main():
    heartbeats = request_heartbeats()

    highest_idle_cpu = sorted(heartbeats.items(),
                                 key = lambda kv: kv[1]["cpuIdlePct"],
                                 reverse = True)[0][0]

    print("Sending task to machine at: " + highest_idle_cpu)

    response = send_source(highest_idle_cpu)
    print(response.status_code, '\t:\t', response.text)

if __name__ in "__main__":
    main()
