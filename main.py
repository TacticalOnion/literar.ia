# app.py
import streamlit as st
from anthropic import Anthropic

class LiteraryAgent:
    def __init__(self):
        self.anthropic = Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])
        
        # Elementos literarios predefinidos
        self.styles = {
            "Cortázar": "narrativa no lineal, realismo mágico, juegos con el tiempo",
            "Pizarnik": "poético, oscuro, introspectivo",
            "Bukowski": "crudo, directo, realista"
        }
        
        self.themes = [
            "La soledad en la ciudad",
            "Encuentros inesperados",
            "Realidades paralelas",
            "Memoria y tiempo",
            "Sueños y realidad",
            "El absurdo cotidiano"
        ]

    def get_story_prompt(self, theme, style_mix, length, additional_notes):
        return f"""
        Genera un cuento original que combine los siguientes elementos:
        
        Tema principal: {theme}
        Estilos literarios a combinar: {style_mix}
        Longitud aproximada: {length} palabras
        
        Notas adicionales: {additional_notes}
        
        El cuento debe ser completamente original mientras mantiene elementos 
        estilísticos de Cortázar, Pizarnik y Bukowski, específicamente en:
        - La estructura narrativa experimental de Cortázar
        - El lenguaje poético y metafórico de Pizarnik
        - La crudeza y honestidad de Bukowski
        
        Por favor, genera una historia original que integre estos elementos.
        """

    def generate_story(self, prompt):
        try:
            response = self.anthropic.messages.create(
                model="claude-3-haiku-20240307",
                max_tokens=1000,
                temperature=0.9,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return response.content[0].text
        except Exception as e:
            return f"Error en la generación: {str(e)}"

def main():
    st.set_page_config(page_title="Agente Escritor Literario", page_icon="📚")
    
    st.title("📚 Generador de Cuentos Literarios")
    st.write("Inspirado en Cortázar, Pizarnik y Bukowski")
    
    # Inicializar el agente
    agent = LiteraryAgent()
    
    # Interfaz de usuario
    with st.form("story_generator"):
        # Selección de tema
        theme = st.selectbox(
            "Selecciona un tema",
            agent.themes
        )
        
        # Mezcla de estilos
        st.write("Influencia de estilos")
        cortazar_influence = st.slider("Cortázar", 0, 100, 33)
        pizarnik_influence = st.slider("Pizarnik", 0, 100, 33)
        bukowski_influence = st.slider("Bukowski", 0, 100, 34)
        
        # Longitud
        length = st.select_slider(
            "Longitud aproximada",
            options=[500, 1000, 1500, 2000],
            value=1000
        )
        
        # Notas adicionales
        additional_notes = st.text_area(
            "Notas adicionales",
            "Agrega cualquier elemento específico que desees incluir..."
        )
        
        submitted = st.form_submit_button("Generar Cuento")
        
    if submitted:
        # Crear mezcla de estilos basada en los porcentajes
        style_mix = f"""
        Cortázar ({cortazar_influence}%): {agent.styles['Cortázar']}
        Pizarnik ({pizarnik_influence}%): {agent.styles['Pizarnik']}
        Bukowski ({bukowski_influence}%): {agent.styles['Bukowski']}
        """
        
        with st.spinner("Generando historia..."):
            # Generar el prompt y la historia
            prompt = agent.get_story_prompt(theme, style_mix, length, additional_notes)
            story = agent.generate_story(prompt)
            
            # Mostrar la historia
            st.markdown("### Tu Historia")
            st.markdown(story)
            
            # Botón para descargar
            st.download_button(
                "Descargar historia",
                story,
                file_name="historia_generada.txt",
                mime="text/plain"
            )

if __name__ == "__main__":
    main()