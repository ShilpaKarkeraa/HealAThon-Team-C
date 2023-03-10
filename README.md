# HealAThon-Team-C
#### Team: Evan / evan.low@illumetechnology.com

# Saving Kidneys using AI: Earlier Detection of Chronic Kidney Disease Using Machine Learning

#### Goal: 
To Develop a Machine Learning Model to detect early stages of Chronic Kidney Disease (CKD) using clinical data to assist healthcare providers in identifying patients at risk for CKD, allowing for earlier interventions and potentially better outcomes.

<p>
This is a machine learning project that aims to classify chronic kidney disease (CKD) using a decision tree classifier algorithm as well as a random forest classifier algorithm. 
</p>
   
<p>
The project performs various data cleaning and exploratory data analysis (EDA) steps before building a decision tree model, such as replacing null/NaN values, handling outliers, and visualizing the data. After cleaning and analyzing the data, the data is split into training and test datasets and fit through the 2 different models. Both models are evaluated using the test dataset, and accuracy scores, confusion matrices, and classification reports are compared.
</p>
<p>
Using the python joblib library, the trained model can be exported and transferred to be imported in other external programs used to predict CKD using the same data inputs.
</p>


2 files are needed to run: 
- CKD_classification.ipynb
- chronic_kidney_disease.csv (datafile)



The program execution will produce the following joblib files
- dtc_trained_model.joblib
- RF_trained_model.joblib
intended to be fed into the demo flask web application
