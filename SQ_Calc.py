import streamlit as st
import math
import pandas as pd
import matplotlib.pyplot as plt

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

fname = 'AM15_G_wav_Mod.csv'
df_AM15 = pd.read_csv(fname, sep = ',')
#st.dataframe(df_AM15)
en_AM15 = df_AM15['Energy']
Jsc_int = df_AM15['Jsc_int']

st.write('This is a SQ Calculator')
st.write('')
st.write('')
st.write('')

# Create a plot using matplotlib
plt.figure(figsize=(6, 4))  # Optional: set the figure size
plt.plot(df_AM15['wavelength'], df_AM15['AM15_G_wav'], label='AM15 Spectrum')
plt.xlabel('Wavelength (nm)')
plt.ylabel('AM15 G (W/m²/nm)')
plt.title('AM15 Spectrum Plot')
plt.legend()

# Display the plot in Streamlit
st.pyplot(plt)

# Input box for Bandgap value
st.write('Please enter a Bandgap Value in eV')
bandgap = st.number_input('')

# Function to calculate SQ Voc
def Voc_SQ(bandgap):
    return -.1788 + 0.93 * bandgap

qfls = Voc_SQ(bandgap)

def Jsc_SQ(egap, jsc_int,  en_AM15):
    i=0
    for en in en_AM15:
        if en < egap:
            break
        i +=1
    return jsc_int[i]*1000

jsc = Jsc_SQ(bandgap,Jsc_int, en_AM15)

def FF_SQ(Voc,n=1):
    kT = 0.026
    return (Voc/(n*kT) - math.log(Voc/(n*kT) + 0.72)) /(1 + Voc/(n*kT))*100

ff= FF_SQ(qfls)

pce = ff*qfls*jsc/100

# Display the result with larger font for the SQ Radiative limit
st.markdown(f"<p class='large-font'>The SQ Radiative Voc is:   {round(qfls, 2)}  eV</p>", unsafe_allow_html=True)
st.markdown(f"<p class='large-font'>The SQ Current is:   {round(jsc, 2)}  mA/cm2</p>", unsafe_allow_html=True)
st.markdown(f"<p class='large-font'>The SQ FF is:   {round(ff, 2)}  mA/cm2</p>", unsafe_allow_html=True)
st.markdown(f"<p class='large-font'>The SQ PCE is:   {round(pce, 2)}  %</p>", unsafe_allow_html=True)
#st.dataframe(df_AM15)


