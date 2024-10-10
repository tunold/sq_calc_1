import streamlit as st
import math

# Title of the app

# Set the page configuration

st.set_page_config(page_title="SQ Calculator", page_icon=":bar_chart:", layout="wide")
# Add custom CSS to set a global font size for the entire app
st.markdown(
    """
    <style>
    /* Set a global font size for the entire app */
    html, body, [class*="st"], input, label, button {
        font-size: 30px;  /* Adjust the global font size here */
    }

    /* Make the number input box narrower */
    input[type=number] {
        width: 150px;  /* Adjust this value to change the width */
    }

    /* Style for the SQ Radiative limit output to make it larger */
    .large-font {
        font-size: 30px !important;  /* Adjust the size of the output text */
        /*font-weight: bold;*/
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.write('This is a SQ Calculator')
st.write('')
st.write('')
st.write('')
# Input box for Bandgap value
st.write('Please enter a Bandgap Value in eV')
bandgap = st.number_input('')


# Function to calculate SQ Voc
def Voc_SQ(bandgap):
    return -.1788 + 0.93 * bandgap


# Display the result with larger font for the SQ Radiative limit
st.markdown(f"<p class='large-font'>The SQ Radiative limit is:   {round(Voc_SQ(bandgap), 2)}  eV</p>", unsafe_allow_html=True)
