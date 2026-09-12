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
    if organic_matter < 2.0:
        organic_result = "Your soil organic matter is low."
    elif organic_matter <= 4.0:
        organic_result = "Your soil organic matter is in a reasonable range."
    else:
        organic_result = "Your soil has high organic matter."
    st.write(f"**Organic Matter Analysis:** {organic_result}")
    if nitrogen < 20:
        nitrogen_result = "Your soil nitrogen level is low."
    elif nitrogen <= 40:
        nitrogen_result = "Your soil nitrogen level is in a moderate range."
    else:
        nitrogen_result = "Your soil nitrogen level is high."

    st.write(f"**Nitrogen Analysis:** {nitrogen_result}")
    if phosphorus < 15:
        phosphorus_result = "Your soil phosphorus level is low."
    elif phosphorus <= 30:
        phosphorus_result = "Your soil phosphorus level is in a moderate range."
    else:
        phosphorus_result = "Your soil phosphorus level is high."

    st.write(f"**Phosphorus Analysis:** {phosphorus_result}")
    if potassium < 100:
        potassium_result = "Your soil potassium level is low."
    elif potassium <= 200:
        potassium_result = "Your soil potassium level is in a moderate range."
    else:
        potassium_result = "Your soil potassium level is high."

    st.write(f"**Potassium Analysis:** {potassium_result}")
    if ec < 2.0:
        ec_result = "Your soil has low salinity."
    elif ec <= 4.0:
        ec_result = "Your soil has moderate salinity."
    else:
        ec_result = "Your soil has high salinity."

    st.write(f"**EC Analysis:** {ec_result}")
    if soil_texture == "Loamy" and crop == "Rice":
        crop_result = "Loamy soil is generally suitable for rice cultivation when water and nutrient management are appropriate."
    else:
        crop_result = f"{soil_texture} soil selected for {crop}. Crop-specific recommendations will be added."

    st.write(f"**Crop & Soil Analysis:** {crop_result}")
    if nitrogen < 20:
        nitrogen_advice = "Consider improving nitrogen availability through appropriate nitrogen management."
    elif nitrogen <= 40:
        nitrogen_advice = "Nitrogen is in a moderate range. Apply nitrogen fertilizer according to crop requirements and avoid excessive application."
    else:
        nitrogen_advice = "Nitrogen is high. Avoid unnecessary nitrogen fertilizer application."
    
    st.write(f"**Nitrogen Recommendation:** {nitrogen_advice}")
    if phosphorus < 15:
        phosphorus_advice = "Phosphorus is low. Consider appropriate phosphorus management based on crop requirements."
    elif phosphorus <= 30:
        phosphorus_advice = "Phosphorus is in a moderate range. Maintain balanced phosphorus management and avoid unnecessary application."
    else:
        phosphorus_advice = "Phosphorus is high. Avoid unnecessary phosphorus fertilizer application."

    st.write(f"**Phosphorus Recommendation:** {phosphorus_advice}")
    if potassium < 100:
        potassium_advice = "Potassium is low. Consider appropriate potassium management based on crop requirements."
    elif potassium <= 200:
        potassium_advice = "Potassium is in a moderate range. Maintain balanced potassium management and avoid unnecessary application."
    else:
        potassium_advice = "Potassium is high. Avoid unnecessary potassium fertilizer application."

    st.write(f"**Potassium Recommendation:** {potassium_advice}")
    if ec < 2.0:
        ec_advice = "Soil salinity is currently low. Maintain proper irrigation and drainage to prevent salt accumulation."
    elif ec <= 4.0:
        ec_advice = "Soil has moderate salinity. Monitor salinity and maintain good irrigation and drainage."
    else:
        ec_advice = "Soil salinity is high. Consider improving drainage and managing salt accumulation before planting."
    
    st.write(f"**EC Recommendation:** {ec_advice}")

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
