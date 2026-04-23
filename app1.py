import streamlit as st
import numpy as np
import pickle

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AI Fraud Detection System",
    page_icon="💳",
    layout="wide"
)

# ---------------- STYLE ---------------- #

st.markdown("""
<style>

.stApp{
background: linear-gradient(135deg,#0f172a,#1e293b);
color:white;
}

.title{
font-size:38px;
font-weight:bold;
text-align:center;
padding:20px;
background:linear-gradient(90deg,#00c6ff,#0072ff);
border-radius:12px;
}

.metric-card{
background:#1e293b;
padding:15px;
border-radius:10px;
text-align:center;
box-shadow:0px 4px 20px rgba(0,0,0,0.4);
}

</style>
""",unsafe_allow_html=True)

# ---------------- LOAD MODEL ---------------- #

model = pickle.load(open("trained_model.sav","rb"))
scaler = pickle.load(open("scaler.sav","rb"))

# ---------------- HEADER ---------------- #

st.markdown('<div class="title">💳 AI Credit Card Fraud Detection Dashboard</div>',unsafe_allow_html=True)

st.write("")

col1,col2,col3 = st.columns(3)

with col1:
    st.markdown('<div class="metric-card">⚡ Real Time Detection</div>',unsafe_allow_html=True)

with col2:
    st.markdown('<div class="metric-card">🧠 Machine Learning Model</div>',unsafe_allow_html=True)

with col3:
    st.markdown('<div class="metric-card">🔒 Secure Monitoring</div>',unsafe_allow_html=True)

st.write("")
st.write("")

# ---------------- DEMO DATA ---------------- #

fraud_demo = [
938.00,
-5.31,4.28,-3.90,1.77,-1.72,-1.73,
-4.64,2.09,-2.55,-3.73,3.45,-2.90,
-0.82,-5.00,0.42,-2.10,-4.20,-1.75,
0.32,0.37,0.88,-0.42,-0.75,0.18,
0.23,0.51,0.70,-0.33,
0.00
]

normal_demo = [
10000.00,
0.25,-0.10,1.20,0.30,0.50,0.20,
0.15,0.05,0.10,0.20,0.05,0.10,
0.20,0.15,0.10,0.05,0.02,0.03,
0.01,0.05,0.02,0.01,0.03,0.04,
0.02,0.03,0.01,0.02,
120.00
]

# ---------------- DEMO BUTTONS ---------------- #

demo1,demo2 = st.columns(2)

if demo1.button("🟢 Load Normal Transaction"):
    for i,val in enumerate(normal_demo):
        st.session_state[f"f{i}"] = val

if demo2.button("🔴 Load Fraud Transaction"):
    for i,val in enumerate(fraud_demo):
        st.session_state[f"f{i}"] = val

st.write("")

# ---------------- INPUT FIELDS ---------------- #

st.subheader("Transaction Details")

feature_names = [
"Time","V1","V2","V3","V4","V5","V6","V7","V8","V9","V10",
"V11","V12","V13","V14","V15","V16","V17","V18","V19",
"V20","V21","V22","V23","V24","V25","V26","V27","V28","Amount"
]

features = []

col1,col2 = st.columns(2)

for i,name in enumerate(feature_names):

    if i < 15:
        with col1:
            val = st.number_input(name,key=f"f{i}",value=0.0,format="%.2f")
    else:
        with col2:
            val = st.number_input(name,key=f"f{i}",value=0.0,format="%.2f")

    features.append(val)

st.write("")

# ---------------- PREDICTION ---------------- #

if st.button("🚨 Detect Fraud"):

    arr = np.array(features).reshape(1,-1)

    arr_scaled = scaler.transform(arr)

    pred = model.predict(arr_scaled)[0]

    probs = model.predict_proba(arr_scaled)[0]

    fraud_index = list(model.classes_).index(1)

    prob = float(probs[fraud_index])

    st.subheader("Fraud Risk Score")

    st.progress(prob)

    st.write(f"Fraud Probability: **{prob*100:.2f}%**")

    if prob < 0.30:
        st.success("🟢 Low Risk Transaction")

    elif prob < 0.70:
        st.warning("🟡 Medium Risk Transaction")

    else:
        st.error("🔴 High Risk Transaction")

    if pred == 1:
        st.error("🚨 Fraudulent Transaction Detected")
        st.balloons()
    else:
        st.success("✅ Legitimate Transaction")