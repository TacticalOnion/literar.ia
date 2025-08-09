# app.py
import streamlit as st
import requests

class EnhancedLiteraryAgent:
    def __init__(self):
        base = st.secrets.get("OLLAMA_BASE_URL", "http://localhost:11434")
        self.ollama_url = f"{base}/api/generate"
        self.ollama_model = st.secrets.get("OLLAMA_MODEL", "llama3.1:8b-instruct-q4_1")
        self.system_prompt = st.secrets.get("OLLAMA_SYSTEM", "")
        self.safe_preamble = st.secrets.get("OLLAMA_PREAMBLE", "")

        # Elementos literarios predefinidos
        self.styles = {
            "Cortázar": "narrativa no lineal, realismo mágico, juegos con el tiempo",
            "Pizarnik": "poético, oscuro, introspectivo",
            "García Márquez": "realismo mágico, narrativa circular, memoria colectiva",
            "Rulfo": "realismo rural, voces espectrales, tiempo fragmentado",
            "Allende": "realismo mágico, perspectiva femenina, saga familiar",
            "Esquivel": "realismo mágico culinario, romance, tradición",
            "Carpentier": "real maravilloso, barroquismo, historia",
            "Bukowski": "realismo sucio, cotidianidad cruda, antimaterialismo",
            "Yates": "realismo psicológico, desesperanza suburbana, introspección",
            "Wolff": "realismo minimalista, memoria personal, relaciones familiares",
            "Phillips": "realismo psicológico, voces marginales, intimismo"
        }
        
        self.themes = [
            "La soledad en la ciudad",
            "Encuentros inesperados",
            "Realidades paralelas",
            "Memoria y tiempo",
            "Sueños y realidad",
            "El absurdo cotidiano",
            "Conflictos familiares",
            "La búsqueda de identidad",
            "El peso de la historia",
            "La transformación personal",
            "La vida en los márgenes",
            "El desarraigo urbano"
        ]
        
        # Géneros literarios
        self.genres = [
            "Realismo mágico",
            "Literatura urbana",
            "Novela psicológica",
            "Realismo sucio",
            "Real maravilloso",
            "Narrativa experimental"
        ]

    def get_story_prompt(self, theme, genre, style_mix, length, additional_notes):
        return f"""
        {self.safe_preamble}
        Genera un cuento original que combine los siguientes elementos:
        
        Tema principal: {theme}
        Género literario: {genre}
        Estilos literarios a combinar: {style_mix}
        Longitud aproximada: {length} palabras
        
        Notas adicionales: {additional_notes}
        
        El cuento debe ser completamente original mientras integra elementos 
        estilísticos de los autores seleccionados, considerando:
        - La construcción del mundo narrativo
        - El manejo del tiempo y la estructura
        - El tono y la voz narrativa
        - El tratamiento de los personajes
        - La atmósfera y el ambiente
        
        La historia debe mantener coherencia con el género seleccionado 
        mientras incorpora los elementos estilísticos de los autores.
        """

    def generate_story(self, prompt):
        try:
            payload = {
                "model": self.ollama_model,
                "prompt": prompt,
                "stream": False,
                "system": self.system_prompt,
                "options": {
                    "temperature": 0.9,
                    "num_predict": 2000
                }
            }
            response = requests.post(self.ollama_url, json=payload, timeout=120)
            response.raise_for_status()
            data = response.json()
            return data.get("response", "No se pudo generar la historia.")
        except Exception as e:
            return f"Error en la generación: {str(e)}"

def main():
    st.set_page_config(page_title="Agente Escritor Literario Avanzado", page_icon="📚")
    
    st.title("📚 Generador de Cuentos Literarios")
    st.write("Una fusión de estilos literarios latinoamericanos y universales")
    
    # Inicializar el agente
    agent = EnhancedLiteraryAgent()
    
    # Interfaz de usuario mejorada
    with st.form("story_generator"):
        # Selección de género
        genre = st.selectbox(
            "Selecciona un género literario",
            agent.genres
        )
        
        # Selección de tema
        theme = st.selectbox(
            "Selecciona un tema",
            agent.themes
        )
        
        # Selección de autores y sus influencias
        st.write("### Influencia de autores")
        st.write("Selecciona hasta tres autores y ajusta sus niveles de influencia")
        
        # Permitir selección de autores
        available_authors = list(agent.styles.keys())
        selected_authors = st.multiselect(
            "Selecciona los autores (máximo 3)",
            available_authors,
            max_selections=3
        )
        
        # Sliders dinámicos para los autores seleccionados
        author_influences = {}
        if selected_authors:
            remaining_percentage = 100
            for i, author in enumerate(selected_authors[:-1]):  # Todos menos el último
                max_value = remaining_percentage if i == len(selected_authors)-2 else 100
                influence = st.slider(
                    f"Influencia de {author}",
                    0,
                    max_value,
                    min(33, max_value)
                )
                author_influences[author] = influence
                remaining_percentage -= influence
            
            # El último autor toma el porcentaje restante
            if selected_authors:
                last_author = selected_authors[-1]
                author_influences[last_author] = remaining_percentage
                st.write(f"Influencia de {last_author}: {remaining_percentage}%")
        
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
        if not selected_authors:
            st.error("Por favor, selecciona al menos un autor.")
            return
            
        # Crear mezcla de estilos basada en los autores seleccionados
        style_mix = "\n".join([
            f"{author} ({influence}%): {agent.styles[author]}"
            for author, influence in author_influences.items()
        ])
        
        with st.spinner("Generando historia..."):
            # Generar el prompt y la historia
            prompt = agent.get_story_prompt(theme, genre, style_mix, length, additional_notes)
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