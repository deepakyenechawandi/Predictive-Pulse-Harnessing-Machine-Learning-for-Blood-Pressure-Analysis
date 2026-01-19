import pandas as pd
from flask_wtf import FlaskForm
from wtforms import (
    SelectField,
    SubmitField  
)
from wtforms.validators import DataRequired

train = pd.read_csv('data/patient_data.csv')
X_data = train.drop(columns=['Stages'])

class InputForm(FlaskForm):
    Gender = SelectField(
        label="Gender",
        choices = ['Male',"Female"],
        validators=[DataRequired()]
    )
     
    Age = SelectField(
        label="Age",
        choices = ['18-34', '35-50', '51-64', '65+'],
        validators=[DataRequired()]
    )

    History = SelectField(
        label="History of Hypertension",
        choices = ['Yes',"No"],
        validators=[DataRequired()]
    )

    Patient = SelectField(
        label="Diagnosed Patient",
        choices = ['Yes',"No"],
        validators=[DataRequired()]
    )

    TakeMedication = SelectField(
        label=" Medication for Hypertension",
        choices = ['Yes',"No"],
        validators=[DataRequired()]
    )

    Severity = SelectField(
        label="Severity of the condition",
        choices = ['Mild', 'Moderate', 'Severe'],
        validators=[DataRequired()]
    )

    BreathShortness = SelectField(
        label="Experience shortness of breath",
        choices = ['Yes',"No"],
        validators=[DataRequired()]
    )

    VisualChanges = SelectField(
        label="Vision problems",
        choices = ['Yes',"No"],
        validators=[DataRequired()]
    )


    NoseBleeding = SelectField(
        label="Nose Bleeds",
        choices = ['Yes',"No"],
        validators=[DataRequired()]
    )


    Whendiagnoused = SelectField(
        label="How long ago the condition was diagnosed",
        choices = ['<1 Year', '1 - 5 Years', '>5 Years'],
        validators=[DataRequired()]
    )


    Systolic = SelectField(
        label="Systolic blood pressure range",
        choices = ['100+', '111 - 120', '121 - 130', '130+'],
        validators=[DataRequired()]
    )

    Diastolic = SelectField(
        label="Diastolic blood pressure range",
        choices = ['70 - 80', '81 - 90', '91 - 100', '100+', '130+'],
        validators=[DataRequired()]
    )

    ControlledDiet	 = SelectField(
        label="Conrtolled Diet",
        choices = ['yes',"No"],
        validators=[DataRequired()]
    )


    submit = SubmitField("Predict")