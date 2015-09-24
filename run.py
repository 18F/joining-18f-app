from flask import Flask, render_template
from form import ApplicationForm

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('JOINING_18F_APP_SETTINGS')

@app.route('/', methods=('GET', 'POST'))
def apply():
    form = ApplicationForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('form.html', form=form)

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
