# AI-Soil-Health-Advisor
An AI-powered decision-support system that helps farmers understand soil health and receive sustainable soil-management recommendations.

## Overview

AI Soil Health Advisor is a web-based soil analysis tool designed to help users interpret common soil test parameters and make more informed soil-management decisions.

The application combines a machine-learning fertility insight with a transparent rule-based soil health assessment. Users can enter soil parameters such as pH, organic matter, nitrogen, phosphorus, potassium, electrical conductivity, soil texture, and crop type.

The tool provides:

* ML-based soil fertility insight
* Overall soil health score
* Individual soil parameter analysis
* Crop and soil-texture guidance
* Practical soil-management recommendations

This project was developed as a prototype for the AI Builders Hackathon.
## Tech Stack

- Python
- Streamlit
- Pandas
- Scikit-learn
- imbalanced-learn
- Joblib
- Random Forest
- GitHub

## Features

- Interactive soil data input
- ML-based soil fertility insight
- Overall soil health score
- pH, organic matter, N, P, K, and EC analysis
- Soil texture and crop-specific guidance
- Practical soil-management recommendations
- Clear and beginner-friendly interface
- Streamlit-based web application

## Machine Learning

The application uses a labeled soil-fertility dataset containing **880 soil samples**.

The model uses the following features:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Soil pH
- Electrical conductivity (EC)
- Organic carbon (OC)

Several machine-learning approaches were evaluated using stratified cross-validation. A **Balanced Random Forest** was selected as the final model because it provided a better balance between overall performance and detection of the underrepresented highly fertile class.

The final model achieved approximately **89% cross-validation accuracy** with a **0.78 macro F1-score**.

## Project Structure

```text
AI-Soil-Health-Advisor/
│
├── app.py
├── dataset1 (1).csv
├── soil_health_model.pkl
├── requirements.txt
└── README.md
```
## Installation & Setup
### 1. Clone the repository
git clone https://github.com/nasreen-akhtar/AI-Soil-Health-Advisor.git
cd AI-Soil-Health-Advisor
```
### 2. Install the required dependencies
pip install -r requirements.txt
```
### 3. Run the application
streamlit run app.py
```
The application will open in your browser at the local Streamlit address provided by the terminal.
## Usage

1. Open the AI Soil Health Advisor application.
2. Enter the available soil test values.
3. Select the soil texture and target crop.
4. Review the ML-based fertility insight.
5. Review the overall soil health score and individual parameter analysis.
6. Follow the recommended soil-management actions.
## Live Demo

Try the deployed application here:

https://ai-soil-health-advisor-gziix8ame2s4deudwvrwga.streamlit.app/
## Repository

Source code and project files are available on GitHub:

https://github.com/nasreen-akhtar/AI-Soil-Health-Advisor
## Disclaimer

AI Soil Health Advisor is a prototype decision-support tool. Its results are intended to provide preliminary insights and should not replace laboratory soil testing or professional agronomic advice.


