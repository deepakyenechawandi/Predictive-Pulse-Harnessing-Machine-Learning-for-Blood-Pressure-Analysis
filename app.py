import pandas as pd
import joblib
from flask import (
    Flask,
    url_for,
    render_template
)
from forms import InputForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_key"

model = joblib.load("model.joblib")

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    form = InputForm()
    if form.validate_on_submit():
        x_new = pd.DataFrame(dict(
            Gender=[form.Gender.data],
            Age=[form.Age.data],
            History=[form.History.data],
            Patient=[form.Patient.data],
            TakeMedication=[form.TakeMedication.data],
            Severity=[form.Severity.data],
            BreathShortness=[form.BreathShortness.data],
            VisualChanges=[form.VisualChanges.data],
            NoseBleeding=[form.NoseBleeding.data],
            Whendiagnoused=[form.Whendiagnoused.data],
            Systolic=[form.Systolic.data],
            Diastolic=[form.Diastolic.data],
            ControlledDiet=[form.ControlledDiet.data]
        ))

        # ✅ Predict
        prediction = model.predict(x_new)[0]

        # ✅ Map numeric prediction to stage label
        stage_map = {
            0: "NORMAL",
            1: "HYPERTENSION (Stage-1)",
            2: "HYPERTENSION (Stage-2)",
            3: "HYPERTENSIVE CRISIS"
        }

        stage_label = stage_map.get(prediction, "Unknown")

        # ✅ Final message
        message = f"Based on the provided details, your blood pressure stage is {stage_label}."
    else:
        message = "Please provide valid input details!"

    return render_template("predict.html", title="Predict", form=form, output=message)


if __name__ == "__main__":
    app.run(debug=True, port=10000)
