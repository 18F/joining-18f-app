from flask_wtf import Form
from wtforms import StringField, BooleanField, SelectField, TextAreaField, RadioField
from flask_wtf.file import FileField
from wtforms.validators import DataRequired, Email, URL
from werkzeug import secure_filename

class ApplicationForm(Form):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone')
    city = StringField('City')
    state = StringField('State')
    zipcode = StringField('Zip Code')
    citizenship = BooleanField('Verify you are a U.S. Citizen or Green Card holder')
    primary_skillset = SelectField('Please indicate your primary skillset. Your response here will be used primarily in assigning reviewers for your application.', choices=[
           ('acquisition_specialist', 'Acquisition Specialist'),
           ('back_end_developer', 'Back End Developer'),
           ('content_strategist', 'Content Strategist'),
           ('content_writer', 'Content Writer'),
           ('data_architect', 'Data Architect'),
           ('devops_engineer', 'DevOps Engineer'),
           ('front_end_developer', 'Front End Developer'),
           ('full_stack_developer', 'Full Stack Developer'),
           ('product_lead', 'Product Lead'),
           ('project_or_program_manager', 'Project / Program Manager'),
           ('ux_research_and_design', 'UX Research and Design'),
           ('technical_architect', 'Technical Architect'),
           ('technical_recruiter', 'Technical Recruiter'),
           ('visual_designer', 'Visual Designer'),
        ])
    other_skills = TextAreaField('Other skills you have')
    link1 = StringField('Link 1', validators=[URL()])
    link2 = StringField('Link 2', validators=[URL()])
    link3 = StringField('Link 3', validators=[URL()])
    why_join_18f = TextAreaField('Why do you want to join 18F?')
    resume = TextAreaField('Resume')
    fulltime_ok = BooleanField('Verify your ability to work full-time')
    location_pref = SelectField('Select your preferred work location', choices=[
            ('chi', 'Chicago'),
            ('ny', 'New York'),
            ('sf', 'San Francisco'),
            ('dc', 'Washington, DC'),
            ('rmt', 'Remote')
        ])
    is_veteran = RadioField('Are you a Veteran of the U.S. Armed Forces or are you eligible for "derived" <a target="_blank" href="http://www.opm.gov/StaffingPortal/vetguide.asp#2Types">preference</a>?',
            choices=[('', 'No'), ('yes', 'Yes')])
    veteran_pref_type = RadioField('', choices=[
            ('none', 'No, I do not claim Veterans\' Preference.'),
            ('ssp', '0-point Sole Survivorship Preference (SSP).'),
            ('tp', '5-point preference based on active duty in the U.S. Armed Forces (TP).'),
            ('cp', '10-point preference based on a compensable service connected disability of at least 10% but less than 30% (CP).'),
            ('cps', '10-point preference based on a compensable service connected disability of 30% or more (CPS).'),
            ('xp', '10-point preference for non-compensable disability or Purple Heart (XP).'),
            ('xp2', '10-point preference based on widow/widower or mother of a deceased veteran, or spouse or mother of a disabled veteran (XP).'),
        ])
    addl_opps = BooleanField('Please also consider me for other employment opportunities within the US government.')
    where_they_found_us = TextAreaField('Where did you learn about 18F?')


