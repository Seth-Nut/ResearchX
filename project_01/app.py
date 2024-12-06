import streamlit as st
import numpy as np
import base64
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Initial page config
st.set_page_config(
    page_title="Análisis Carrera de Ingeniería V región de Chile",
    layout="wide",
    initial_sidebar_state="expanded",
)


# extra classes
class SidebarText:
    introduction = """
        <small> 
        Este análisis brinda una visión global del desempeño académico y la experiencia estudiantil, abordando retención, tiempos de egreso, carga académica, matrícula y factores curriculares. El objetivo es guiar mejoras continuas y optimizar la formación. 
        

        </small>
        """
    goals = """
        <small>  

- 📈 Identificar tendencias en matrícula, egreso y titulación  
- 🏗️ Evaluar carga académica y plan de estudios  
- 🔍 Analizar indicadores clave (aprobación, retención, progresión)  
- 🌱 Orientar el fortalecimiento continuo de la carrera

     </small> 
        """

class BodyText:

    intro ="""
### **Descripción General del Programa**

La carrera está diseñada para completarse en un período de **5 años**, equivalente a **10 semestres académicos**. A lo largo del programa, los estudiantes cursan un total de **57 asignaturas**, distribuidas en distintos niveles, desde los básicos hasta los más avanzados. Estas asignaturas acumulan un total de **209 créditos**, con una carga académica balanceada entre formación teórica y práctica.

---

### **Distribución de Asignaturas por Nivel**

- **Niveles Iniciales (1 y 2)**  
  Comprenden los dos primeros años de la carrera, con un enfoque en desarrollar bases sólidas en los conocimientos fundamentales.  
  - **Cantidad de cursos:** 13.  
  - **Créditos totales:** 52.  
  - **Tasas de aprobación:** Varían entre el 47% y el 96%.  
  - **Departamentos involucrados:** depto_1, depto_2 y depto_3.

- **Niveles Intermedios (3 y 4)**  
  Los cursos en estos niveles profundizan en los conocimientos previos y preparan a los estudiantes para abordar problemáticas más complejas.  
  - **Cantidad de cursos:** 20.  
  - **Créditos totales:** 72.  
  - **Tasas de aprobación:** Varían entre el 50% y el 84%.  
  - **Departamentos involucrados:** depto_2, depto_3 y depto_4.

- **Niveles Avanzados (5 al 10)**  
  Durante los últimos años, las asignaturas se orientan a la especialización y aplicación de los conocimientos adquiridos en proyectos multidisciplinarios.  
  - **Cantidad de cursos:** 24.  
  - **Créditos totales:** 85.  
  - **Tasas de aprobación:** Generalmente superiores al 75%, con varios cursos alcanzando el 100%.  
  - **Departamentos involucrados:** depto_2, depto_5, depto_7, y depto_8.

    """

    carrera = """

Este programa de ingeniería, impartido en una institución de prestigio, reúne a estudiantes con diversos antecedentes académicos y socioeconómicos. A continuación, se destacan aspectos clave del programa:

- **Identificación y Desempeño Académico:**
  - Cada estudiante tiene un código único que permite monitorear su trayectoria.
  - Indicadores como el Promedio de Notas de Enseñanza Media (NEM) y puntajes de ingreso destacan su preparación previa.

- **Origen y Diversidad:**
  - Los estudiantes provienen de diversas regiones y tipos de establecimientos educativos (públicos, privados y subvencionados), lo que enriquece el entorno académico.

- **Continuidad y Preferencias:**
  - La elección de este programa refleja su prestigio entre los estudiantes.
  - Datos como el año de egreso de la educación secundaria permiten analizar tendencias y niveles de persistencia.

- **Apoyo Financiero:**
  - Becas y créditos estudiantiles facilitan el acceso y la permanencia en el programa.
  - Estos apoyos son fundamentales para reducir barreras económicas y fomentar el desarrollo académico.


"""
    

class ImagesURL:
    icon = "https://cdn.iconscout.com/icon/free/png-256/free-graduating-student-icon-download-in-svg-png-gif-file-formats--female-education-study-school-back-to-pack-icons-2042096.png"
    img_01 = "https://cdni.iconscout.com/illustration/premium/thumb/career-advancement-illustration-download-in-svg-png-gif-file-formats--vocational-training-professional-development-guidance-educational-pathways-education-pack-school-illustrations-9506614.png"
class DataURL:
    path_data = 'https://raw.githubusercontent.com/Seth-Nut/ResearchX/refs/heads/main/project_01/data/'
    previo_universidad = path_data + 'datos_previos_anonimizados.csv'
    durante_universidad = path_data + 'datos_durante_anonimizados.csv'
    malla = path_data + 'malla_anonimizados.csv'

# extra functions
# Función para crear el histograma
def create_histogram_preu(df, column_name, hue=None):
    fig = px.histogram(df, x=column_name, color=hue,
                       title=f'Histograma de {column_name}' + (f' por {hue}' if hue else ''),
                       color_discrete_sequence=px.colors.sequential.Teal)
    fig.update_layout(
        xaxis_title=column_name,
        yaxis_title='Frequency'
    )
    fig.update_traces(marker=dict(line=dict(color="black", width=1)))
    st.plotly_chart(fig)

# Función para crear el countplot
def create_countplot_preu(df, column_name, hue=None):
    fig = px.histogram(df, y=column_name, color=hue, title=f'Count Plot de {column_name}' + (f' por {hue}' if hue else ''),
                       category_orders={column_name: df[column_name].value_counts().index},
                       color_discrete_sequence=px.colors.sequential.Teal)
    fig.update_layout(
        xaxis_title='Count',
        yaxis_title=column_name
    )
    fig.update_traces(marker=dict(line=dict(color="black", width=1)))
    st.plotly_chart(fig)

def plot_numeric_variables(df):
    st.markdown("""<big>Numeric Variables </big>""", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    x_column_options = [
        'puntaje_ingreso',
        'puntaje_psu',
        'psu_lenguaje',
        'psu_matematica',
        'nem',
        'porcentaje_beca'
    ]

    for col in x_column_options:
        df[col] = df[col].replace(0, np.nan)

    x_column = col1.selectbox("Select column:", options=x_column_options)
    plot_type_options = [
        "univariate",
        "bivariate",
    ]  # You can add more plot types if you wish
    plot_type = col2.selectbox("Numeric Plot type:", options=plot_type_options)

    if plot_type == "univariate":
        create_histogram_preu(df,x_column)
    else:
        create_histogram_preu(df, x_column,'estado')

def plot_categorical_variables(df):
    st.markdown("""<big>Categorical Variables </big>""", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    x_column_options_cat = [
        'region',
        'tipo_colegio',
        'preferencia',
        'continuidad'
    ]

    x_column_cat = col1.selectbox("Select column:", options=x_column_options_cat)
    plot_type_options_cat = [
        "univariate",
        "bivariate"
    ]  # You can add more plot types if you wish
    plot_type_cat = col2.selectbox("Categorical Plot type:", options=plot_type_options_cat)

    if plot_type_cat == "univariate":
        # Create a bar plot with Altair
        create_countplot_preu(df, x_column_cat)
    else:
        create_countplot_preu(df, x_column_cat, 'estado')


def create_heatmap_malla(malla):
    # Calcular el conteo de cursos por nivel
    conteo = malla.groupby('nivel').size().reset_index(name='total')
    max_courses = malla.groupby('nivel')['sigla'].count().max()

    frames = []

    # Crear DataFrame adicional para rellenar con filas vacías
    for nivel in malla['nivel'].unique():
        valor = conteo.loc[conteo['nivel'] == nivel, 'total'].values[0]
        temp = pd.DataFrame(columns=malla.columns).sort_values(['nivel', 'sigla'])
        temp['nivel'] = [nivel] * (max_courses - valor)
        temp['sigla'] = ""
        frames.append(temp.fillna(0))

    df_extra = pd.concat(frames)
    malla_new = pd.concat([malla, df_extra])#.sort_values(['nivel', 'creditos'], ascending=[True, False])
    malla_new['enumeracion'] = malla_new.groupby('nivel').cumcount() + 1
    malla_new['nivel'] = malla_new['nivel'].astype(int)
    malla_new.loc[malla_new['aprobacion'] == '', 'aprobacion'] = 0

    # Crear una tabla pivote para el heatmap, llenando celdas vacías con NaN
    pivot_table = malla_new.pivot(index='enumeracion', columns='nivel', values='aprobacion').fillna(0)

    # Crear anotaciones personalizadas con siglas
    annotations = malla_new.pivot(index='enumeracion', columns='nivel', values='sigla')

    # Invertir el orden de las filas para que vayan de 1 a 7 de arriba hacia abajo
    pivot_table = pivot_table.iloc[::-1]
    annotations = annotations.iloc[::-1]

    # Crear el heatmap con Plotly
    fig = go.Figure(data=go.Heatmap(
        z=pivot_table.values,
        x=pivot_table.columns,
        y=pivot_table.index,
        text=annotations.values,
        colorscale='Blues',
        showscale=True,
        hoverinfo="text+z"
    ))

    # Actualizar el texto de las anotaciones a color blanco
    fig.update_traces(texttemplate='%{text}', textfont=dict(color='white'))

    fig.update_layout(
        title='Heatmap de Aprobacion por Nivel y Sigla',
        xaxis_nticks=36,
        xaxis_title='Nivel',
        yaxis_title='Enumeracion',
        yaxis_autorange='reversed'  # Invertir el eje y
    )

    st.plotly_chart(fig)






# Define img_to_bytes() function
def img_to_bytes(img_url):
    response = requests.get(img_url)
    img_bytes = response.content
    encoded = base64.b64encode(img_bytes).decode()
    return encoded



# main function
def main():
    """
    Main function to set up the Streamlit app layout.
    """
    cs_sidebar()
    cs_body()
    return None

# Define the cs_sidebar() function
def cs_sidebar():
    """
    Populate the sidebar with various content sections related to Python.
    """

    st.sidebar.markdown(
        """[<img src='data:image/png;base64,{}' class='img-fluid' width=200 >](https://streamlit.io/)""".format(
            img_to_bytes(
                ImagesURL.icon
            )
        ),
        unsafe_allow_html=True,
    )

    st.sidebar.header("Análisis Exploratorio en una carrera de ingeniería en la V región de Chile")


    st.sidebar.markdown(SidebarText.introduction,unsafe_allow_html=True)
    st.sidebar.markdown("\n")
    st.sidebar.markdown("__🛳️ Objetivos__")
    st.sidebar.markdown(SidebarText.goals,unsafe_allow_html=True)

    return None

# Define the cs_body() function
def cs_body():
    """
    Create content sections for the main body of the
     Streamlit cheat sheet with Python examples.
    """

    @st.cache_data()
    def load_data():
        # Load data from CSV file
        df_preu = pd.read_csv(DataURL.previo_universidad)
        df_u = pd.read_csv(DataURL.durante_universidad)
        malla = pd.read_csv(DataURL.malla)

        return df_preu,df_u,malla

    df_preu, df_u, malla = load_data()

    # Title of the application
    st.title("Análisis Exploratorio en una carrera de ingeniería en la V región de Chile")

    # Tab menu.
    tab1, tab2 = st.tabs(
        ["⚒️ Sobre la Carrera", "📝 Datos Matricula"]
    )


    with tab1:
        create_heatmap_malla(malla)
        st.markdown(BodyText.intro, unsafe_allow_html=True)

    with tab2:
        st.markdown(BodyText.carrera, unsafe_allow_html=True)

        st.subheader("Plots")

        # numerical variables
        plot_numeric_variables(df_preu)

        # categorical variables
        plot_categorical_variables(df_preu)













    css = '''
    <style>
        .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        font-size:1.5rem;
        }
    </style>
    '''

    st.markdown(css, unsafe_allow_html=True)





# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()