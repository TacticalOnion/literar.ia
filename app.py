import streamlit as st
from anthropic import Anthropic
import json
import random
from datetime import datetime

class LiteraryAgent:
    def __init__(self):
        self.anthropic = Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])
        
        # Elementos narrativos base
        self.narrative_elements = {
            "temas": ["soledad", "alienación", "realidad fragmentada", "tiempo no lineal", 
                     "memoria", "sueños", "ciudad", "relaciones humanas"],
            "tonos": ["introspectivo", "surrealista", "crudo", "poético", 
                     "existencial", "absurdo", "melancólico"],
            "estructuras": ["fragmentada", "circular", "stream of consciousness", 
                          "realismo mágico", "narración no lineal"]
        }
        
        # Inicializar historial de cuentos
        if "stories" not in st.session_state:
            st.session_state.stories = []

    def generate_prompt(self, theme, tone, structure, additional_instructions):
        """Genera el prompt para Claude"""
        base_prompt = f"""
        Crea un cuento original con las siguientes características:
        - Tema principal: {theme}
        - Tono narrativo: {tone}
        - Estructura narrativa: {structure}
        
        Instrucciones adicionales del usuario:
        {additional_instructions}
        
        Consideraciones estilísticas:
        - Usa elementos de realismo mágico y cotidianidad
        - Incorpora metáforas y símbolos potentes
        - Mantén un balance entre lo lírico y lo narrativo
        - Explora la psicología de los personajes
        - Usa descripciones vívidas y precisas
        
        Genera un cuento completamente original que refleje estas características.
        """
        return base_prompt

    def generate_story(self, prompt):
        """Genera un cuento usando la API de Claude"""
        try:
            message = self.anthropic.messages.create(
                model="claude-3-opus-20240229",
                max_tokens=2000,
                temperature=0.9,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )
            return message.content[0].text
        except Exception as e:
            return f"Error en la generación: {str(e)}"

    def display_interface(self):
        """Muestra la interfaz de usuario"""
        st.title("🖋️ Agente Escritor Literario")
        
        # Sidebar para configuración y opciones
        with st.sidebar:
            st.header("Elementos Narrativos")
            
            theme = st.selectbox(
                "Tema Principal",
                self.narrative_elements["temas"]
            )
            
            tone = st.selectbox(
                "Tono Narrativo",
                self.narrative_elements["tonos"]
            )
            
            structure = st.selectbox(
                "Estructura Narrativa",
                self.narrative_elements["estructuras"]
            )
            
            st.markdown("---")
            st.markdown("""
            ### Acerca del Agente
            Este agente literario genera cuentos originales
            inspirados en estilos narrativos contemporáneos.
            """)

        # Área principal
        st.markdown("### Generador de Cuentos")
        
        additional_instructions = st.text_area(
            "Instrucciones Adicionales",
            "Escribe aquí elementos específicos que desees incluir en el cuento..."
        )
        
        if st.button("Generar Cuento"):
            with st.spinner("Creando historia..."):
                prompt = self.generate_prompt(
                    theme, tone, structure, additional_instructions
                )
                story = self.generate_story(prompt)
                
                # Guardar la historia
                st.session_state.stories.append({
                    "fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "tema": theme,
                    "tono": tone,
                    "estructura": structure,
                    "contenido": story
                })
                
                # Mostrar la historia
                st.markdown("### Historia Generada")
                st.markdown(story)
                
                # Opciones de exportación
                if st.button("Exportar como TXT"):
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    filename = f"cuento_{timestamp}.txt"
                    with open(filename, "w", encoding="utf-8") as f:
                        f.write(story)
                    st.success(f"Historia guardada como {filename}")

        # Historial de cuentos
        if st.session_state.stories:
            st.markdown("### Historial de Cuentos")
            for idx, story in enumerate(st.session_state.stories):
                with st.expander(f"Cuento {idx + 1} - {story['fecha']}"):
                    st.markdown(f"**Tema:** {story['tema']}")
                    st.markdown(f"**Tono:** {story['tono']}")
                    st.markdown(f"**Estructura:** {story['estructura']}")
                    st.markdown("---")
                    st.markdown(story['contenido'])

def main():
    st.set_page_config(
        page_title="Agente Escritor Literario",
        page_icon="🖋️",
        layout="wide"
    )
    
    if "ANTHROPIC_API_KEY" not in st.secrets:
        st.error("""
        ⚠️ Configura tu clave API de Anthropic en .streamlit/secrets.toml:
        ANTHROPIC_API_KEY = "tu-clave-api"
        """)
        return
    
    agent = LiteraryAgent()
    agent.display_interface()

if __name__ == "__main__":
    main()