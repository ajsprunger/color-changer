from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class RGBForm(FlaskForm):
  r = IntegerField('r', validators=[DataRequired()])
  g = IntegerField('g', validators=[DataRequired()])
  b = IntegerField('b', validators=[DataRequired()])
  submit = SubmitField('Go')