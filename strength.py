import pandas as pd
import numpy as np

df = pd.read_csv('diabetes.csv')

X = df.iloc[:, :-1]
y = df['Outcome']

# Train, Test split
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=7)

# Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier

rf_clf = RandomForestClassifier()

rf_clf.fit(X_train, y_train)

df_test = pd.read_csv('diabetes.csv')

X_acutal_test = df_test.iloc[:, :-1]
y_actual_test = df_test['Outcome']

symptoms_dict = {}

for index, symptom in enumerate(X):
    symptoms_dict[symptom] = index

input_vector = np.zeros(len(symptoms_dict))


