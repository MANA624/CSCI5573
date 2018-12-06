# I don't think this file is necessary anymore,
# but I'll keep it around just for kicks

from flask import Flask, request

# Create the application instance
app = Flask(__name__, template_folder="templates")


# Create a URL route in our application for "/"
@app.route('/', methods=["GET", "POST"])
def home():
    results = request.form.get("output")
    if results:
        with open("results.txt", 'a+') as writer:
            writer.write(results)
            writer.write('\n')
        return "Message received!"
    else:
        return "No results found"

# Run the application
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
