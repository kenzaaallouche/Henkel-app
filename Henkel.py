import streamlit as st
from openpyxl import load_workbook

import random
import pandas as pd
import streamlit as st
from scarp import TestKetest
import pandas as pd
import streamlit as st


@st.cache_data() 
def load_data():
    df =  pd.read_excel ('bdd.xlsx')
    df=df.drop(['Region', 'City','Area','District ID', 'District Name', 'Salesman Name', 'Customer No','BUID', 'Points','Price', 'Value', 'Discount','Qty'], axis=1)
    return df

# Définir le titre de l'application Streamlit

st.title(":red[HENKEL DASHBOARD]")
#st.caption('ALLOUCHE KENZA.')
st.divider()
st.sidebar.image("logo.png",caption="HENKEL DASHBOARD")
DF =load_data()

st.sidebar.header('Please filter')
SalesmanNo=st.sidebar.multiselect(
    "VENDEUR",
    options=DF["Salesman No"].unique(),
    default=DF["Salesman No"].unique(),
)
Item_Name=st.sidebar.multiselect(
    "Produit",
    options=DF["Item Name"].unique(),
    default=DF["Item Name"].unique(),
)
df_filtre = DF.loc[DF['Salesman No'].isin(SalesmanNo) & DF['Item Name'].isin(Item_Name)]



a=DF["Net"].sum


    #variable distribution Histogram

st.dataframe(df_filtre)
#test_instance = TestKetest()
if st.button('AUTOMATISATION SALES BUZZ'):
    test_instance = TestKetest()
    # Créez une instance de la classe TestKetest
    test_instance.setup_method(None)
    test_instance.test_ketest()
    
    #test_instance.teardown_method(None)
   
    # Appeler la fonction pour ouvrir le répertoire de téléchargement

# Create a dataframe with pandas (you can pass any pandas dataframe)





# Chargement du fichier Excel
file = st.file_uploader("Sélectionnez un fichier Excel", type=["xlsx"])

if file is not None:
    # Lecture du contenu du fichier Excel
    wb = load_workbook(file)
    sheet = wb.active

    # Supprimer les deux premières lignes
    sheet.delete_rows(1, 2)

    # Enregistrer le fichier Excel modifié
    wb.save("kenza.xlsx")

    st.success("Les deux premières lignes ont été supprimées et le fichier a été enregistré avec succès.")
