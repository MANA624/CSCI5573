import requests


def send_source():
    filename = "test_program.py"
    with open(filename, 'r') as reader:
        source = reader.read()
    r = requests.post("http://therealpi.net", data={"source": source})
    return r


def main():
    response = send_source()
    print(response.status_code, '\t:\t', response.text)


if __name__ in "__main__":
    main()
