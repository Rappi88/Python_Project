import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
import numpy as np



df = pd.read_csv('C:/Users/cg12680/OneDrive - Cerved/Documents/Python_Project/Performance_Account.csv',
                 index_col="Cod_Agente",
                 sep=";",
                 header=0)

### Analisi del DB e del tipo di variabili / colonne contenute

df.shape
df.head(10)

df_null = df[df.isna().any(axis=1)]



df.loc[(df["Enasarco_Dipendente"] == "Enasarco") & (df["Qualità_lavoro"]>=1)]
df.loc[(df["Enasarco_Dipendente"] == "Enasarco") | (df["Qualità_lavoro"]>=1)]

missing_value = df.isnull().sum()
missing_value


df.describe()
df.info()
df.columns

# Voglio convertire gli object in valori numerici

df["Anagrafiche_visitate_>2"]=pd.to_numeric(df['Anagrafiche_visitate_>2'], errors='coerce')
media_anag_visit=df["Anagrafiche_visitate_>2"].mean()
df = df.fillna({"Anagrafiche_visitate_>2": media_anag_visit}, inplace=True)


#df["Perc_visitate_>2"]=pd.to_numeric(df['Perc_visitate_>2'], errors='coerce')
#df["Durata_media_opp_vinte_>5"]=pd.to_numeric(df['Durata_media_opp_vinte_>5'].str.replace(".",","), errors='coerce')
#df["Durata_media_opp_aperte"]=pd.to_numeric(df['Durata_media_opp_aperte'], errors='coerce')
#df["Ticket_Medio"]=pd.to_numeric(df['Ticket_Medio'], errors='coerce')
#df["Churn_NUM_Totale"]=pd.to_numeric(df['Churn_NUM_Totale'], errors='coerce')
#df["Churn_VAL_Totale"]=pd.to_numeric(df['Churn_VAL_Totale'], errors='coerce')
#df["VALUTAZIONE_AM"]=pd.to_numeric(df['VALUTAZIONE_AM'], errors='coerce')

df.info()


### voglio provare a vedere se ci sono correlazioni interessanti 
### (altre opzioni sono: "hist", "ecdf", "kde")
### sns.displot(data=df["Enasarco_Dipendente"], kind='hist', rug=True, height=5, aspect=2)
sns.barplot(x=df["Enasarco_Dipendente"], y=df["TARGET_PRESI_VT1"])
sns.heatmap(data=df["Qualità_lavoro"], annot=True)


### tipologie di scatterplot
sns.scatterplot(x=df["Qualità_lavoro"], y=df["TARGET_PRESI_VT1"], hue=df["Enasarco_Dipendente"])
sns.regplot(x=df["Qualità_lavoro"], y=df["TARGET_PRESI_VT1"])                           
sns.lmplot(x="Clienti_Tot", y="TARGET_PRESI_VT1", 
           hue="Enasarco_Dipendente",
           data=df)                              
# Caratteristiche del grafico (titolo, nome degli assi, dimensione figura, ...)
plt.title("Analisi vs target presi")





