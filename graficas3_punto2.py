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

#PUNTO 2
# Crear un DataFrame de Pandas
df = pd.DataFrame(data)

# Asignar colores a cada materia
color_dict = {
    'Matemáticas': 'blue',
    'Historia': 'red',
    'Ciencias': 'green',
    'Lenguaje': 'purple'
}

# Crear el boxplot con Plotly
fig = px.box(df, x='materia', y='nota', color='materia',  category_orders={'materia': ['Matemáticas', 'Historia', 'Ciencias', 'Lenguaje']}, color_discrete_map=color_dict, title='Gráfica de Cajas',
             labels={'materia': '', 'nota': 'Valores'})

# Mostrar el gráfico
fig.show()
