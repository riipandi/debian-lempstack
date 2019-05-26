import re

from flask import current_app
from flask_wtf import FlaskForm
from wtforms import BooleanField, DecimalField, FloatField, IntegerField, \
    DateTimeField, DateField, \
    FileField, PasswordField, StringField, TextAreaField, \
    RadioField, SelectField, SelectMultipleField, \
    HiddenField, SubmitField
from wtforms.validators import InputRequired, Length
from wtforms import ValidationError
from .models import ItemModel


def filter_keyname(data):
    return re.sub('[^a-z0-9_-]', '', str(data).lower())

def validate_keyname(self, field):
    if field.data != self.item.keyname and \
            ItemModel.query.filter_by(keyname=field.data).first():
        raise ValidationError('Keyname already in use.')


class CreatItemForm(FlaskForm):
    keyname    = StringField('Keyname', validators=[InputRequired(),Length(2,63),validate_keyname], filters=[filter_keyname])
    item_title = StringField('Title', validators=[InputRequired(),Length(1,255)])
    submit     = SubmitField('Create Item')

    def __init__(self, item, *args, **kwargs):
        super(CreatItemForm, self).__init__(*args, **kwargs)
        self.item = item


class EditItemForm(FlaskForm):
    id          = HiddenField('id')
    keyname     = StringField('Keyname', validators=[InputRequired(),Length(2,63),validate_keyname], filters=[filter_keyname])
    item_status = SelectField('Item Status', choices=[], coerce=int)
    item_title  = StringField('Title', validators=[InputRequired(),Length(1,255)])
    item_text   = TextAreaField('Text')
    mod_create  = DateTimeField('Item Created')
    mod_update  = DateTimeField('Item Updated')
    owner_id    = SelectField('Item Owner', choices=[], coerce=int)
    users_id    = SelectMultipleField('Editors', choices=[], coerce=int)
    submit      = SubmitField('Update Item')

    def __init__(self, item, *args, **kwargs):
        super(EditItemForm, self).__init__(*args, **kwargs)
        self.item_status.choices = [
            (current_app.config['ITEM_STATUS_DRAFT'], current_app.config['ITEM_STATUS'][current_app.config['ITEM_STATUS_DRAFT']]),
            (current_app.config['ITEM_STATUS_COMPLETED'], current_app.config['ITEM_STATUS'][current_app.config['ITEM_STATUS_COMPLETED']]),
            (current_app.config['ITEM_STATUS_APPROVED'],current_app.config['ITEM_STATUS'][current_app.config['ITEM_STATUS_APPROVED']]),
            (current_app.config['ITEM_STATUS_HIDDEN'], current_app.config['ITEM_STATUS'][current_app.config['ITEM_STATUS_HIDDEN']]),
            ]
        self.item = item

