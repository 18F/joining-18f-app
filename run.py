from flask import Flask
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('JOINING_18F_APP_SETTINGS')

@app.route('/')
def apply():
    return "Apply to 18F!"

if __name__ == '__main__':
    app.run()
