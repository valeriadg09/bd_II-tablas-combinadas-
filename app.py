import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

st.title("Bases de Datos Ventas Tigo Colombia")

st.subheader("Carga los archivos de Excel aquí")

uploaded_file1 = st.file_uploader("Carga la primera base de datos", type="xlsx")
uploaded_file2 = st.file_uploader("Carga la segunda base de datos", type="xlsx")

if uploaded_file1 and uploaded_file2:
    
    df1 = pd.read_excel(uploaded_file1, engine='openpyxl')
    df2 = pd.read_excel(uploaded_file2, engine='openpyxl')

    df_combined = pd.concat([df1, df2])

    st.write("Datos combinados:")
    st.dataframe(df_combined)

    engine = create_engine('mysql+pymysql://root:Commandos2002++@localhost/base_prueba')
    
    if st.button("Guardar en la base de datos"):
        df_combined.to_sql('ventas_combinadas', con=engine, if_exists='replace', index=False)
        st.success("Datos guardados en la base de datos con éxito.")
else:
    st.info("Por favor, carga ambos archivos de Excel para continuar.")
