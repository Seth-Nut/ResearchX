import streamlit as st
from PIL import Image
import base64
import requests


# Initial page config
st.set_page_config(
    page_title="A Framework for Integrating Artificial General Intelligence into Engineering Education: Enhancing Human-Centric Approaches for Industry 5.0",
    layout="wide",
    initial_sidebar_state="expanded",
)


# extra classes
class SidebarText:
    introduction = """
        <small> 
        Este estudio explora la validación inicial del Marco AGI²E², 
        una guía para integrar la Inteligencia General Artificial (AGI) en la 
        educación en ingeniería. El marco busca equilibrar habilidades técnicas y centradas
          en lo humano, preparando a los estudiantes para los retos de la Industria 5.0. Se recopilaron perspectivas de expertos de la academia y la industria para evaluar su relevancia, viabilidad y aplicabilidad práctica. Los hallazgos subrayan la importancia de alinear la competencia técnica con la creatividad, el razonamiento ético y la adaptabilidad, 
        apoyados por instituciones y capacitación docente.

        </small>
        """
    goals = """
        <small>  

            Evaluar la validez del contenido del Marco AGI²E².
            - **Pregunta 1:** ¿Cómo perciben los expertos la relevancia, viabilidad y aplicabilidad del Marco AGI²E²?
            - **Pregunta 2:** ¿Qué fortalezas, debilidades y recomendaciones ofrecen los expertos para su refinamiento?
            

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
    icon = "images/icon.png"
    icon2 = "https://raw.githubusercontent.com/Seth-Nut/ResearchX/refs/heads/main/project_02/images/icon.png"


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
        """[<img src='data:image/png;base64,{}' class='img-fluid' width=450 >](https://streamlit.io/)""".format(
            img_to_bytes(
                ImagesURL.icon2
            )
        ),
        unsafe_allow_html=True,
    )

    st.sidebar.header("A Framework for Integrating Artificial General Intelligence into Engineering Education: Enhancing Human-Centric Approaches for Industry 5.0")
    st.sidebar.markdown("_Autores: Trini S. Balart y Dr. Kristi J. Shryock_")

    st.sidebar.markdown(SidebarText.introduction,unsafe_allow_html=True)
    with st.sidebar:
        # Sección de Objetivos
        with st.expander("__🎯 Objetivo__"):
            st.markdown("""
            Evaluar la validez del contenido del Marco AGI²E².
            - **Pregunta 1:** ¿Cómo perciben los expertos la relevancia, viabilidad y aplicabilidad del Marco AGI²E²?
            - **Pregunta 2:** ¿Qué fortalezas, debilidades y recomendaciones ofrecen los expertos para su refinamiento?
            """, unsafe_allow_html=True)

        # Sección de Metodología
        with st.expander("__🛠️ Metodología__"):
            st.markdown("""
            - **Diseño:** Estudio cualitativo utilizando análisis temático.
            - **Participantes:** Siete expertos en inteligencia artificial y educación en ingeniería, seleccionados mediante muestreo intencional basado en el método Delphi.
            - **Recolección de Datos:** Entrevistas semiestructuradas realizadas en persona y vía Zoom.
            - **Análisis:** Análisis temático iterativo con codificación inductiva y deductiva para identificar temas centrales y perspectivas.
            """, unsafe_allow_html=True)

        # Sección de Componentes
        with st.expander("__📚 Componentes Educativos__"):
            st.markdown("""
            1. **Uso de la IA en Educación:** Tutor personalizado y creación de experiencias de aprendizaje adaptativo.
            2. **Transformación de Roles:** Cambio hacia la mentoría, enfocándose en pensamiento crítico y creatividad.
            3. **Consideraciones Éticas:** Necesidad de políticas claras y capacitación robusta para docentes.
            4. **Modelos Educativos Futuros:** Integración de herramientas de IA preservando aspectos humanos.
            """, unsafe_allow_html=True)

        # Sección de Resultados Clave
        with st.expander("__🔑 Resultados Clave__"):
            st.markdown("""
            - **Currículo Evolutivo:** Integración de herramientas de IA preservando aspectos humanos.
            - **Adopción Exitosa:** Consideraciones éticas y apoyo institucional como elementos clave.
            - **Validación de Expertos:** Relevancia y viabilidad destacadas para la Industria 5.0.
            - **Investigaciones Futuras:** Incorporación de diversos actores y pruebas empíricas.
            """, unsafe_allow_html=True)

        # Sección de Referencias
        with st.expander("__🔗 Referencias__"):
            st.markdown("""
            **Trini S. Balart, Kristi J. Shryock.**  
            *A Framework for Integrating Artificial General Intelligence into Engineering Education: Enhancing Human-Centric Approaches for Industry 5.0.*  
            TechRxiv, junio de 2024.  
            **Contacto:** Trini Balart, tsbalart@tamu.edu
            """, unsafe_allow_html=True)

    return None

# Define the cs_body() function
def cs_body():
    """
    Create content sections for the main body of the
     Streamlit cheat sheet with Python examples.
    """

    # Título de la aplicación
    st.title("Marco AGI²E²")

    # Menú de pestañas
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🌐 Skill 01",
        "🎯 Skill 02",
        "🔄 Skill 03",
        "💡 Skill 04",
        "⚖️ Skill 05",
    ])

    # Contenido para la primera pestaña
    with tab1:
        st.header("Entornos de Aprendizaje Interdisciplinarios")
        st.markdown("""
        La integración de la AGI permite crear entornos dinámicos e interdisciplinarios, destacando:
        - **Conexión de disciplinas:** Uso de la IA para unir áreas como ingeniería, humanidades, ciencias sociales y estudios éticos, promoviendo una comprensión holística.
        - **Aprendizaje interactivo:** Implementación de simulaciones y herramientas interactivas que permiten a los estudiantes experimentar con problemas del mundo real.
        - **Proyectos colaborativos:** Diseñar actividades donde equipos multidisciplinarios trabajen en soluciones para retos globales como el cambio climático o la inclusión digital.
        - **Casos prácticos:** Incorporación de proyectos de empresas reales en el currículo, permitiendo que los estudiantes apliquen sus conocimientos de manera práctica.
        """)
        st.info("💡 La interdisciplinariedad fomenta no solo habilidades técnicas, sino también empatía y entendimiento cultural.")

    # Contenido para la segunda pestaña
    with tab2:
        st.header("Trayectorias Educativas Personalizadas")
        st.markdown("""
        Las trayectorias personalizadas se logran mediante el uso de algoritmos de IA que:
        - **Análisis predictivo:** Identifican patrones de aprendizaje para anticipar necesidades futuras.
        - **Rutas personalizadas:** Diseñan programas de estudio únicos adaptados a los intereses y habilidades individuales de los estudiantes.
        - **Herramientas de autoevaluación:** Los estudiantes pueden medir su progreso y ajustar su plan de estudio de forma dinámica.
        - **Soporte en tiempo real:** Chatbots y asistentes virtuales proporcionan ayuda inmediata en tareas complejas.
        """)
        st.warning("⚠️ Evitar que las trayectorias personalizadas limiten la exploración de los estudiantes.")


    # Contenido para la tercera pestaña
    with tab3:
        st.header("Adaptación Continua y Aprendizaje Permanente")
        st.markdown("""
        El marco AGI²E² fomenta la adaptabilidad continua al:
        - **Identificación de habilidades emergentes:** Uso de análisis de datos para ajustar rápidamente el currículo a las demandas del mercado laboral.
        - **Currículo flexible:** Integración de casos de estudio y proyectos basados en problemas actuales de la industria.
        - **Colaboración industrial:** Creación de asociaciones con empresas para proporcionar mentorías, pasantías y oportunidades de investigación aplicada.
        - **Plataformas de aprendizaje continuo:** Acceso a contenidos actualizados y certificados profesionales para mantenerse competitivo.
        """)
        st.success("✅ Aprender a aprender es una de las habilidades más importantes para prosperar en un mercado laboral en constante cambio.")

    # Contenido para la cuarta pestaña
    with tab4:
        st.header("Desarrollo de Habilidades del Siglo XXI")
        st.markdown("""
        Este marco prioriza el desarrollo de habilidades como:
        - **Pensamiento crítico:** Desafíos que requieren evaluación lógica y resolución de problemas complejos.
        - **Creatividad:** Uso de herramientas digitales para fomentar la innovación en proyectos colaborativos.
        - **Comunicación:** Mejora de habilidades orales y escritas mediante simulaciones de reuniones y presentaciones.
        - **Liderazgo ético:** Toma de decisiones informadas considerando factores sociales, económicos y medioambientales.
        """)
        st.info("💬 La combinación de habilidades técnicas y blandas prepara a los estudiantes para liderar en el siglo XXI.")

    # Contenido para la quinta pestaña
    with tab5:
        st.header("Consideraciones Éticas")
        st.markdown("""
        La integración de AGI en la educación debe abordar:
        - **Privacidad:** Implementar sistemas seguros que respeten la privacidad de los estudiantes y protejan sus datos personales.
        - **Equidad:** Diseñar algoritmos que eviten sesgos y promuevan la inclusión.
        - **Transparencia:** Desarrollar herramientas que expliquen cómo se toman decisiones algorítmicas.
        - **Rol del educador:** Potenciar la figura del docente como guía y mentor, complementando, no reemplazando, su rol.
        - **Currículo ético:** Incluir módulos educativos sobre ética en la tecnología y responsabilidad social.
        """)
        st.warning("🔍 Reflexiona: ¿Qué acciones concretas podemos tomar hoy para asegurar el uso ético de la AGI en la educación?")
    



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