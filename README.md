# 📚 Literar.IA

Literar.IA es un generador de cuentos basado en IA que combina estilos literarios de autores latinoamericanos y universales. Utilizando la API de Anthropic (Claude), el proyecto permite crear historias originales mezclando diferentes perspectivas narrativas, estilos literarios y elementos técnicos de la narrativa.

## 🌟 Características

### Estilos Literarios
- **Autores Incluidos**: 
  - Julio Cortázar
  - Alejandra Pizarnik
  - Gabriel García Márquez
  - Juan Rulfo
  - Isabel Allende
  - Laura Esquivel
  - Alejo Carpentier
  - Charles Bukowski
  - Richard Yates
  - Tobias Wolff
  - Jayne Anne Phillips

### Elementos Narrativos
- **Perspectivas Narrativas**:
  - Primera persona (yo protagonista, yo testigo)
  - Segunda persona
  - Tercera persona (omnisciente, limitado, objetivo)

- **Tipos de Narrador**:
  - Omnisciente
  - Limitado
  - Objetivo
  - No fiable
  - Multiple

### Elementos Técnicos
- **Atmósfera**: Onírica, Opresiva, Nostálgica, Misteriosa, Cotidiana, Surreal
- **Tiempo Narrativo**: Lineal, No lineal, Circular, Fragmentado, Simultáneo
- **Estilos de Diálogo**: Directo, Indirecto, Indirecto libre, Monólogo interior, Flujo de consciencia

### Géneros Literarios
- Realismo mágico
- Literatura urbana
- Novela psicológica
- Realismo sucio
- Real maravilloso
- Narrativa experimental

## 🛠️ Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/holasoymalva/literar.ia.git
cd literar.ia
```

2. Crea un entorno virtual e instala las dependencias:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Configura las variables de entorno:
   - Crea un archivo `.streamlit/secrets.toml`
   - Añade tu API key de Anthropic:
```toml
ANTHROPIC_API_KEY = "tu-api-key"
```

## 🚀 Uso

1. Inicia la aplicación:
```bash
streamlit run app.py
```

2. Accede a la interfaz web en tu navegador (por defecto en `http://localhost:8501`)

3. En la interfaz principal:
   - Selecciona el género literario
   - Elige un tema
   - Configura la perspectiva narrativa y tipo de narrador
   - Ajusta los elementos de la historia
   - Selecciona hasta tres autores de influencia
   - Especifica la longitud deseada
   - Añade notas adicionales si lo deseas

4. Utiliza la pestaña de "Herramientas Creativas" para:
   - Generar esquemas de historias
   - Explorar diferentes combinaciones de temas y géneros

## 📋 Requisitos

- Python 3.8+
- Streamlit
- Anthropic API Key
- Dependencias listadas en `requirements.txt`

## 📝 Archivo requirements.txt

```txt
streamlit==1.31.0
anthropic==0.8.1
python-dotenv==1.0.0
```

## 🤝 Contribución

Las contribuciones son bienvenidas. Por favor, sigue estos pasos:

1. Fork el proyecto
2. Crea una rama para tu característica (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add: AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE.md](LICENSE.md) para más detalles.

## 🙏 Agradecimientos

- Anthropic por proporcionar la API de Claude
- A todos los autores que inspiran este proyecto
- La comunidad de desarrollo de Streamlit

## 📞 Contacto

Project Link: [https://github.com/holasoymalva/literar.ia](https://github.com/holasoymalva/literar.ia)
