import pandas as pd
import numpy as np
import csv
import joblib
from flask import Flask, render_template, request
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

app = Flask(__name__)

def predict_ckd(row_data, model):
    # perform some calculations or predictions on the input data
    # loaded_model = joblib.load('RF_trained_model.joblib')
    # prediction_from_loaded_model = loaded_model.predict(row_data)
    prediction_from_loaded_model = model.predict(row_data)
    if prediction_from_loaded_model == 0:
        result = "No Chronic Kidney Disease"
    else:
        result = "Chronic Kidney Disease"
    row_data.append(result)
    return row_data


@app.route('/', methods=['GET', 'POST'])
def landing():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return redirect(request.url)
        if file:
            loaded_model = joblib.load('RF_trained_model.joblib')
            #loaded_model = joblib.load('dtc_trained_model.joblib')
            file_data = pd.read_csv(file)
            file_data_df = pd.DataFrame(file_data)
            file_data_df.columns = ['age', 'blood_pressure', 'specific_gravity', 'albumin', 'sugar', 'red_blood_cells', 'pus_cell', 'pus_cell_clumps', 'bacteria', 'blood_glucose_random', 'blood_urea', 'serum_creatinine', 'sodium', 'potassium', 'haemoglobin', 'packed_cell_volume', 'white_blood_cell_count', 'red_blood_cell_count','hypertension', 'diabetes_mellitus', 'coronary_artery_disease', 'appetite', 'peda_edema','aanemia']
            cat_cols = ['red_blood_cells','pus_cell','pus_cell_clumps','bacteria','hypertension','diabetes_mellitus','coronary_artery_disease','appetite','peda_edema','aanemia']
            le = LabelEncoder()
            for col in cat_cols:
                file_data_df[col] = le.fit_transform(file_data_df[col])

            # Set feature names for the DecisionTreeClassifier
            loaded_model.feature_names = list(file_data_df.columns.values)
            prediction = loaded_model.predict(file_data_df)

            file_data_df['prediction'] = 'Chronic Kidney Disease' # default first

            for i in range(len(prediction)):
                x = prediction[i]
                file_data_df.loc[i, 'prediction'] = (lambda x: "No Chronic Kidney Disease" if x == 0 else "Chronic Kidney Disease")(x)

            return render_template('landing.html', file_data_df=file_data_df)
    else:
        return render_template('landing.html', file_data_df=None)


if __name__ == '__main__':
    app.run()
