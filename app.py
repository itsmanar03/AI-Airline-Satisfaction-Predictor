import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
import base64

img = Image.open("logo.png")

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
background_image = get_base64("background.jpg")

st.set_page_config(
    page_title="AI Airline Satisfaction Dashboard",
    page_icon=img,
    layout="wide",
    initial_sidebar_state="expanded"
)

# LOAD MODEL FILES
model = joblib.load("xgb_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")
model_columns = joblib.load("model_columns.pkl")

# THEME COLORS
background = "#0a0a0a"
card_bg = "#1a1a1a"
sidebar_bg = "#111111"

text_color = "#FFD700"
muted_text = "#a2a2a2"

border_color = "#FFD700"

input_bg = "#1f1f1f"
secondary_bg = "#222222"

button_1 = "#FFD700"
button_2 = "#b8860b"

chart_bg = "#0a0a0a"

# CUSTOM CSS
st.markdown(
    f"""
    <style>
    html, body, [class*="css"] {{
        font-family: 'Poppins', sans-serif;
    }}

.stApp {{
    background-image:
        linear-gradient(rgba(0,0,0,0.78), rgba(0,0,0,0.78)),
        url("data:image/jpg;base64,{background_image}");

    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;

    color: #FFD700;
}}

    section[data-testid="stSidebar"] {{
        background: {sidebar_bg};
        border-right: 1px solid {border_color};
    }}

    section[data-testid="stSidebar"] * {{
        color: {text_color} !important;
    }}

    h1 {{
        font-size: 3.2rem !important;
        font-weight: 800 !important;
        letter-spacing: -1px;
        color: {text_color};
    }}

    h2, h3 {{
        font-weight: 700 !important;
        color: {text_color};
    }}

    p, label, span {{
        color: {muted_text} !important;
    }}

    hr {{
        border-color: {border_color};
    }}

    /* BUTTONS */
    .stButton > button {{
        background: linear-gradient(135deg, {button_1}, {button_2});
        color: black;
        border: none;
        border-radius: 14px;
        padding: 0.9rem 1rem;
        font-size: 15px;
        font-weight: 600;
        transition: 0.3s ease;
        width: 100%;
        box-shadow: 0px 4px 14px rgba(255,215,0,0.3);
    }}

    .stButton > button:hover {{
        transform: translateY(-2px);
        opacity: 0.95;
    }}

    /* INPUTS */
    .stNumberInput input,
    .stTextInput input {{
        background: {input_bg} !important;
        color: {text_color} !important;
        border-radius: 14px !important;
        border: 1px solid {border_color} !important;
    }}

    .stSelectbox div[data-baseweb="select"] {{
        background: {input_bg} !important;
        border-radius: 14px !important;
        border: 1px solid {border_color} !important;
    }}

    .stSelectbox * {{
        color: {text_color} !important;
    }}

    /* METRIC CARDS */
    .metric-card {{
        background: {card_bg};
        padding: 32px;
        border-radius: 24px;
        border: 1px solid {border_color};
        text-align: center;
        transition: 0.3s ease;
        box-shadow: 0px 8px 24px rgba(255,215,0,0.15);
    }}

    .metric-card:hover {{
        transform: translateY(-4px);
    }}

    .metric-card h2 {{
        font-size: 40px;
        font-weight: 800;
        color: {text_color} !important;
    }}

    .metric-card h3 {{
        color: {button_1} !important;
        font-size: 18px;
        margin-bottom: 14px;
    }}

    /* PREDICTION BOX */
    .prediction-box {{
        background: linear-gradient(135deg, {button_1}, {button_2});
        padding: 36px;
        border-radius: 24px;
        text-align: center;
        color: #000000 !important;
        font-weight: 800;
        box-shadow: 0px 8px 24px rgba(255,215,0,0.3);
    }}

    .prediction-box h1, .prediction-box h2 {{
        color: #000000 !important;
        margin: 0;
    }}

    /* RECOMMENDATION BOX */
    .recommendation-box {{
        background: {secondary_bg};
        padding: 24px;
        border-radius: 18px;
        border-left: 5px solid {button_1};
        color: {text_color};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# SIDEBAR CONTENT
st.sidebar.title("Dashboard Settings")
st.sidebar.metric("Model Accuracy", "96.2%")
st.sidebar.metric("Dataset Rows", "25,976")
st.sidebar.metric("Features", len(model_columns))

st.sidebar.markdown("""
### About The System
This dashboard uses Machine Learning to analyze airline passenger satisfaction.
""")

# LOGO SECTION
col1, col2 = st.columns([1, 5])

with col1:
    st.image("logo.png", width=120)

with col2:
    st.title("AI Airline Satisfaction Dashboard")
    st.markdown("### AI-powered passenger satisfaction prediction system")

# MAIN HEADER
st.markdown("Analyze customer satisfaction.")

st.divider()


# KPI CARDS
k1, k2, k3, k4 = st.columns(4)

with k1:
    st.markdown("<div class='metric-card'><h3>Model</h3><h2>XGBoost</h2></div>",
                unsafe_allow_html=True)

with k2:
    st.markdown("<div class='metric-card'><h3>Accuracy</h3><h2>96.2%</h2></div>",
                unsafe_allow_html=True)

with k3:
    st.markdown(
        f"<div class='metric-card'><h3>Features</h3><h2>{len(model_columns)}</h2></div>", unsafe_allow_html=True)

with k4:
    st.markdown("<div class='metric-card'><h3>Dataset</h3><h2>25K+</h2></div>",
                unsafe_allow_html=True)

st.divider()

# INPUT SECTION
st.subheader("Passenger Information")

left, right = st.columns(2)

with left:
    age = st.number_input("Age", min_value=7, max_value=85, value=None)
    flight_distance = st.number_input(
        "Flight Distance", min_value=30, max_value=5000, value=None)
    travel_class = st.selectbox(
        "Class", ["Select Class", "Business", "Eco", "Eco Plus"])
    type_of_travel = st.selectbox(
        "Type of Travel", ["Select Travel Type", "Business travel", "Personal Travel"])
    inflight_entertainment = st.slider("Inflight Entertainment", 1, 5, 3)
    seat_comfort = st.slider("Seat Comfort", 1, 5, 3)

with right:
    gender = st.selectbox("Gender", ["Select Gender", "Male", "Female"])
    customer_type = st.selectbox(
        "Customer Type", ["Select Customer Type", "Loyal Customer", "disloyal Customer"])
    online_boarding = st.slider("Online Boarding", 1, 5, 3)
    onboard_service = st.slider("On-board Service", 1, 5, 3)
    leg_room = st.slider("Leg Room Service", 1, 5, 3)
    departure_delay = st.number_input(
        "Departure Delay (Min)", min_value=0, max_value=1500, value=None)

required_fields = [age, flight_distance, departure_delay]

# PREDICTION
if st.button("Predict Satisfaction"):
    if (
        None in required_fields
        or travel_class == "Select Class"
        or type_of_travel == "Select Travel Type"
        or gender == "Select Gender"
        or customer_type == "Select Customer Type"
    ):
        st.warning("Please fill all required fields before prediction.")
    else:
        input_dict = {
            'Age': [age],
            'Flight Distance': [flight_distance],
            'Inflight entertainment': [inflight_entertainment],
            'Online boarding': [online_boarding],
            'Seat comfort': [seat_comfort],
            'On-board service': [onboard_service],
            'Leg room service': [leg_room],
            'Departure Delay in Minutes': [departure_delay],
            'Gender_Male': [1 if gender == "Male" else 0],
            'Customer Type_disloyal Customer': [1 if customer_type == "disloyal Customer" else 0],
            'Type of Travel_Personal Travel': [1 if type_of_travel == "Personal Travel" else 0],
            'Class_Eco': [1 if travel_class == "Eco" else 0],
            'Class_Eco Plus': [1 if travel_class == "Eco Plus" else 0]
        }

        input_df = pd.DataFrame(input_dict).reindex(
            columns=model_columns,
            fill_value=0
        )

        prediction = model.predict(input_df)
        predicted_label = label_encoder.inverse_transform(prediction)[0]
        probabilities = model.predict_proba(input_df)[0]
        confidence = round(np.max(probabilities) * 100, 2)

        st.divider()
        result_col, chart_col = st.columns([1, 1])

        # RESULT
        with result_col:
            st.markdown(
                f"""
                <div class="prediction-box">
                    <h1>{predicted_label.upper()}</h1>
                    <br>
                    <h2>Confidence: {confidence:.2f}%</h2>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown("<br>", unsafe_allow_html=True)
            st.subheader("Recommendation")

            if predicted_label == "satisfied":
                st.markdown(
                    """
                    <div class="recommendation-box">
                    Passenger satisfaction is high.  
                    Maintain premium services and customer loyalty programs.
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    """
                    <div class="recommendation-box">
                    Passenger satisfaction is low.  
                    Improve onboard experience and reduce delays.
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        # PIE CHART
        with chart_col:
            prob_df = pd.DataFrame({
                "Status": label_encoder.classes_,
                "Probability": probabilities
            })

            fig = px.pie(
                prob_df,
                names="Status",
                values="Probability",
                hole=0.55,
                color_discrete_sequence=["#FFD700", "#b8860b"]
            )

            fig.update_traces(textinfo="percent+label")
            fig.update_layout(
                title=" ",
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font_color=text_color,
                title_font_size=20
            )
            st.plotly_chart(fig, use_container_width=True)

        st.divider()

        # GAUGE CHART
        st.subheader("Confidence Analysis")

        gauge = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=confidence,
                title={'text': "Prediction Confidence"},
                gauge={
                    'axis': {'range': [0, 100]},
                    'bar': {'color': "#FFD700"},
                    'steps': [
                        {'range': [0, 50], 'color': '#333333'},
                        {'range': [50, 80], 'color': '#b8860b'},
                        {'range': [80, 100], 'color': '#FFD700'}
                    ]
                }
            )
        )

        gauge.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            font_color=text_color,
            height=350
        )
        st.plotly_chart(gauge, use_container_width=True)

# FOOTER
st.divider()
st.markdown(
    """
    <center>
    Developed using Streamlit, Plotly, and XGBoost Machine Learning  
    </center>
    """,
    unsafe_allow_html=True
)

# EXTRA INFO / CREDITS
st.markdown(
    """
    <br>
    <center>
    <small>
    © 2026 AI Airline Satisfaction Dashboard | Designed by Manar Ali 
    </small>
    </center>
    """,
    unsafe_allow_html=True
)