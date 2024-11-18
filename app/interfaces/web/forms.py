from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SubmitField
from wtforms.validators import DataRequired

class QuestionarioForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    idade = IntegerField('Idade', validators=[DataRequired()])
    transporte = FloatField('Gastos com Transporte (mensal)', validators=[DataRequired()])
    alimentacao = FloatField('Gastos com Alimentação (mensal)', validators=[DataRequired()])
    energia = FloatField('Gastos com Energia (mensal)', validators=[DataRequired()])
    submit = SubmitField('Calcular Pegada de Carbono')
