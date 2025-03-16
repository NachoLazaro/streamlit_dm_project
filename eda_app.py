# PROYECTO DE CONSOLIDACION STREAMLIT: FUNCION eda_app.py

# Importaciones: streamlit, pandas, matplotlib, seaborn

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np



# Función principal que emplearemos en la APP
def run_eda_app():

	# Todo el código a escribir va aquí
   
	st.subheader("Sección EDA")

	option=st.sidebar.selectbox(
		'Selecciona una opción:',
		['Descriptivo', 'Gráfico']
	)

	# Carga de ficheros
	df_diabetes=pd.read_csv("data/diabetes_data_upload.csv")
	df_diabetes_clean=pd.read_csv("data/diabetes_data_upload_clean.csv")
	df_age_data=pd.read_csv("data/freqdist_of_age_data.csv")


	# Sección Descriptivo
	if option == "Descriptivo":
		st.subheader("Análisis descriptivo")
		
		st.dataframe(data=df_diabetes)

		with st.expander("Tipos de Datos", expanded=False, icon=None):

			st.write(df_diabetes.dtypes)
		
		with st.expander("Resumen descriptivo", expanded=False, icon=None):

			st.write(df_diabetes_clean.describe())
		
		with st.expander("Distribución por género (Gender)", expanded=False, icon=None):

			st.write(df_diabetes["Gender"].value_counts())
		
		with st.expander("Distribución por clase/label (Class)", expanded=False, icon=None):

			st.write(df_diabetes["class"].value_counts())

	# Sección Gráfico
	elif option == 'Gráfico':
		st.subheader("Análisis gráfico")

		# Crear columnas
		col1, col2  = st.columns([2,1])

		with col1:
			with st.expander("Gráfico de distribución por género (Gender)", expanded=False, icon=None):
				# Create the plot
				fig, ax = plt.subplots()
				ax.bar(df_diabetes["Gender"].value_counts().index, df_diabetes["Gender"].value_counts().values, color=['blue', 'orange'])
				ax.set_xlabel('Gender')
				ax.set_ylabel('count')
				# Display the plot in Streamlit
				st.pyplot(fig)
				
			with st.expander("Gráfico de distribución por clase/label (Class)", expanded=False, icon=None):
				# Create the plot
				fig, ax = plt.subplots()
				ax.bar(df_diabetes["class"].value_counts().index, df_diabetes["class"].value_counts().values, color=['blue', 'orange'])
				ax.set_xlabel('class')
				ax.set_ylabel('count')
				# Display the plot in Streamlit
				st.pyplot(fig)
		
		with col2:
			with st.expander("Gender Distribution", expanded=False, icon=None):
				st.write(df_diabetes["Gender"].value_counts())

			with st.expander("Class Distribution", expanded=False, icon=None):
				st.write(df_diabetes["class"].value_counts())


		#####
		with st.expander("Frequency Dist Plot of Age", expanded=False, icon=None):
			# Create the plot
			fig, ax = plt.subplots()
			colors = sns.color_palette("viridis", len(df_age_data))  # Colormap de Seaborn
			sns.barplot(x='Age', y='count', data=df_age_data, palette=colors, ax=ax)
			ax.set_xlabel('Age', fontsize=12)
			ax.set_ylabel('counts', fontsize=12)
			ax.tick_params(axis='x', rotation=45)  # Rotar etiquetas del eje X		
			# Display the plot in Streamlit
			st.pyplot(fig)
		
		with st.expander("Detección de Outliers", expanded=False, icon=None):
			# Create the plot
			fig, ax = plt.subplots()
			sns.boxplot(x='Gender', y='Age', data=df_diabetes, ax=ax, palette="pastel")
			ax.set_xlabel('Género', fontsize=12)
			ax.set_ylabel('Edad', fontsize=12)
			st.pyplot(fig)
		
		with st.expander("Correlation Plot", expanded=False, icon=None):
				correlation_matrix=df_diabetes_clean.corr()
				# Crear el heatmap con Seaborn
				fig, ax = plt.subplots(figsize=correlation_matrix.shape)
				sns.heatmap(correlation_matrix, annot=True, cmap="inferno", ax=ax)
				st.pyplot(fig)


# Fin de la FUNCION







