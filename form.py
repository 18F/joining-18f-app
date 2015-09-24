from flask_wtf import Form
from wtforms import StringField, BooleanField, SelectField, TextAreaField
from flask_wtf.file import FileField
from wtforms.validators import DataRequired, Email, URL
from werkzeug import secure_filename

class ApplicationForm(Form):
    name = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(),Email()])
    phone = StringField('phone')
    city = StringField('city')
    state = StringField('state')
    zipcode = StringField('zipcode')
    citizenship = BooleanField('citizenship')
    primary_skillset = SelectField('primary_skillset', choices=[
           ('Acquisition Specialist'),
           ('Back end developer'),
           ('Content Strategist'),
           ('Content Writer'),
           ('Data Architect'),
           ('DevOps Engineer'),
           ('Front end developer'),
           ('Full stack developer'),
           ('Product Lead'),
           ('Project / Program Manager'),
           ('UX Research and Design'),
           ('Technical Architect'),
           ('Technical Recruiter'),
           ('Visual Designer'),
        ]);
    other_skills = TextAreaField('other_skills')
    link1 = StringField('link1', validators=[URL()])
    link2 = StringField('link2', validators=[URL()])
    link3 = StringField('link3', validators=[URL()])
    why_join_18f = TextAreaField('why_join_18f')

