import streamlit as st
import pickle
import numpy as np

# Load the saved Random Forest model
model = pickle.load(open('classifyModel.pkl', 'rb'))

# Streamlit app with custom HTML and CSS
st.markdown("""
    <style>
    body {
        background-color: #f4f4f9;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
    }
    .stButton button:hover {
        background-color: #43a049;
    }
    .header {
        background-color: #282c34;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
    }
    .header h1 {
        color: white;
    }
    .footer {
        text-align: center;
        margin-top: 30px;
        font-size: 14px;
        color: #666666;
    }
    .output-box {
        background-color: #282c34;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin-top: 20px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Header section
st.markdown("""
    <div class="header">
        <h1>🌊 Water Quality Classifier</h1>
        <p style="color: #b0bec5;">Analyze water safety based on its characteristics</p>
    </div>
""", unsafe_allow_html=True)

# Input fields in rows
st.markdown("### Enter Water Parameters Below")

col1, col2 = st.columns(2)
with col1:
    ph = st.number_input("pH Level (1-14)", min_value=0.0, max_value=14.0, value=7.0, step=0.1)
    hardness = st.number_input("Hardness (mg/L)", value=150.0, step=0.1)
    solids = st.number_input("Solids (mg/L)", value=50000.0, step=1.0)

with col2:
    chloramines = st.number_input("Chloramines (mg/L)", value=5.0, step=0.1)
    sulfate = st.number_input("Sulfate (mg/L)", value=300.0, step=0.1)
    conductivity = st.number_input("Conductivity (μS/cm)", value=400.0, step=0.1)

col3, col4 = st.columns(2)
with col3:
    organic_carbon = st.number_input("Organic Carbon (mg/L)", value=10.0, step=0.1)
    turbidity = st.number_input("Turbidity (NTU)", value=4.0, step=0.1)

with col4:
    trihalomethanes = st.number_input("Trihalomethanes (μg/L)", value=60.0, step=0.1)

# Combine inputs into a single array
input_data = np.array([ph, hardness, solids, chloramines, sulfate, conductivity, 
                       organic_carbon, trihalomethanes, turbidity]).reshape(1, -1)

# Predict button
if st.button("Predict Water Quality"):
    prediction = model.predict(input_data)
    quality = "Safe" if prediction[0] == 1 else "Not Safe"
    
    # Display result in a styled box
    st.markdown(f"""
        <div class="output-box">
            <h3>The water quality is: <span style="color:blue;">{quality}</span></h3>
        </div>
    """, unsafe_allow_html=True)

# Footer section
st.markdown("""
    <div class="footer">
        Built with ❤️ using <a href="https://streamlit.io/" target="_blank">Streamlit</a>
    </div>
""", unsafe_allow_html=True)
