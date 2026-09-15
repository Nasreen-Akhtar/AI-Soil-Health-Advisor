import streamlit as st
import joblib
model = joblib.load("soil_health_model.pkl")

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
organic_carbon = organic_matter

ml_input = [[
    nitrogen,
    phosphorus,
    potassium,
    ph,
    ec,
    organic_carbon
]]

ml_prediction = model.predict(ml_input)[0]
st.subheader("🤖 ML-Based Fertility Insight")

fertility_labels = {
    0: "Less Fertile",
    1: "Fertile",
    2: "Highly Fertile"
}

st.info(
    f"Dataset-based ML model indicates: "
    f"**{fertility_labels[ml_prediction]}**"
)

st.caption(
    "This ML insight is based on patterns learned from the training dataset. "
    "The overall soil health assessment and recommendations are generated "
    "separately using rule-based soil criteria."
)
if st.button("Analyze Soil"):
    score = 0

    # Soil pH — 20 points
    if 6.0 <= ph <= 7.5:
        score += 20
    elif 5.5 <= ph < 6.0 or 7.5 < ph <= 8.0:
        score += 12
    else:
        score += 5

    # Organic Matter — 20 points
    if 2.0 <= organic_matter <= 4.0:
        score += 20
    elif 1.5 <= organic_matter < 2.0:
        score += 12
    else:
        score += 5

    # Nitrogen — 15 points
    if 20 <= nitrogen <= 40:
        score += 15
    elif 15 <= nitrogen < 20 or 40 < nitrogen <= 50:
        score += 9
    else:
        score += 4

    # Phosphorus — 15 points
    if 15 <= phosphorus <= 30:
        score += 15
    elif 10 <= phosphorus < 15 or 30 < phosphorus <= 40:
        score += 9
    else:
        score += 4

    # Potassium — 15 points
    if 100 <= potassium <= 200:
        score += 15
    elif 75 <= potassium < 100 or 200 < potassium <= 250:
        score += 9
    else:
        score += 4

    # EC / Salinity — 15 points
    if ec < 2.0:
        score += 15
    elif ec <= 4.0:
        score += 9
    else:
        score += 4
    
    if ph < 6.0:
        ph_result = "Your soil is acidic."
    elif ph <= 7.5:
        ph_result = "Your soil pH is in a suitable range for many crops."
    else:
        ph_result = "Your soil is alkaline."

    st.subheader("🔬 Soil Analysis")
    st.subheader("🌱 Overall Soil Health Score")
    final_score = round((score / 100) * 100)
    st.metric("Soil Health Score", f"{final_score}/100")
    st.progress(final_score / 100)
    st.caption("Score is based on the entered soil properties and the current rule-based assessment.")
    if final_score >= 80:
        st.success("🌱 Excellent soil health")
    elif final_score >= 60:
        st.info("🌿 Good soil health")
    elif final_score >= 40:
        st.warning("⚠️ Soil health needs improvement")
    else:
        st.error("🔴 Soil health needs attention")
    
    st.subheader("💡 Overall Assessment")
    
    if final_score >= 80:
        summary = (
            "Based on the entered values, the soil shows generally favorable "
            "conditions. Continue balanced nutrient management, maintain organic "
            "matter, and avoid excessive fertilizer application."
        )
    elif final_score >= 60:
        summary = (
            "Based on the entered values, the soil shows generally acceptable "
            "conditions, but some areas may need attention. Focus on balanced "
            "nutrient management and regular soil monitoring."
        )
    else:
        summary = (
            "Based on the entered values, some soil properties may need attention. "
            "Consider targeted soil management and follow-up soil testing."
        )

    st.write(summary)

        
    st.write(f"**pH Analysis:** {ph_result}")
    if ph < 6.0:
       st.warning("⚠️ Soil pH is acidic.")
    elif ph <= 7.5:
       st.success("🟢 Soil pH is in a suitable range.")
    else:
       st.warning("⚠️ Soil pH is alkaline.")
    if organic_matter < 2.0:
        organic_result = "Your soil organic matter is low."
    elif organic_matter <= 4.0:
        organic_result = "Your soil organic matter is in a reasonable range."
    else:
        organic_result = "Your soil has high organic matter."
    st.write(f"**Organic Matter Analysis:** {organic_result}")
    if organic_matter < 2.0:
       st.warning("⚠️ Organic matter needs attention.")
    elif organic_matter <= 4.0:
       st.success("🟢 Organic matter is in a reasonable range.")
    else:
       st.info("🔵 Organic matter is high.")
    if nitrogen < 20:
        nitrogen_result = "Your soil nitrogen level is low."
    elif nitrogen <= 40:
        nitrogen_result = "Your soil nitrogen level is in a moderate range."
    else:
        nitrogen_result = "Your soil nitrogen level is high."

    st.write(f"**Nitrogen Analysis:** {nitrogen_result}")
    if nitrogen < 20:
       st.warning("⚠️ Nitrogen needs attention.")
    elif nitrogen <= 40:
       st.success("🟢 Nitrogen level is moderate.")
    else:
       st.info("🔵 Nitrogen level is high.")
    
    if phosphorus < 15:
        phosphorus_result = "Your soil phosphorus level is low."
    elif phosphorus <= 30:
        phosphorus_result = "Your soil phosphorus level is in a moderate range."
    else:
        phosphorus_result = "Your soil phosphorus level is high."

    st.write(f"**Phosphorus Analysis:** {phosphorus_result}")
    if phosphorus < 15:
        st.warning("⚠️ Phosphorus needs attention.")
    elif phosphorus <= 30:
        st.success("🟢 Phosphorus level is moderate.")
    else:
        st.info("🔵 Phosphorus level is high.")

    if potassium < 100:
        potassium_advice = "Potassium is low. Consider appropriate potassium management based on crop requirements."
    elif potassium <= 200:
        potassium_advice = "Potassium is in a moderate range. Maintain balanced potassium management and avoid unnecessary application."
    else:
        potassium_advice = "Potassium is high. Avoid unnecessary potassium fertilizer application."

    st.write(f"**Potassium Analysis:** {potassium_advice}")
    if potassium < 100:
        st.warning("⚠️ Potassium may need attention.")
    elif potassium <= 200:
        st.success("🟢 Potassium management is currently balanced.")
    else:
        st.info("🔵 Potassium is high. Avoid unnecessary fertilizer application.")

    if ec < 2.0:
        ec_result = "Your soil has low salinity."
    elif ec <= 4.0:
        ec_result = "Your soil has moderate salinity."
    else:
        ec_result = "Your soil has high salinity."
    st.write(f"**EC Analysis:** {ec_result}")

    if ec < 2.0:
        st.success("🟢 Soil salinity is low.")
    elif ec <= 4.0:
        st.warning("🟡 Soil salinity needs monitoring.")
    else:
        st.error("🔴 Soil salinity is high.")

    if crop == "Rice":
        if soil_texture == "Loamy":
            crop_result = "Loamy soil is generally suitable for rice cultivation when water and nutrient management are appropriate."
        elif soil_texture == "Clayey":
            crop_result = "Clayey soil can support rice cultivation because it retains water well, but proper drainage and nutrient management are important."
        elif soil_texture == "Sandy":
            crop_result = "Sandy soil may have limited water-holding capacity for rice. Good irrigation, organic matter, and careful nutrient management are important."
        else:
            crop_result = f"{soil_texture} soil selected for rice. Monitor water retention, drainage, and nutrient availability."

    elif crop == "Wheat":
        if soil_texture == "Loamy":
            crop_result = "Loamy soil is generally suitable for wheat because it provides a good balance of drainage, water retention, and nutrient availability."
        elif soil_texture == "Sandy":
            crop_result = "Sandy soil may require better water and nutrient management for wheat because of lower water-holding capacity."
        elif soil_texture == "Clayey":
            crop_result = "Clayey soil can support wheat, but good drainage and soil structure management are important."
        else:
            crop_result = f"{soil_texture} soil selected for wheat. Monitor soil moisture, drainage, and nutrient availability."

    elif crop == "Maize":
        if soil_texture == "Loamy":
            crop_result = "Loamy soil is generally favorable for maize because it provides good drainage, moisture retention, and nutrient availability."
        elif soil_texture == "Sandy":
            crop_result = "Sandy soil can support maize but may require frequent irrigation and careful nutrient management because of lower water and nutrient retention."
        elif soil_texture == "Clayey":
            crop_result = "Clayey soil can support maize, but good drainage and soil structure are important to prevent waterlogging and poor root development."
        else:
            crop_result = f"{soil_texture} soil selected for maize. Monitor soil moisture, drainage, and nutrient availability."

    elif crop == "Vegetables":
        if soil_texture == "Loamy":
            crop_result = "Loamy soil is generally favorable for vegetables because it provides good drainage, moisture retention, and root development."
        elif soil_texture == "Sandy":
            crop_result = "Sandy soil may require frequent irrigation and organic matter additions to improve moisture and nutrient retention for vegetables."
        elif soil_texture == "Clayey":
            crop_result = "Clayey soil may require improved drainage and organic matter management to support healthy vegetable root development."
        else:
            crop_result = f"{soil_texture} soil selected for vegetables. Monitor drainage, moisture, organic matter, and nutrient availability."

    else:
        crop_result = f"{soil_texture} soil selected for {crop}. Consider soil moisture, drainage, organic matter, and nutrient management."
    st.write(f"**Crop & Soil Analysis:** {crop_result}")
        # Soil texture analysis
    if soil_texture == "Sandy":
        texture_advice = (
            "Sandy soil has lower water and nutrient-holding capacity. "
            "Consider adding organic matter, using efficient irrigation, "
            "and applying nutrients in smaller split doses."
        )
    elif soil_texture == "Clayey":
        texture_advice = (
            "Clayey soil can have drainage and compaction problems. "
            "Maintain good drainage, avoid working the soil when it is too wet, "
            "and add organic matter to improve soil structure."
        )
    elif soil_texture == "Silty":
        texture_advice = (
            "Silty soil can be prone to erosion and compaction. "
            "Maintain soil cover, add organic matter, and use careful irrigation "
            "to protect soil structure."
        )
    elif soil_texture == "Loamy":
        texture_advice = (
            "Loamy soil generally provides a good balance of water retention, "
            "drainage, and nutrient availability. Maintain organic matter and "
            "balanced nutrient management."
        )
    else:
        texture_advice = (
            "Soil texture was not specified. Consider a soil texture test "
            "for more accurate water and nutrient management recommendations."
        )

    st.write(f"**Soil Texture Recommendation:** {texture_advice}")
    st.subheader("🌾 Recommended Action Plan")

    actions = []

    if ph < 6.0:
        actions.append("🧪 Address acidic soil conditions based on a soil test and crop requirements.")

    if ec > 4.0:
        actions.append("💧 Improve drainage and irrigation management to reduce salt accumulation.")

    if organic_matter < 2.0:
        actions.append("🌱 Increase organic matter using well-decomposed compost or suitable organic materials.")

    if nitrogen < 20:
        actions.append("🌿 Improve nitrogen availability through balanced, crop-appropriate nitrogen management.")

    if phosphorus < 15 or potassium < 100:
        actions.append("🌾 Address low phosphorus and/or potassium through crop-appropriate nutrient management.")

    if soil_texture == "Sandy":
        actions.append("💦 Improve water and nutrient retention in sandy soil through organic matter and efficient irrigation.")

    if actions:
        for i, action in enumerate(actions[:5], start=1):
            st.write(f"**{i}.** {action}")
    else:
        st.success("🌱 Soil conditions are generally favorable. Continue balanced soil management and regular soil testing.")

    st.subheader("📋 Entered Soil Information")

    st.write(f"**pH:** {ph}")
    st.write(f"**Organic Matter:** {organic_matter}%")
    st.write(f"**Nitrogen:** {nitrogen} mg/kg")
    st.write(f"**Phosphorus:** {phosphorus} mg/kg")
    st.write(f"**Potassium:** {potassium} mg/kg")
    st.write(f"**EC:** {ec} dS/m")
    st.write(f"**Soil Texture:** {soil_texture}")
    st.write(f"**Crop:** {crop}")

    st.success(
        "Soil analysis completed successfully. "
        "Review the analysis and recommendations above."
    )
    st.info(
        "ℹ️ Note: This tool provides preliminary, rule-based soil health guidance. "
        "For field-level decisions, recommendations should be validated through "
        "laboratory soil testing and local agronomic expertise."
    )
