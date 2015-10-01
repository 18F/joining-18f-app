from flask import Flask, render_template, flash
from form import ApplicationForm

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('JOINING_18F_APP_SETTINGS')

@app.route('/', methods=('GET', 'POST'))
def apply():
    form = ApplicationForm()
    if form.validate_on_submit():
        return redirect('/success')
    else:
        flash_errors(form)
    return render_template('form.html', form=form)

@app.route('/success')
def success():
    return render_template('success.html')

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (getattr(form, field).label.text, error), 'error')

if __name__ == '__main__':
    app.run(debug=True)
