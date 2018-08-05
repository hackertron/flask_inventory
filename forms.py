from wtforms import Form, StringField, TextAreaField, PasswordField, validators, BooleanField, HiddenField


#  Register Form Class
class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')


# user_info
class user_info(Form):
    user_id = HiddenField('user_id')
    org_name = StringField('Org_name', [validators.Length(min=1, max=50)])
    contact_person = StringField('Contact_person', [validators.Length(min=4, max=50)])
    contact_email = StringField('Contact_email', [validators.Length(min=10, max=100)])
    contact_no = StringField('Contact_no', [validators.DataRequired(), validators.Length(min=10, max=10)])
    address = StringField('Address', [validators.Length(min=10, max=500)])
    state = StringField('State', [validators.Length(min=3, max=30)])
    pin_code = StringField('Pin_code', [validators.Length(min=6, max=6)])
    city = StringField('City', [validators.Length(min=3, max =50)])
    country = StringField('Country', [validators.Length(min=3, max=30)])
    GSTIN_number = StringField('GSTIN_num', [validators.Length(min=15, max=15)])
    serial_key_2 = StringField('Serial_key_2', [validators.Length(min=5, max=30)])
    package = StringField('Package', [validators.DataRequired()])
    tally = BooleanField('Tally')
    busy = BooleanField('Busy')
    openoffice = BooleanField('Openoffice')
    username1 = StringField('Username1', [validators.Length(min=3, max=30)])
    username2 = StringField('Username2', [validators.Length(min=3, max=30)])
    username3 = StringField('Username3', [validators.Length(min=3, max=30)])


# Skill Form Class
class SkillForm(Form):
    skill_name = StringField('skill_name', [validators.Length(min=1, max=100)])


# Article Form Class
class RecommendForm(Form):
    title = StringField('Title', [validators.Length(min=1, max=200)])
    body = TextAreaField('Body', [validators.Length(min=30)])
