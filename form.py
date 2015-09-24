from flask_wtf import Form
from wtforms import StringField, BooleanField, SelectField, TextAreaField, RadioField
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
           ('acquisition_specialist', 'Acquisition Specialist'),
           ('back_end_developer', 'Back end developer'),
           ('content_strategist', 'Content Strategist'),
           ('content_writer', 'Content Writer'),
           ('data_architect', 'Data Architect'),
           ('devops_engineer', 'DevOps Engineer'),
           ('front_end_developer', 'Front end developer'),
           ('full_stack_developer', 'Full stack developer'),
           ('product_lead', 'Product Lead'),
           ('project_or_program_manager', 'Project / Program Manager'),
           ('ux_research_and_design', 'UX Research and Design'),
           ('technical_architect', 'Technical Architect'),
           ('technical_recruiter', 'Technical Recruiter'),
           ('visual_designer', 'Visual Designer'),
        ])
    other_skills = TextAreaField('other_skills')
    link1 = StringField('link1', validators=[URL()])
    link2 = StringField('link2', validators=[URL()])
    link3 = StringField('link3', validators=[URL()])
    why_join_18f = TextAreaField('why_join_18f')
    resume = TextAreaField('resume')
    fulltime_ok = BooleanField('fulltime_ok')
    location_pref = SelectField('location_pref', choices=[
            ('chi', 'Chicago'),
            ('ny', 'New York'),
            ('sf', 'San Francisco'),
            ('dc', 'Washington, DC'),
            ('rmt', 'Remote')
        ])
    is_veteran = RadioField('Are you a Veteran of the U.S. Armed Forces or are you eligible for "derived" preference?',
            choices=[('', 'No'), ('yes', 'Yes')])
    veteran_pref_type = RadioField('veteran_pref_type', choices=[
            ('none', 'No, I do not claim Veterans\' Preference.'),
            ('ssp', '0-point Sole Survivorship Preference (SSP).'),
            ('tp', '5-point preference based on active duty in the U.S. Armed Forces (TP).'),
            ('cp', '10-point preference based on a compensable service connected disability of at least 10% but less than 30% (CP).'),
            ('cps', '10-point preference based on a compensable service connected disability of 30% or more (CPS).'),
            ('xp', '10-point preference for non-compensable disability or Purple Heart (XP).'),
            ('xp2', '10-point preference based on widow/widower or mother of a deceased veteran, or spouse or mother of a disabled veteran (XP).'),
        ])
    addl_opps = BooleanField('addl_opps')
    where_they_found_us = TextAreaField('where_they_found_us')


