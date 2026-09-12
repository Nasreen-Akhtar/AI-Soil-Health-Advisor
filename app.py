import streamlit as st

st.set_page_config(
    page_title="AI Soil Health Advisor",
    page_icon="🌱",
    layout="centered"
)

st.title("🌱 AI Soil Health Advisor")

st.write(
    "An AI-powered decision-support system for helping farmers "
    "understand soil health and make sustainable soil-management decisions."
)

st.subheader("Enter Your Soil Information")

ph = st.number_input(
    "Soil pH (0–14)",
    min_value=0.0,
    max_value=14.0,
    value=7.0,
    step=0.1
)

organic_matter = st.number_input(
    "Organic Matter (%)",
    min_value=0.0,
    max_value=100.0,
    value=2.0,
    step=0.1
)

nitrogen = st.number_input(
    "Nitrogen (mg/kg)",
    min_value=0.0,
    value=0.0,
    step=1.0
)

phosphorus = st.number_input(
    "Phosphorus (mg/kg)",
    min_value=0.0,
    value=0.0,
    step=1.0
)

potassium = st.number_input(
    "Potassium (mg/kg)",
    min_value=0.0,
    value=0.0,
    step=1.0
)

ec = st.number_input(
    "Electrical Conductivity (EC) (dS/m)",
    min_value=0.0,
    value=0.0,
    step=0.1
)

soil_texture = st.selectbox(
    "Soil Texture",
    ["Sandy", "Loamy", "Clayey", "Silty", "Not sure"]
)

crop = st.selectbox(
    "Crop (Optional)",
    ["Not specified", "Rice", "Wheat", "Maize", "Vegetables", "Other"]
)

if st.button("Analyze Soil"):
    
        if ph < 6.0:
        ph_result = "Your soil is acidic."
    elif ph <= 7.5:
        ph_result = "Your soil pH is in a suitable range for many crops."
    else:
        ph_result = "Your soil is alkaline."

    st.subheader("🔬 Soil Analysis")
    st.write(f"**pH Analysis:** {ph_result}")

    st.subheader("🌱 Soil Information")

    st.write(f"**pH:** {ph}")
    st.write(f"**Organic Matter:** {organic_matter}%")
    st.write(f"**Nitrogen:** {nitrogen}")
    st.write(f"**Phosphorus:** {phosphorus}")
    st.write(f"**Potassium:** {potassium}")
    st.write(f"**EC:** {ec}")
    st.write(f"**Soil Texture:** {soil_texture}")
    st.write(f"**Crop:** {crop}")

    st.success(
        "Your soil information has been recorded. "
        "AI-based soil analysis will be added in the next stage."
    )
