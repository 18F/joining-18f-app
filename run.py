from flask import Flask
app = Flask(__name__)

@app.route('/')
def apply():
    return "Apply to 18F!"

if __name__ == '__main__':
    app.run()
