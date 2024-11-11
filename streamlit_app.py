import streamlit as st
import pandas as pd

if "data" not in st.session_state:
    st.session_state.data = [
        {"Row Labels": "[B3] 48.3X4 CHS", "Max of Elem Station": 2.425, "Max of P": 15.6916, "Min of P": -1.283, "Max of V2": 2.0973, "Min of V2": -5.5459, "Max of V3": 0.9721, "Min of V3": -0.7313, "Max of T": 0.056, "Min of T": -0.0423, "Max of M2": 0.5243, "Min of M2": -0.1731, "Max of M3": 0.9528, "Min of M3": -0.3229},
    ]

st.title('Calculation Generator from Excel Input')

st.write("# Data Table")
data_df = pd.DataFrame(st.session_state.data)

# Editable Data Table using Streamlit's built-in features
edited_df = st.data_editor(data_df, num_rows="dynamic")

# Submit button to update session state
def update_data():
    st.session_state.data = edited_df.to_dict(orient='records')

if st.button("Submit Changes"):
    update_data()

st.write("# Updated Data Table")
st.dataframe(st.session_state.data)
