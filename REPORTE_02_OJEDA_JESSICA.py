import csv

lista_datos = []
with open("synergy_logistics_database.csv", "r") as document:
    lector = csv.reader(document)
    
    for linea in lector:
        lista_datos.append(linea)
                    
#Codigo para consigna 1 "Opción 1) Rutas de exportacion e importacion, respectivamente"

dirección = "Exports"
contador_export = 0
exportaciones_contadas = []
conteo_exportaciones = []

for ruta in lista_datos:

    if ruta[1] == dirección:
        ruta_actual = [ruta[2], ruta[3]]
        
        if ruta_actual not in exportaciones_contadas:
            for movimiento in lista_datos:
              if ruta_actual == [movimiento[2], movimiento[3]] and movimiento[1]== dirección:
                contador_export += 1
            exportaciones_contadas.append(ruta_actual)
            conteo_exportaciones.append([ruta[2],ruta[3],contador_export])
            contador_export=0
conteo_exportaciones.sort(reverse = True, key = lambda x:x [2])
print (conteo_exportaciones)
contador=0
for importe in conteo_exportaciones:
    contador += int(importe[2])
print("el total de exportaciones es : ",contador)


dirección = "Imports"
contador_import = 0
importaciones_contadas = []
conteo_importaciones = []
for ruta in lista_datos:

    if ruta[1] == dirección:
        ruta_actual = [ruta[2], ruta[3]]
        
        if ruta_actual not in importaciones_contadas:
            for movimiento in lista_datos:
              if ruta_actual == [movimiento[2], movimiento[3]] and movimiento[1]== dirección:
                contador_import += 1
            importaciones_contadas.append(ruta_actual)
            conteo_importaciones.append([ruta[2],ruta[3],contador_import])
            contador_import=0
conteo_importaciones.sort(reverse = True, key = lambda x:x [2])
print (conteo_importaciones)

contador2=0
for importe in conteo_importaciones:
    contador2 += int(importe[2])
print("el total de importaciones es : ",contador2)

#lo que consideraba que me ayudaria a una comclusion mas completa:

#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import plotly.express as px


# In[2]:


dataset = pd.read_csv("/Users/jessicaO.O/Downloads/synergy_logistics_database.csv")
dataset = pd.DataFrame(dataset)
dataset


# In[3]:


dataset["ex"]= "Exports"
dataset


# In[4]:


dataset_exports= dataset.query("direction == ex")[["origin", "destination", "total_value"]]
dataset_exports['ruta_name'] = dataset_exports["origin"].map(str) + "-" + dataset_exports["destination"]
dataset_exports


# In[5]:


#media = data.groupby(['Group'])['Free_Energy'].mean()
agrupar_exports = dataset_exports.groupby(['ruta_name'])['total_value'].sum()
agrupar_exports =pd.DataFrame(agrupar_exports)
#by_year = planets.sort_values('year')
agrupar_exports= agrupar_exports.sort_values('total_value')
agrupar_exports


# In[6]:


#fig = px.bar(data_canada, x='year', y='pop')
#fig.show()

fig = px.bar(agrupar_exports)
fig.show()


# In[7]:


dataset["imp"]= "Imports"
dataset


# In[8]:


dataset_exports= dataset.query("direction == imp")[["origin", "destination", "total_value"]]
dataset_exports['ruta_name'] = dataset_exports["origin"].map(str) + "-" + dataset_exports["destination"]
dataset_exports


# In[9]:


#media = data.groupby(['Group'])['Free_Energy'].mean()
agrupar_exports = dataset_exports.groupby(['ruta_name'])['total_value'].sum()
agrupar_exports =pd.DataFrame(agrupar_exports)
#by_year = planets.sort_values('year')
agrupar_exports= agrupar_exports.sort_values('total_value')
agrupar_exports


# In[10]:


#fig = px.bar(data_canada, x='year', y='pop')
#fig.show()

fig = px.bar(agrupar_exports)
fig.show()


# In[11]:


dataset = pd.read_csv("/Users/jordy/Downloads/synergy_logistics_database.csv")
dataset = pd.DataFrame(dataset)
dataset


# In[12]:


tran= dataset['transport_mode']
tran= pd.DataFrame(tran)
tran['total_value']= dataset['total_value']
tran


# In[13]:


#agrupar_exports = dataset_exports.groupby(['ruta_name'])['total_value'].sum()
agrupar_transport = tran.groupby(['transport_mode'])['total_value'].sum()
agrupar_transport =pd.DataFrame(agrupar_transport)
#agrupar_exports= agrupar_exports.sort_values('total_value')
agrupar_transport = agrupar_transport.sort_values('total_value')
agrupar_transport


# In[14]:


fig = px.bar(agrupar_transport)
fig.show()


# In[15]:


dataset = pd.read_csv("/Users/jessicaO.O/Downloads/synergy_logistics_database.csv")
dataset = pd.DataFrame(dataset)
dataset["ex"]= "Exports"
dataset["imp"]= "Imports"
dataset_imports_origin= dataset.query("direction == imp")[["origin", "total_value"]]
dataset_imports_destination= dataset.query("direction == imp")[["destination", "total_value"]]
dataset_exports_origin= dataset.query("direction == ex")[["origin", "total_value"]]
dataset_exports_destination= dataset.query("direction == ex")[["destination", "total_value"]]


# In[16]:


#Generando listas y juntandolas
list_exports_origin_country = dataset_exports_origin['origin']
list_exports_origin_totalv = dataset_exports_origin['total_value']
list_exports_destination_country = dataset_exports_destination['destination']
list_exports_destination_totalv = dataset_exports_destination['total_value']

list_imports_origin_country = dataset_imports_origin['origin']
list_imports_origin_totalv = dataset_imports_origin['total_value']
list_imports_destination_country = dataset_imports_destination['destination']
list_imports_destination_totalv = dataset_imports_destination['total_value']

list_coutry = []

list_coutry =+ list_exports_origin_country 
list_coutry =+ list_exports_destination_country 
list_coutry =+ list_imports_origin_country 
list_coutry =+ list_imports_destination_country 

list_totalv = []

list_totalv =+ list_exports_origin_totalv
list_totalv =+ list_exports_destination_totalv
list_totalv =+ list_imports_origin_totalv
list_totalv =+ list_imports_destination_totalv


# In[17]:


total_country = []
total_country = pd.DataFrame(total_country)
total_country['country']= list_coutry
total_country['total_value'] = list_totalv

total_country


# In[18]:


total_country = total_country.groupby(['country'])['total_value'].sum()
total_country = pd.DataFrame(total_country)
total_country = total_country.sort_values('total_value')
total_country


# In[20]:


fig = px.bar(total_country)
fig.show()


# In[ ]:







