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
    score = 0
    if 6.0 <= ph <= 7.5:
        score += 15
    if 2.0 <= organic_matter <= 4.0:
        score += 15
    
    if ph < 6.0:
        ph_result = "Your soil is acidic."
    elif ph <= 7.5:
        ph_result = "Your soil pH is in a suitable range for many crops."
    else:
        ph_result = "Your soil is alkaline."

    st.subheader("🔬 Soil Analysis")
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
        potassium_result = "Your soil potassium level is low."
    elif potassium <= 200:
        potassium_result = "Your soil potassium level is in a moderate range."
    else:
        potassium_result = "Your soil potassium level is high."

    st.write(f"**Potassium Analysis:** {potassium_result}")
    if potassium < 100:
       st.warning("⚠️ Potassium needs attention.")
    elif potassium <= 200:
       st.success("🟢 Potassium level is moderate.")
    else:
       st.info("🔵 Potassium level is high.")
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
    if soil_texture == "Loamy" and crop == "Rice":
        crop_result = "Loamy soil is generally suitable for rice cultivation when water and nutrient management are appropriate."
    else:
        crop_result = f"{soil_texture} soil selected for {crop}. Crop-specific recommendations will be added."

    st.write(f"**Crop & Soil Analysis:** {crop_result}")

    st.subheader("🌱 Soil Health Recommendations")

    if nitrogen < 20:
        nitrogen_advice = "Consider improving nitrogen availability through appropriate nitrogen management."
    elif nitrogen <= 40:
        nitrogen_advice = "Nitrogen is in a moderate range. Apply nitrogen fertilizer according to crop requirements and avoid excessive application."
    else:
        nitrogen_advice = "Nitrogen is high. Avoid unnecessary nitrogen fertilizer application."

    st.write(f"**Nitrogen Recommendation:** {nitrogen_advice}")
    if nitrogen < 20:
       st.warning("⚠️ Nitrogen may need attention.")
    elif nitrogen <= 40:
       st.success("🟢 Nitrogen management is currently balanced.")
    else:
       st.info("🔵 Nitrogen is high. Avoid unnecessary fertilizer application.")
    if phosphorus < 15:
        phosphorus_advice = "Phosphorus is low. Consider appropriate phosphorus management based on crop requirements."
    elif phosphorus <= 30:
        phosphorus_advice = "Phosphorus is in a moderate range. Maintain balanced phosphorus management and avoid unnecessary application."
    else:
        phosphorus_advice = "Phosphorus is high. Avoid unnecessary phosphorus fertilizer application."

    st.write(f"**Phosphorus Recommendation:** {phosphorus_advice}")
    if phosphorus < 15:
       st.warning("⚠️ Phosphorus may need attention.")
    elif phosphorus <= 30:
       st.success("🟢 Phosphorus management is currently balanced.")
    else:
       st.info("🔵 Phosphorus is high. Avoid unnecessary fertilizer application.")
    if potassium < 100:
        potassium_advice = "Potassium is low. Consider appropriate potassium management based on crop requirements."
    elif potassium <= 200:
        potassium_advice = "Potassium is in a moderate range. Maintain balanced potassium management and avoid unnecessary application."
    else:
        potassium_advice = "Potassium is high. Avoid unnecessary potassium fertilizer application."

    st.write(f"**Potassium Recommendation:** {potassium_advice}")
    if potassium < 100:
       st.warning("⚠️ Potassium may need attention.")
    elif potassium <= 200:
       st.success("🟢 Potassium management is currently balanced.")
    else:
       st.info("🔵 Potassium is high. Avoid unnecessary fertilizer application.")
    if ec < 2.0:
        ec_advice = "Soil salinity is currently low. Maintain proper irrigation and drainage to prevent salt accumulation."
    elif ec <= 4.0:
        ec_advice = "Soil has moderate salinity. Monitor salinity and maintain good irrigation and drainage."
    else:
        ec_advice = "Soil salinity is high. Consider improving drainage and managing salt accumulation before planting."
    
    st.write(f"**EC Recommendation:** {ec_advice}")
    if ec < 2.0:
       st.success("🟢 Salinity management is currently good.")
    elif ec <= 4.0:
       st.warning("🟡 Salinity needs monitoring.")
    else:
       st.error("🔴 Salinity needs immediate attention.")
    if organic_matter < 2.0:
        organic_advice = "Organic matter is low. Consider adding well-decomposed organic material such as compost to improve soil health."
    elif organic_matter <= 4.0:
        organic_advice = "Organic matter is in a reasonable range. Maintain it by returning crop residues and using appropriate organic amendments."
    else:
        organic_advice = "Organic matter is high. Continue practices that maintain soil organic matter."

    st.write(f"**Organic Matter Recommendation:** {organic_advice}")
    if organic_matter < 2.0:
       st.warning("⚠️ Organic matter may need improvement.")
    elif organic_matter <= 4.0:
       st.success("🟢 Organic matter management is currently good.")
    else:
       st.info("🔵 Organic matter is high.")
    if ph < 6.0:
        ph_advice = "Soil is acidic. Consider appropriate soil amendments based on a soil test and crop requirements."
    elif ph <= 7.5:
        ph_advice = "Soil pH is in a suitable range. Maintain balanced nutrient and soil management practices."
    else:
        ph_advice = "Soil is alkaline. Consider appropriate management practices based on a soil test and crop requirements."

    st.write(f"**pH Recommendation:** {ph_advice}")
    if ph < 6.0:
       st.warning("⚠️ Soil pH may need correction.")
    elif ph <= 7.5:
       st.success("🟢 Soil pH management is currently suitable.")
    else:
       st.warning("⚠️ Soil pH may need correction.")
    if crop == "Rice":
        crop_advice = (
            "For rice, maintain balanced nutrient management, "
            "avoid excessive nitrogen application, and maintain proper water and drainage management."
        )

    elif crop == "Wheat":
        crop_advice = (
            "For wheat, maintain balanced nitrogen and phosphorus management, "
            "avoid excessive fertilizer application, and maintain good soil moisture."
        )

    elif crop == "Maize":
        crop_advice = (
            "For maize, maintain balanced nitrogen and potassium management, "
            "support good soil moisture, and avoid excessive fertilizer application."
        )

    elif crop == "Vegetables":
        crop_advice = (
            "For vegetables, maintain balanced nutrient management, "
            "add organic matter when needed, and maintain proper irrigation and drainage."
        )

    else:
        crop_advice = (
            f"General soil management recommendations are provided for {crop}."
        )

    st.write(f"**Crop-Specific Recommendation:** {crop_advice}")
    

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
        "Soil analysis completed successfully. "
        "Review the analysis and recommendations above."
    )

    
