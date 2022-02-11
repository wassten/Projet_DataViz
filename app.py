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
import locale
locale.setlocale(locale.LC_ALL, '')
from PIL import Image
from functools import wraps
from time import time
#footer
import streamlit as st
from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent
from htbuilder.funcs import rgba, rgb

#Page configuration
st.set_page_config(layout="wide",page_title='Real Investate', page_icon=Image.open('ri.JPG'))

st.write('🎹 🎶 A little bit of Aznavour 🎶 🎹')
audio_file = open('aznavour.mp3', 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/mp3', start_time = 7)

# Create connection object.
# `anon=False` means not anonymous, i.e. it uses access keys to pull data.
#fs = s3fs.S3FileSystem(anon=False)

# Retrieve file contents.
# Uses st.cache to only rerun when the query changes or after 10 min.
#@st.cache(ttl=600)
#def read_file(filename):
#    with fs.open(filename) as f:
#        return f.read().decode("utf-8")

#content = read_file("streamlitw/full_2016.csv.csv")
#st.write(content)


df1 = pd.read_csv("https://chenutfamily.freeboxos.fr:45883/share/GOrVpuxe12bweaK9/full_2020_1.csv",nrows=300000,memory_map=True,low_memory=False,usecols=['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude'])[['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude']]
df2 = pd.read_csv("https://chenutfamily.freeboxos.fr:45883/share/-mqSOhjWBxt-rSMZ/full_2020_2.csv",nrows=300000,low_memory=False,usecols=['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude'])[['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude']]
full_2020=pd.concat([df1,df2])

df6 = pd.read_csv("https://chenutfamily.freeboxos.fr:45883/share/U_Nn5m1-sXAux1qO/full_2019_1.csv",nrows=300000,memory_map=True,low_memory=False,usecols=['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude'])[['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude']]
df3 = pd.read_csv("https://chenutfamily.freeboxos.fr:45883/share/zogg9pmrCYohCAyX/full_2019_2.csv",nrows=300000,low_memory=False,usecols=['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude'])[['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude']]
df4 = pd.read_csv("https://chenutfamily.freeboxos.fr:45883/share/QN5fX5w0qiLStf-o/full_2019_3.csv",nrows=300000,memory_map=True,low_memory=False,usecols=['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude'])[['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude']]
df5 = pd.read_csv("https://chenutfamily.freeboxos.fr:45883/share/-hVR2tOISmPUcNEG/full_2019_4.csv",nrows=300000,low_memory=False,usecols=['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude'])[['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude']]

full_2020=pd.concat([df3,df4,df5,df6])

df1 = pd.read_csv("https://chenutfamily.freeboxos.fr:45883/share/GOrVpuxe12bweaK9/full_2020_1.csv",nrows=300000,memory_map=True,low_memory=False,usecols=['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude'])[['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude']]
df2 = pd.read_csv("https://chenutfamily.freeboxos.fr:45883/share/-mqSOhjWBxt-rSMZ/full_2020_2.csv",nrows=300000,low_memory=False,usecols=['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude'])[['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude']]
full_2020=pd.concat([df1,df2])

df1 = pd.read_csv("https://chenutfamily.freeboxos.fr:45883/share/GOrVpuxe12bweaK9/full_2020_1.csv",nrows=300000,memory_map=True,low_memory=False,usecols=['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude'])[['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude']]
df2 = pd.read_csv("https://chenutfamily.freeboxos.fr:45883/share/-mqSOhjWBxt-rSMZ/full_2020_2.csv",nrows=300000,low_memory=False,usecols=['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude'])[['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude']]
full_2020=pd.concat([df1,df2])

df1 = pd.read_csv("https://chenutfamily.freeboxos.fr:45883/share/GOrVpuxe12bweaK9/full_2020_1.csv",nrows=300000,memory_map=True,low_memory=False,usecols=['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude'])[['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude']]
df2 = pd.read_csv("https://chenutfamily.freeboxos.fr:45883/share/-mqSOhjWBxt-rSMZ/full_2020_2.csv",nrows=300000,low_memory=False,usecols=['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude'])[['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude']]
full_2020=pd.concat([df1,df2])










#Important variable
path = "https://jtellier.fr/DataViz/"
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
file = open("time.txt", "w+")
def timing(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()
        file.write('Temps écoulé : {}'.format((end-start)) + "sec")
        return result
    return wrapper

def choix_genre(genre):
        if genre == 'Lands':
                mask_constructible = df['Terrains'] == 'terrains a bâtir'
                type2 = st.sidebar.radio('Type :',
                        ('Building','Non-building'))
                if type2 == 'Building':     
                        x = 'Terrains constructibles'
                        type3 = df[mask_constructible] 
                if type2 == 'non-building':
                        x = 'Terrains non-contructibles'
                        type3 = df[df['Terrains'] == 'sols']

        if genre == 'Property':
                type2 = st.sidebar.radio('Choix du type',
                        ('Houses','Appartments','Commerces'))
                if type2 == 'Houses':  
                        x = 'maisons'
                        type3 = df[df['Biens immobiliers']=='Maison'] 
                if type2 == 'Appartments':
                        x = 'appartements'
                        type3 = df[df['Biens immobiliers']=='Appartement']
                if type2 == 'Commerces': 
                        x = 'commerces'      
                        type3 = df[df['Biens immobiliers']=='Local industriel. commercial ou assimilé']
        return type3, x


@timing
@st.cache
def cleaning(years):
        dataframe = file + str(years)
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
        dataframe = file + str(years)
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
        dataframe = file + str(years)
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

df_2016 = simple_cleaning(2016)
df_2017 = simple_cleaning(2017)
df_2018 = simple_cleaning(2018)
df_2019 = simple_cleaning(2019)
df_2020 = simple_cleaning(2020)
df_all = pd.concat([df_2016,df_2017,df_2018,df_2019,df_2020])
df20 = cleaning(2020)

page = st.sidebar.radio('',
                ('Accueil','Data explorer'))


if page == 'Accueil':
        col1, col2 = st.columns(2)
        col2.image(Image.open('paris1.jpg'), caption='Eiffel Tower on the Seine')
        col1.header("Welcome to Real Investate")
        col1.subheader("In this special issue #5, we'll talk about Open Data 📊 !")
        col1.subheader("After Italy 🍕, France 🥐 is the second european country to release websites to provide Open Data.")
        col1.subheader("And as you can imagine, it's really interesting :eyes:" )
        col1.subheader("Lest's begin with some viz !" )
        st.markdown("---")
        
        
        #1 Carte régions avec valeur foncières 
        st.subheader("First, the average property value per region : " )
        col1, col2 = st.columns(2)
        with col1.expander("More info :"):
            st.write('Ile de France is the first region, within the capital : Paris !')
        régions=json.load(open("regions.geojson",'r'))
        dfdep2020=df20.groupby('Nom de la région')['valeur_fonciere'].mean()
        choropleth=px.choropleth(data_frame=dfdep2020,geojson=régions, locations=dfdep2020.index,color='valeur_fonciere',scope="europe", featureidkey='properties.nom')
        choropleth.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        col2.write('Census for comparaison')
        col2.image(Image.open('census.JPG'), caption='Census')
        col1.write(choropleth)

        col1, col2 = st.columns(2)
        #2 Pie avec nature mutation
        col1.subheader("Now look about the type of sales :" )
        with col1.expander("More info :"):
            st.write('Vente : Sales, Vente en l\'état futur d\'achevement : Sale in future state of completion')
        dd = df20.groupby('nature_mutation', as_index=False).count()
        dd = dd[['date_mutation','nature_mutation']]
        fig = px.pie(dd,values='date_mutation',names='nature_mutation',color_discrete_sequence=px.colors.sequential.Tealgrn[::-1])
        fig.update_traces(textposition='inside')
        fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
        col1.write(fig)

        #3 Pir type of real estate
        col2.subheader("And the type of real estate :" )
        with col2.expander("More info :"):
            st.write('Maisons : Houses, Appartement : Appartment, Dépendence : Dependency')
        dd = df20.groupby('nature_mutation', as_index=False).count()
        dd = df20.groupby('Biens immobiliers', as_index=False).count()
        dd = dd[['date_mutation','Biens immobiliers']]
        fig = px.pie(dd,values='date_mutation',names='Biens immobiliers',color_discrete_sequence=px.colors.sequential.Tealgrn[::-1])
        fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
        col2.write(fig)

        #4 Carte départements avec count ventes
        st.subheader("What is the county with the most real estate transactions ? " )
        col1, col2 = st.columns(2) 
        dfdep20202=df20.groupby('Nom du département').count()
        with col2.expander("Look at the Top 5 !"):
            st.write(dfdep20202.sort_values(by=['valeur_fonciere'], ascending=False).index[:5])
        departements=json.load(open("departements1.geojson",'r'))
        dfdep2020=df20.groupby('code_departement').count()
        dfdep2020.loc[20] = 5
        dfdep2020.loc[57] = 5
        dfdep2020.loc[67] = 5
        dfdep2020.loc[68] = 5
        choropleth=px.choropleth(dfdep2020,geojson=departements, locations=dfdep2020.index,color=dfdep2020.valeur_fonciere,scope="europe",featureidkey='properties.code')
        choropleth.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        col1.image(Image.open('aisne.jpeg'), caption='Cathedral of Laon in the county of Aisne.')
        col2.write(choropleth)

        #5 Carte départements avec count ventes
        st.subheader("Lands are interesting aswell :" )
        with st.expander("More info :"):
            st.write('Double-click to see the value you are interested of.')
        dd = df20.groupby('Terrains', as_index=False).count()

        dd = dd[['date_mutation','Terrains']]

        fig = px.pie(dd,values='date_mutation',names='Terrains', hole=.3,color_discrete_sequence=px.colors.sequential.Tealgrn[::-1])
        fig.update_traces(textposition='inside')
        fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
        st.write(fig)


        #6 Property value per years
        st.subheader("Now, your turn !" )
        st.subheader("A bar chart with property value per years :" )
        col1, col2 = st.columns(2)
        with col1.expander("Choose your county :"):
            régions = st.selectbox('Select a county',
                                options=df_all['Nom de la région'].unique(),
                                index=12)                       
        df_all1 = df_all.groupby(['Nom de la région'],as_index=False).count()
        df_all1.rename(columns={'valeur_fonciere2016':'2016'}, inplace = True)
        df_all1.rename(columns={'valeur_fonciere2017':'2017'}, inplace = True)
        df_all1.rename(columns={'valeur_fonciere2018':'2018'}, inplace = True)
        df_all1.rename(columns={'valeur_fonciere2019':'2019'}, inplace = True)
        df_all1.rename(columns={'valeur_fonciere2020':'2020'}, inplace = True)        
        dff = df_all1[df_all1['Nom de la région']==régions]   
        dff = dff.melt(id_vars=['Nom de la région'] , value_vars=['2016',
                                                            '2017','2018',
                                                            '2019','2020'])
        fig = px.bar(dff,x='variable', y='value',labels={'variable':'Property value','value':"Year"})
        col1.write(fig)
        diff = int(100-(dff.iloc[4]['value']/dff.iloc[3]['value']*100))
        
        
        #For more personalization :)
        if régions == 'AUVERGNE-RHONE-ALPES':
            pic =  'auvergne-rhone-alpes'
        elif régions == 'BOURGOGNE-FRANCHE-COMTE':
            pic = 'bourgogne-franche-comte'
        elif régions == 'BRETAGNE':
            pic = 'bretagne'
        elif régions == 'CENTRE-VAL DE LOIRE':
            pic = 'centre-val-de-loire'
        elif régions == 'CORSE':
            pic = 'corse'
        elif régions == 'GRAND EST':
            pic = 'grand-est'
        elif régions == 'GUADELOUPE':
            pic = 'guadeloupe'
        elif régions == 'ILE-DE-FRANCE':
            pic = 'ile-de-france'
        elif régions == 'OCCITANIE':
            pic = 'occitanie'
        elif régions == 'GUYANE':
            pic = 'guyane'           
        elif régions == 'MARTINIQUE':
            pic = 'martinique'
        elif régions == 'PAYS DE LA LOIRE':
            pic = 'pays-de-la-loire'
        elif régions == 'NOUVELLE-AQUITAINE':
            pic = 'nouvelle-aquitaine'
        elif régions == 'NORMANDIE':
            pic = 'normandie'    
        elif régions == 'HAUTS-DE-FRANCE':
            pic = 'hauts-de-france'
        elif régions == 'LA REUNION':
            pic = 'la-reunion'
        elif régions == 'PROVENCE-ALPES-COTE D\'AZUR':
            pic = 'provence-alpes-cote-d-azur'    


        col2.image(f'https://nestenn.com/public/img/regions/{pic}.jpg', caption=f'A glimpse of {régions}')
        st.info(f'As you can see, COVID-19 has a noteworthy impact on real estate in France. In county {régions}, we can see a difference of {diff} % between 2019 and 2020. ')
        
        st.markdown('---')


        agree = st.checkbox('See a portion of the dataframe use in this article')
        agree2 = st.checkbox('Group by county')
        if agree:
            st.write(df20.head(10))
        if agree2:
            st.write(df20.groupby('Nom de la région').mean())
        st.info('All viz above are only from 2020 expect the bar chart')


if page == 'Data explorer':
        year = st.sidebar.slider(
        'Choose a year: ',
        2016, 2020,2016)
        genre = st.sidebar.radio('Type of real estate :',
                ('Property','Lands'))
        df = cleaning(year)
        type3,x = choix_genre(genre)                
        map = type3[['latitude','longitude']]
        valeur = type3[['valeur_fonciere']]

        #Création des columns
        col1, col2 = st.columns(2)
        col11,col22,col33,col44=st.columns(4)

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
        col11.subheader(locale.format('%d', int(valeur[mask_region].sum()), grouping=True))
        col22.subheader('.   €')


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
        col2.write(f'Prix total des ventes en euros sur les {x} en {year} :')
        col33.subheader(locale.format('%d', int(valeur[mask_dep].sum()), grouping=True))
        col44.subheader('€')


st.info('Source of the dataset :  https://www.data.gouv.fr/en/datasets/demandes-de-valeurs-foncieres/ ')


#Footer and Layer with images and links (LinkedIn)
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
        image('https://i.postimg.cc/RFyHy4kV/logo2.jpg',width=px(550), height=px(35))
    ]
    layout2(*myargs)

footer()
header()

 
