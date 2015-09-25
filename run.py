from flask import Flask, render_template, request, redirect
from form import ApplicationForm
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('JOINING_18F_APP_SETTINGS')


@app.route('/', methods=('GET', 'POST'))
def apply():
    form = ApplicationForm()
#    if form.validate_on_submit():  # This never gets reached.
    if request.method == 'POST':    # Temporarily forcing this until validation works.
        application_content = stringify_form_submission(form)
        title = form['name'].data
        create_google_doc(title, application_content)
        return redirect('/success')
    return render_template('form.html', form=form)


@app.route('/success')
def success():
    return render_template('success.html')


def stringify_form_submission(form):
    stringified_form_submission = ''

    for fieldname, value in form.data.items():
        stringified_form_submission += '{}: {}\n'.format(fieldname, value)

    return stringified_form_submission


def create_google_doc(title, application_content):
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)

    test_file = drive.CreateFile({'title': '{}.txt'.format(title)})
    test_file.SetContentString(application_content)
    test_file.Upload()

    return None

if __name__ == '__main__':
    app.run(debug=True)
