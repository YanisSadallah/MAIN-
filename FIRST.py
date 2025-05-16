import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("C:/Users/YANIGOAT/Documents/HRDataset_v14.csv")
#PRESENTATION DES DATAS
print(data.shape)
print(data.head(20))
print(data.describe())
print(data.columns)
print(data.isnull().sum())
print(data.info())

#REGROUPEMENT DES TRAVAILLEURS PAR PERFORMANCE
print(data['PerformanceScore'].unique())
print(data['PerformanceScore'].value_counts())
print(data.groupby('PerformanceScore')['Absences'].mean())
sns.barplot(data=data, x='PerformanceScore', y='Absences')
plt.show()
#PREMIERE IMPRESSION : LA PRÉSENCE AU TRAVAIL PERMET L'EFFICACITÉ ; HYPOTHESE SUR LE GROUPE PIP : EFFECTIF FAIBLE/TRES SURVEILLÉ
#QUI SONT LES OUTLIERS EN TERME D'ABSENCE
premierquantile = data['Absences'].quantile(0.25)
troisiemequantile = data['Absences'].quantile(0.75)
IQR = troisiemequantile - premierquantile
print(IQR)
outliersabsence = data[data['Absences'] > troisiemequantile + 1.5*IQR]
print(troisiemequantile + 1.5*IQR)
#PAS DE DEPASSEMENT DE CE TAUX
print(data['Absences'].max())
#PERSONNE AU DESSUS DE 30 ABSENCES; 20 MAXIMUM
print(data['Sex'].value_counts())
#PLUS DE FEMMES DANS L'ENTREPRISE ; REPARTITION PAR GROUPE DE PERFORMANCE
print(data.groupby('PerformanceScore')['Sex'].value_counts())
#TEST CHI DEUX ENTRE SEXE ET GR DE PERF
print(data['GenderID'].value_counts())
import scipy.stats as stats
tableaucroise=pd.crosstab(data['GenderID'], data['PerformanceScore'])
from scipy.stats import chi2_contingency
print(chi2_contingency(tableaucroise))
#PVALUE SUPERIEURE AU SEUIL; ON NE REJETTE PAS L'HYPOTHESE