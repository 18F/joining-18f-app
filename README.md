# joining-18f-app
The 18F application form

## Installing

After you've cloned this repo and made a Virtualenv with Python 3.x, run:
    
    pip install -r requirements.txt

## Configuring

You'll need to make your own local settings file and populate it with a secret key.

    cp settings_local.example.py settings_local.py

Then fire up Python and generate a key to copy and paste into the value of `JOINING_18F_APP_SECRET_KEY` in that file.

    python
    >>> import os; os.urandom(24)

## Running

You'll need to let Flask know where your local config file is, so run the server like so:

    JOINING_18F_APP_SETTINGS=settings_local.py python run.py

Then you should be able to access the app at `http://localhost:5000`.
