#  PROYECTO CONSOLIDACION STREAMLIT: FUNCION app.py

# Importaciones
import streamlit as st
import streamlit.components.v1 as stc
from eda_app import run_eda_app
from ml_app import run_ml_app

st.set_page_config(layout="wide")


# Función main()
def main():

	option=st.sidebar.selectbox(
		'Selecciona una opción:',
		['Home','EDA', 'ML', 'Info']
	)

	match option:

		case 'Home': home()
		case 'EDA':  run_eda_app()
		case 'ML': run_ml_app()
		case 'Info': info()

# Función home()
def home():

	st.markdown(
    """
    <div style="background-color: #1E90FF; padding: 10px; border-radius: 10px; width: 100%;">
        <h3 style="color: white; text-align: center;">App para la detección temprana de DM</h3>
        <h5 style="color: white; text-align: center;">(Diabetes Mellitus)</h5>
    </div>
    """,
    unsafe_allow_html=True)

	st.header("Home")
	st.subheader("App para la detección temprana de DM")
	st.write("Dataset que contiene señales y sintomas que pueden indicar diabetes o posibilidad de diabetes")
	st.subheader("Fuente de datos")
	st.code(" - https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dat")
	st.subheader("Contenidos de la App")
	st.code("""
        -  EDA Section : Análisis exploratorio de los datos.
        -  ML Section : Predicción de Diabetes basada en ML (Machine Learning).
    """)


def info():
	
	st.subheader("Info")
	st.write("MBIT, Proyecto de consolidación, librearía Streamlit")
	stc.iframe("https://www.mbitschool.com/en", width=800, height=600, scrolling=True)

if __name__ == '__main__':
	main()