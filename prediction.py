import numpy as np
import pickle
import streamlit

model = pickle.load(open("trained_model.sav", "rb"))
scaler = pickle.load(open("scaler.sav", "rb"))

sample = X_test.iloc[0].values.reshape(1,-1)

sample_scaled = scaler.transform(sample)

prediction = model.predict(sample_scaled)

if prediction[0] == 0:
    print("Normal Transaction")
else:
    print("Fraudulent Transaction")