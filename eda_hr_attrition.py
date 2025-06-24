# eda_hr_attrition.ipynb

# Librerías iniciales
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
sns.set(style="whitegrid")

# Cargar dataset
df = pd.read_csv(r'C:\Users\César\Documents\GitHub\mi-portafolio\hr-attrition-analysis\WA_Fn-UseC_-HR-Employee-Attrition.csv')

print("Shape del dataset:", df.shape) # Vista general
df.head() # Primeras filas del dataset
df.info() # Información general del dataset
df.describe() # Estadísticas descriptivas
df.isnull().sum().sort_values(ascending=False) # Verificar valores nulos

print(df['Attrition'].value_counts(normalize=True)) # Proporción de empleados que abandonaron la empresa

# Visualización de la distribución de la variable 'Attrition'
attrition_counts= df['Attrition'].value_counts()
attrition_counts.plot(kind='bar', color=['#1f77b4', '#ff7f0e'], title='Distribución de Abandono de Empleados vs No Abandono')
plt.xlabel('Abandono de Empleados')
plt.ylabel('Cantidad de Empleados')
plt.show()

# Variables numéricas principales
numericas = ['Age', 'DailyRate', 'DistanceFromHome', 'HourlyRate', 'MonthlyIncome',
             'MonthlyRate', 'NumCompaniesWorked', 'PercentSalaryHike',
             'TotalWorkingYears', 'TrainingTimesLastYear', 'YearsAtCompany',
             'YearsInCurrentRole', 'YearsSinceLastPromotion', 'YearsWithCurrManager']

# Histograma para cada variable numérica
plt.figure(figsize=(20, 10))
for i, col in enumerate(numericas):
    plt.subplot(4, 4, i + 1)
    sns.histplot(df[col], kde=True, bins=20)
    plt.title(f'Distribución de {col}')
plt.tight_layout()
plt.show()

## Observaciones Iniciales
'- La mayoría de empleados tienen entre 30 y 40 años.'
'- La mayoría gana entre $2,000 y $6,000 mensuales.'
'- Pocos empleados tienen más de 10 años sin promoción.'
'- Los años en la empresa y en el rol actual están sesgados hacia valores bajos, lo que podría estar relacionado con la rotación.'

# Variables categóricas clave
categoricas = ['BusinessTravel', 'Department', 'EducationField', 'Gender', 
               'JobRole', 'MaritalStatus', 'OverTime', 'JobSatisfaction', 'EnvironmentSatisfaction']

plt.figure(figsize=(15, 15))
for i, col in enumerate(categoricas):
    plt.subplot(3, 3, i + 1)
    sns.countplot(x=col, data=df, order=df[col].value_counts().index)
    plt.title(f'Conteo por {col}')
    plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

## Hallazgos iniciales en variables categóricas
'- Hay más empleados en el departamento de R&D que en los otros.'
'- El rol de "Sales Executive" es el más común.'
'- Una proporción considerable hace horas extra (`OverTime = Yes`).'
'- La mayoría están casados o solteros.'
'- Las calificaciones de satisfacción laboral y ambiente están bien distribuidas (poco sesgo).'

# Variables numéricas relevantes para comparar
numericas_comparar = ['Age', 'MonthlyIncome', 'YearsAtCompany', 'TotalWorkingYears',
                      'YearsInCurrentRole', 'YearsSinceLastPromotion', 'DistanceFromHome']

plt.figure(figsize=(20, 15))
for i, col in enumerate(numericas_comparar):
    plt.subplot(3, 3, i + 1)
    sns.boxplot(x='Attrition', y=col, data=df, palette='Set2')
    plt.title(f'{col} según Attrition')
plt.tight_layout()
plt.show()

## Comparaciones clave entre empleados que se fueron vs. se quedaron

'- Los empleados que renunciaron tienden a ser más jóvenes.'
'- Suelen tener menos años en la empresa y en el rol actual.'
'- Tienen ingresos ligeramente más bajos, aunque la diferencia no es extrema.'
'- La distancia desde casa parece ser un factor: los que viven más lejos tienden a renunciar más.'

# Variables categóricas importantes
categoricas_comparar = ['OverTime', 'JobRole', 'MaritalStatus', 'Gender', 'Department', 'BusinessTravel']

plt.figure(figsize=(15, 15))
for i, col in enumerate(categoricas_comparar):
    plt.subplot(2, 3, i + 1)
    attrition_rate = pd.crosstab(df[col], df['Attrition'], normalize='index') * 100
    attrition_rate[['Yes']].sort_values(by='Yes', ascending=False).plot(kind='barh', legend=False, ax=plt.gca())
    plt.title(f'Tasa de renuncia por {col}')
    plt.xlabel('Porcentaje de renuncia')
plt.tight_layout()
plt.show()

## ¿Qué roles o condiciones tienen mayor rotación?

'- Los empleados con horas extra (OverTime) renuncian mucho más.'
'- Algunos puestos como Laboratory Technician o Sales Representative tienen tasas de rotación elevadas.'
'- Los empleados solteros se van más que los casados.'
'- Hay más rotación en el departamento de Sales que en R&D.'
'- Los que viajan con frecuencia (frequent travel) también presentan una mayor rotación.'

# Correlación de variables numéricas
plt.figure(figsize=(12, 10))
sns.heatmap(df[numericas_comparar].corr(), annot=True, cmap='coolwarm')
plt.title('Matriz de correlación')
plt.show()