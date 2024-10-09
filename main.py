import streamlit as st

# Short app description
st.title("EVendo Score Calculator for Esophageal Varices")
st.write("""
This app calculates the EVendo Score, a tool used for assessing the risk of esophageal varices in patients. 
By entering a few clinical parameters, you can quickly determine the patient's score, aiding in decision-making for clinical management.
""")

# Input fields
age = st.number_input("Age", min_value=0, step=1)
albumin = st.number_input("Albumin (g/dL)", min_value=0.0, step=0.1)
platelet_count = st.number_input("Platelet Count (x10^9/L)", min_value=0.0, step=1.0)
international_normalized_ratio = st.number_input("INR", min_value=0.0, step=0.01)

# Calculate EVendo Score
def calculate_evendo(age, albumin, platelet_count, inr):
    # Example formula for EVendo Score, replace with the actual formula if available
    score = (age * 0.1) + (albumin * -0.5) + (platelet_count * -0.1) + (inr * 0.7)
    return score

if st.button("Calculate EVendo Score"):
    evendo_score = calculate_evendo(age, albumin, platelet_count, international_normalized_ratio)
    st.write(f"The calculated EVendo Score is: {evendo_score:.2f}")
