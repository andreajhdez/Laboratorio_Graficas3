# Importar las librerías necesarias
import pandas as pd
import plotly.express as px

#PUNTO 1
# Definir los datos del dataset
data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    'materia': ['Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 
                'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 
                'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje'],
    'nota': [80, 65, 90, 75, 95, 70, 85, 60, 78, 82, 93, 68, 73, 88, 77, 50, 92, 63, 85, 79],
    'aprobado': ['Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'No', 'Sí', 'Sí']
}

#PUNTO 3
# Crear un DataFrame de Pandas
df = pd.DataFrame(data)

# Renombrar los valores en la columna 'aprobado'
df['aprobado'] = df['aprobado'].replace({'Sí': 'Aprobado', 'No': 'No Aprobado'})

# Contar la cantidad de aprobados y no aprobados
aprobados_count = df['aprobado'].value_counts().reset_index()
aprobados_count.columns = ['aprobado', 'count']

# Crear el pie chart con Plotly
fig = px.pie(aprobados_count, values='count', names='aprobado', 
             title='Gráfico de Torta')

# Mostrar la figura
fig.show()