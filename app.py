#import
import streamlit as st
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import datetime as dt
import plotly.express as px
import json
import seaborn as sns
import time
import os
import sys
from PIL import Image
#footer
import streamlit as st
from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent
from htbuilder.funcs import rgba, rgb

#Page configuration
st.set_page_config(layout="wide",page_title='Real Investate', page_icon=Image.open('ri.jpg'))


#Important variable
path = "Desktop/data/"
file = "full_"
file_end = ".csv"
col_list = ['date_mutation',
        'nature_mutation',
        'valeur_fonciere',
        'code_postal',
        'type_local',
        'longitude', 
        'latitude',
        "code_departement",
        'nature_culture'
        ]

st.sidebar.header("Navigation")
#Fonction
@st.cache
def choix_genre(genre):
        if genre == 'Terrains':
                mask_constructible = df['Terrains'] == 'terrains a bâtir'
                type2 = st.sidebar.radio('Choix du type',
                        ('Constructible','Non-Constructible'))
                if type2 == 'Constructible':     
                        x = 'Terrains constructibles'
                        type3 = df[mask_constructible] 
                if type2 == 'Non-Constructible':
                        x = 'Terrains non-contructibles'
                        type3 = df[df['Terrains'] == 'sols']

        if genre == 'Biens immobiliers':
                type2 = st.sidebar.radio('Choix du type',
                        ('maison','appartement','commerce'))
                if type2 == 'maison':  
                        x = 'maisons'
                        type3 = df[df['Biens immobiliers']=='Maison'] 
                if type2 == 'appartement':
                        x = 'appartements'
                        type3 = df[df['Biens immobiliers']=='Appartement']
                if type2 == 'commerce': 
                        x = 'commerces'      
                        type3 = df[df['Biens immobiliers']=='Local industriel. commercial ou assimilé']
        return type3, x

@st.cache
def cleaning(years):
        dataframe = file + str(years) + file_end
        df = pd.read_csv(dataframe, 
                usecols=col_list,
                delimiter=',',
                header=0,  
                parse_dates=['date_mutation'],
                dtype={("nature_mutation ","nom_commune","nature_culture"):"category",
                ("valeur_fonciere","code_postal","surface_relle_bati",
                "surface_terrain"):"float32",
                ("longitude","latitude") : "int32",("code_departement"):"string" })
        df['date_mutation'] = pd.to_datetime(df['date_mutation'])
        #Delete all na and duplicate
        df = df.drop_duplicates(subset='valeur_fonciere')  
        df = df.dropna(subset=['code_postal','longitude','latitude'])  
        #Ajout d'un 0 afin d'avoir 5 chiffres pour tout les départements
        df["code_postal"] = df["code_postal"].astype(str)
        df['code_postal'] = df['code_postal'].str.zfill(7) 
        #Jointure pour avoir les noms des départements et des régions
        correspondance_region = pd.read_csv('correspondance-code-cedex-code-insee.csv',delimiter=';')                
        df.code_postal = ((df.code_postal.astype(float)).astype(int)).astype(str)
        correspondance_region['Code Postal / CEDEX'] = ((correspondance_region['Code Postal / CEDEX'].astype(float)).astype(int)).astype(str)
        df = df.merge(correspondance_region,left_on='code_postal', right_on='Code Postal / CEDEX',how='inner')
        df = df.dropna(subset=['Nom du département','Nom de la région']) 
        #Rename of columns
        df.rename(columns={"type_local": "Biens immobiliers", "nature_culture": "Terrains"}, inplace=True)
        return df

@st.cache
def simple_cleaning(years):
        dataframe = file + str(years) + file_end
        df = pd.read_csv(dataframe, 
                usecols=['valeur_fonciere',
                'code_postal'],
                delimiter=',',
                header=0,  
                dtype={("valeur_fonciere","code_postal"):"float32"})
        #Delete all na and duplicate
        df = df.drop_duplicates(subset='valeur_fonciere')  
        df = df.dropna(subset=['code_postal'])  
        #Ajout d'un 0 afin d'avoir 5 chiffres pour tout les départements
        df["code_postal"] = df["code_postal"].astype(str)
        df['code_postal'] = df['code_postal'].str.zfill(7) 
        #Jointure pour avoir les noms des départements et des régions
        correspondance_region = pd.read_csv('correspondance-code-cedex-code-insee.csv',delimiter=';')                
        df.code_postal = ((df.code_postal.astype(float)).astype(int)).astype(str)
        correspondance_region['Code Postal / CEDEX'] = ((correspondance_region['Code Postal / CEDEX'].astype(float)).astype(int)).astype(str)
        df = df.merge(correspondance_region,left_on='code_postal', right_on='Code Postal / CEDEX',how='inner')
        df = df.dropna(subset=['Nom du département','Nom de la région'])
        df1 = df[['valeur_fonciere','Nom de la région']]
        df1.rename(columns={'valeur_fonciere':'valeur_fonciere'+str(years)}, inplace = True)
        return df1


def get_date(years):
        dataframe = "full_" + str(years) + file_end
        df = pd.read_csv(dataframe, 
                usecols=["date_mutation","code_postal"],
                delimiter=',',
                header=0,
                dtype={
                ("code_postal"):"float32"}
        )
        #Delete all na and duplicate 
        df['date_mutation'] = pd.to_datetime(df['date_mutation'])
        #Ajout d'un 0 afin d'avoir 5 chiffres pour tout les départements
        df = df.dropna(subset=['code_postal'])
        df["code_postal"] = df["code_postal"].astype(str)
        df['code_postal'] = df['code_postal'].str.zfill(7) 
        #Jointure pour avoir les noms des départements et des régions
        correspondance_region = pd.read_csv('correspondance-code-cedex-code-insee.csv',delimiter=';')                
        df.code_postal = ((df.code_postal.astype(float)).astype(int)).astype(str)
        correspondance_region['Code Postal / CEDEX'] = ((correspondance_region['Code Postal / CEDEX'].astype(float)).astype(int)).astype(str)
        df = df.merge(correspondance_region,left_on='code_postal', right_on='Code Postal / CEDEX',how='inner')
        df = df.dropna(subset=['Nom du département','Nom de la région'])
        df1 = df[['date_mutation','Nom de la région']]
        df1.rename(columns={'valeur_fonciere':'valeur_fonciere'+str(years)}, inplace = True)
        return df1

page = st.sidebar.radio('',
                ('Accueil','Viz annuel'))


if page == 'Accueil':
        col1, col2 = st.columns(2)
        col2.image(Image.open('paris1.jpg'), caption='Eiffel Tower on the Seine')
        col1.header("Welcome to Real Investate")
        col1.subheader("In this special issue #5, we'll talk about Open Data 📊 !")
        col1.subheader("After Italy 🍕, France 🥐 is the second european country to release websites to provide Open Data.")
        col1.subheader("And as you can imagine, it's really interesting :eyes:" )
        col1.subheader("Lest's begin" )
        st.markdown("---")


df_2016 = simple_cleaning(2016)
df_2017 = simple_cleaning(2017)
df_2018 = simple_cleaning(2018)
df_2019 = simple_cleaning(2019)
df_2020 = simple_cleaning(2020)
df_all = pd.concat([df_2016,df_2017,df_2018,df_2019,df_2020])
df20 = cleaning(2020)


if page == 'Viz annuel':
        year = st.sidebar.slider(
        'Voir les données de l\'année : ',
        2016, 2020,2016)
        genre = st.sidebar.radio('Choix du type',
                ('Biens immobiliers','Terrains'))
        df = cleaning(year)
        type3,x = choix_genre(genre)                
        map = type3[['latitude','longitude']]
        valeur = type3[['valeur_fonciere']]

        #Création des columns
        col1, col2 = st.columns(2)

        #Séléction et Affichage des cartes région et département
        région = col1.selectbox('Sélectioner une région',
                                options=type3['Nom de la région'].unique(),
                                index=12)
        mask_region = type3['Nom de la région'].astype(str).str.contains(région)                               
        mask_region_count = df['Nom de la région'] == région 
        col1.subheader('Région')
        col1.header(région)
        col1.caption(f"Carte des {x}")
        col1.map(map[mask_region],zoom=6)
        col1.write(f'Nombre de {x} mise en vente en {year} :')
        col1.subheader(f'{int(map[mask_region].size)}')
        col1.write(f'Prix total des ventes en euros sur les {x} en {year} :')
        col1.subheader(f'{int(valeur[mask_region].sum())} €')


        département = col2.selectbox('Sélectioner un département',
                                options=type3['Nom du département'][mask_region].unique(),
                                index=6)
        mask_dep = type3['Nom du département'] == département
        mask_dep_count = df['Nom du département'] == département 
        col2.subheader('Département')
        col2.header(département)
        col2.caption(f"Carte des {x}")
        col2.map((map[mask_dep]),zoom=7.5)
        col2.write(f'Nombre de {x} mise en vente en {year} :')
        col2.subheader(f'{int(map[mask_dep][mask_dep_count].size)}')


#1 Carte régions avec valeur foncières 
st.subheader("First, the average property value per region : " )
with st.expander("More info :"):
    st.write('Ile de France is the first region, within the capital : Paris !')
régions=json.load(open("regions.geojson",'r'))
dfdep2020=cleaning(2020).groupby('Nom de la région').mean('valeur_fonciere')
choropleth=px.choropleth(data_frame=dfdep2020,geojson=régions, locations=dfdep2020.index,color='valeur_fonciere',scope="europe", featureidkey='properties.nom')
choropleth.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
st.write(choropleth)

#2 Pie avec nature mutation 
st.subheader("Now look about the type of sales" )
with st.expander("More info :"):
    st.write('Vente : Sales, Vente en l\'état futur d\'achevement : Sale in future state of completion')
dd = cleaning(2020).groupby('nature_mutation', as_index=False).count()
dd = dd[['date_mutation','nature_mutation']]
fig = px.pie(dd,values='date_mutation',names='nature_mutation',color_discrete_sequence=px.colors.sequential.Tealgrn[::-1])
fig.update_traces(textposition='inside')
fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
st.write(fig)

#3 Carte départements avec count ventes
st.subheader("Now look about the type of real estate" )
with st.expander("More info :"):
    st.write('Maisons : Houses, Appartement : Appartment, Dépendence : Dependency')
dd = cleaning(2020).groupby('nature_mutation', as_index=False).count()
dd = cleaning(2020).groupby('Biens immobiliers', as_index=False).count()
dd = dd[['date_mutation','Biens immobiliers']]
fig = px.pie(dd,values='date_mutation',names='Biens immobiliers',color_discrete_sequence=px.colors.sequential.Tealgrn[::-1])
fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
st.write(fig)

#5 Carte départements avec count ventes
st.subheader("What is the county with the most real estate transactions ? " )
dfdep20202=cleaning(2020).groupby('Nom du département').count()
with st.expander("Look at the Top 5 !"):
    st.write(dfdep20202.sort_values(by=['valeur_fonciere'], ascending=False).index[:5])
departements=json.load(open("departements1.geojson",'r'))
dfdep2020=cleaning(2020).groupby('code_departement').count()
dfdep2020.loc[20] = 5
dfdep2020.loc[57] = 5
dfdep2020.loc[67] = 5
dfdep2020.loc[68] = 5
choropleth=px.choropleth(dfdep2020,geojson=departements, locations=dfdep2020.index,color=dfdep2020.valeur_fonciere,scope="europe",featureidkey='properties.code')
choropleth.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
st.write(choropleth)


dataframe = "full_" + str(2020) + file_end
df = pd.read_csv(dataframe, 
        usecols=["date_mutation","code_postal"],
        delimiter=',',
        header=0,
        dtype={
        ("code_postal"):"float32"}
)
#Delete all na and duplicate 
df['date_mutation'] = pd.to_datetime(df['date_mutation'])
#Ajout d'un 0 afin d'avoir 5 chiffres pour tout les départements
df = df.dropna(subset=['code_postal'])
df["code_postal"] = df["code_postal"].astype(str)
df['code_postal'] = df['code_postal'].str.zfill(7) 
#Jointure pour avoir les noms des départements et des régions
correspondance_region = pd.read_csv('correspondance-code-cedex-code-insee.csv',delimiter=';')                
df.code_postal = ((df.code_postal.astype(float)).astype(int)).astype(str)
correspondance_region['Code Postal / CEDEX'] = ((correspondance_region['Code Postal / CEDEX'].astype(float)).astype(int)).astype(str)
df = df.merge(correspondance_region,left_on='code_postal', right_on='Code Postal / CEDEX',how='inner')
df = df.dropna(subset=['Nom du département','Nom de la région'])
df1 = df[['date_mutation','Nom de la région']]
df1.rename(columns={'valeur_fonciere':'valeur_fonciere'+str(2020)}, inplace = True)

df1 = cleaning(2020)
df1['month']= df1['date_mutation'].dt.month
df1.groupby('month',as_index=False).count()
fig = px.bar(df1,x='month', y='Nom de la région')
st.write(fig)





dd = cleaning(2020).groupby('Terrains', as_index=False).count()

dd = dd[['date_mutation','Terrains']]

fig = px.pie(dd,values='date_mutation',names='Terrains', hole=.3,color_discrete_sequence=px.colors.sequential.Tealgrn[::-1])
fig.update_traces(textposition='inside')
fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
st.write(fig)



df_all = df_all.groupby(['Nom de la région'],as_index=False).count()
dff = df_all[df_all['Nom de la région']=='ILE-DE-FRANCE']   
dff = dff.melt(id_vars=['Nom de la région'] , value_vars=['valeur_fonciere2016',
                                                    'valeur_fonciere2017','valeur_fonciere2018',
                                                    'valeur_fonciere2019','valeur_fonciere2020'])
fig = px.bar(dff,x='variable', y='value')
st.write(fig)

from htbuilder.units import px

def image(src_as_string, **style):
    return img(src=src_as_string, style=styles(**style))

def link(link, text, **style):
    return a(_href=link, _target="_blank", style=styles(**style))(text)

def layout(*args):

    style = """
    <style>
      # MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
     .stApp { bottom: 57px; }
    </style>
    """

    style_div = styles(
        position="fixed",
        left=0,
        bottom=0,
        margin=px(0, 0, 0, 0),
        width=percent(100),
        background_color='#C1EAFF',
        color="black",
        text_align="center",
        height="auto",
        opacity=1
    )

    style_hr = styles(
        display="block",
        margin=px(0, 0, 13, 0),
        border_style="inset",
        border_width=px(1)
    )

    body = p()
    foot = div(
        style=style_div
    )(
        hr(
            style=style_hr
        ),
        body
    )

    st.markdown(style, unsafe_allow_html=True)

    for arg in args:
        if isinstance(arg, str):
            body(arg)

        elif isinstance(arg, HtmlElement):
            body(arg)

    st.markdown(str(foot), unsafe_allow_html=True)

def layout2(*args):

    style = """
    <style>
      # MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
     .stApp { top: 50px; }
    </style>
    """

    style_div = styles(
        position="fixed",
        left=0,
        top=0,
        margin=px(-50, 0, 0, 0),
        width=percent(100),
        background_color='#C1EAFF',
        text_align="center",
        height="auto",
        opacity=1
    )

    style_hr = styles(
        display="block",
        border='solid',
        border_width=px(2),
    )

    body = p()
    foot = div(
        style=style_div
    )(
        hr(
            style=style_hr
        ),
        body
    )

    st.markdown(style, unsafe_allow_html=True)

    for arg in args:
        if isinstance(arg, str):
            body(arg)

        elif isinstance(arg, HtmlElement):
            body(arg)

    st.markdown(str(foot), unsafe_allow_html=True)

def footer():
    myargs = [
        "Made in ",
        image('https://i.postimg.cc/wTbVHYDJ/st-removebg-preview.jpg',
              width=px(25), height=px(25)),
        " with 💙 by ",
        link("https://www.linkedin.com/in/wassim-zouitene/", "Wassim_ZOUITENE"),
        " at 🏠",
    ]
    layout(*myargs)

def header():
    myargs = [
        #image('https://i.postimg.cc/Wbx2zqtB/logo.jpg',width=px(201), height=px(22))
        image('https://i.postimg.cc/RFyHy4kV/logo2.jpg',width=px(550), height=px(35))
    ]
    layout2(*myargs)


if __name__ == "__main__":
    footer()
    header()

 