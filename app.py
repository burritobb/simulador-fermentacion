import streamlit as st
import random

# Configuración de la página con estilo oscuro/gótico sutil
st.set_page_config(page_title="Simulador de Fermentación Vinícola", layout="centered")

# Inyección de CSS para personalizar la estética del juego
st.markdown("""
    <style>
    .main { background-color: #1a1a24; color: #e0e0e0; }
    h1, h2, h3 { color: #ff79c6; text-align: center; font-family: 'Courier New', Courier, monospace; }
    .stButton>button { 
        background-color: #6272a4; color: white; border-radius: 8px; 
        width: 100%; font-weight: bold; border: 1px solid #ff79c6;
    }
    .stButton>button:hover { background-color: #ff79c6; color: #1a1a24; }
    .status-box { 
        padding: 15px; border-radius: 10px; background-color: #282a36; 
        border-left: 5px solid #ff79c6; margin-bottom: 15px;
    }
    .dialogue-box {
        background-color: #21222c; padding: 12px; border-radius: 8px;
        border: 1px dashed #bd93f9; margin-top: 10px; font-style: italic;
    }
    </style>
""", unsafe_allow_html=True)

# --- BASE DE DATOS DE PERSONAJES (Descripciones para que la IA del sitio los renderice) ---
PERSONAJES = {
    "femboy_bartender": {
        "nombre": "Milo (Bartender Principal)",
        "desc": "Chico pixel estilo femboy, tez blanca, mejillas rosadas, cabello blanco, orejas blancas de conejo (humano con orejas, no furro), ojos rosados brillantes. Viste chaleco de bartender elegante."
    },
    "leopardo_rudo": {
        "nombre": "Kaelen (Supervisor de Bodega)",
        "desc": "Chico musculoso, apariencia ruda/gótica, tez morena, ojos dorados intensos, cicatrices en el rostro. Híbrido de leopardo de las nieves (orejas grises con manchas negras y cola larga esponjosa, cuerpo humano, no furro). Silencioso como una bestia controlada."
    }
}

# Inicializar estados globales del juego si no existen
if 'paso' not in st.session_state: st.session_state.paso = 0
if 'promedio' not in st.session_state: st.session_state.promedio = 80
if 'vino_calidad' not in st.session_state: st.session_state.vino_calidad = 100

st.title("🍇 Simulador de Éxito Biotecnológico: El Arte del Vino 🍷")
st.write("---")

# --- INTRODUCCIÓN Y PRESENTACIÓN DE PERSONAJES ---
if st.session_state.paso == 0:
    st.header("Bienvenidos a la Bodega Ancestral")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🐰 " + PERSONAJES["femboy_bartender"]["nombre"])
        st.markdown(f"<div class='status-box'>{PERSONAJES['femboy_bartender']['desc']}</div>", unsafe_allow_html=True)
    with col2:
        st.subheader("🐆 " + PERSONAJES["leopardo_rudo"]["nombre"])
        st.markdown(f"<div class='status-box'>{PERSONAJES['leopardo_rudo']['desc']}</div>", unsafe_allow_html=True)
        
    st.markdown("<div class='dialogue-box'><b>Milo:</b> ¡Hola! Bienvenido. Te enseñaré a transformar la glucosa en el elixir perfecto mediante fermentación anaeróbica. ¡Kaelen vigilará que no arruines los tanques!</div>", unsafe_allow_html=True)
    st.markdown("<div class='dialogue-box'><b>Kaelen:</b> ... No mueras en el intento. La temperatura es traicionera.</div>", unsafe_allow_html=True)
    
    if st.button("Comenzar la Producción"):
        st.session_state.paso = 1
        st.rerun()

# --- MINIJUEGO 1: RECOLECTA Y DESPALILLADO ---
elif st.session_state.paso == 1:
    st.header("Fase 1: El Despalillado y Mosto")
    st.write("Debemos separar las uvas de los raspones (ramas) para liberar el jugo.")
    
    opcion = st.radio("¿Cómo decides presionar y limpiar las uvas?", 
                      ["Ritmo rápido y constante (Cuidado óptimo)", "Presión brusca y descuidada"])
    
    st.markdown("<div class='dialogue-box'><b>Milo:</b> ¡El mosto es el jugo que contiene glucosa y fructosa, el alimento de nuestras levaduras!</div>", unsafe_allow_html=True)
    
    if st.button("Siguiente Paso"):
        if opcion == "Ritmo rápido y constante (Cuidado óptimo)":
            st.session_state.vino_calidad += 10
            st.success("¡Excelente mosto liberado!")
        else:
            st.session_state.vino_calidad -= 15
            st.error("Rompiste demasiadas ramas, el mosto quedó amargo.")
        st.session_state.paso = 2
        st.rerun()

# --- MINIJUEGO 2: ALIMENTACIÓN DE LEVADURAS ---
elif st.session_state.paso == 2:
    st.header("Fase 2: El Banquete de las Levaduras")
    st.write("En plena ausencia de aire, las levaduras deben consumir la glucosa para transformarla en etanol.")
    
    eficiencia = st.slider("Regula la tasa de absorción de glucosa por las levaduras (%)", 0, 100, 50)
    
    st.markdown("<div class='dialogue-box'><b>Milo:</b> En condiciones anaeróbicas, la levadura descompone el azúcar produciendo alcohol y CO2 como desecho.</div>", unsafe_allow_html=True)
    
    if st.button("Confirmar Tasa de Absorción"):
        if 70 <= eficiencia <= 90:
            st.session_state.vino_calidad += 15
            st.success("¡Glucólisis perfecta! Las levaduras trabajan a ritmo óptimo.")
        else:
            st.session_state.vino_calidad -= 20
            st.warning("Eficiencia inestable. Producción de ATP y etanol deficiente.")
        st.session_state.paso = 3
        st.rerun()

# --- MINIJUEGO 3: CONTROL DE TEMPERATURA ---
elif st.session_state.paso == 3:
    st.header("Fase 3: Control de Temperatura Crítica")
    st.write("La fermentación es un proceso exotérmico (libera calor). ¡Monitorea el tanque!")
    
    temp = st.slider("Ajusta la temperatura del tanque de fermentación (°C)", 15, 40, 25)
    
    st.markdown("<div class='dialogue-box'><b>Kaelen:</b> (Te gruñe sutilmente) Mantén la aguja abajo... Si la temperatura supera los 30°C, las levaduras morirán. Si acumulas CO2, el tanque estallará.</div>", unsafe_allow_html=True)
    
    if st.button("Verificar Tanque"):
        if temp > 30:
            st.session_state.vino_calidad -= 40
            st.error("¡Desastre! Las levaduras murieron por exceso de calor.")
        elif temp < 20:
            st.session_state.vino_calidad -= 15
            st.warning("La fermentación se ralentizó demasiado.")
        else:
            st.session_state.vino_calidad += 15
            st.success("Temperatura ideal. El burbujeo de CO2 es estable.")
        st.session_state.paso = 4
        st.rerun()

# --- MINIJUEGO 4: EMBOTELLADO Y SELLADO ---
elif st.session_state.paso == 4:
    st.header("Fase 4: El Embotellado y Control de Oxígeno")
    st.write("Es hora de colocar los corchos. El sellado al vacío es crucial.")
    
    sellado = st.selectbox("¿Cuánto espacio vacío dejarás en la botella?", 
                           ["Espacio mínimo (Sellado al vacío perfecto)", "Espacio considerable (Entrada de aire)"])
    
    st.markdown("<div class='dialogue-box'><b>Milo:</b> ¡Cuidado! Si entra oxígeno, se activan las bacterias Acetobacter y convertirán nuestro hermoso etanol en ácido acético (vinagre).</div>", unsafe_allow_html=True)
    
    if st.button("Terminar Producción"):
        if sellado == "Espacio mínimo (Sellado al vacío perfecto)":
            st.session_state.vino_calidad += 10
        else:
            st.session_state.vino_calidad -= 50
        st.session_state.paso = 5
        st.rerun()

# --- RESULTADO FINAL ---
elif st.session_state.paso == 5:
    st.header("=== EVALUACIÓN DE LA PRODUCCIÓN ===")
    
    st.metric(label="Calidad Final del Vino", value=f"{st.session_state.vino_calidad} / 150")
    
    if st.session_state.vino_calidad >= 120:
        st.balloons()
        st.success("¡ÉXITO TOTAL! Han creado un vino premium de alta escuela biotecnológica.")
        st.markdown("<div class='dialogue-box'><b>Milo:</b> ¡Increíble! Eres un maestro de la biotecnología. ¡Sirvamos esto en la barra!<br><b>Kaelen:</b> (Sonríe de medio lado) Buen trabajo... No rompiste nada. Tienes mis respetos.</div>", unsafe_allow_html=True)
    elif st.session_state.vino_calidad >= 70:
        st.warning("Buen camino, pero el vino tiene detalles estables que pueden mejorar.")
        st.markdown("<div class='dialogue-box'><b>Milo:</b> No está mal, pero podemos ajustar mejor los niveles para la próxima.<br><b>Kaelen:</b> Pasable. Al menos no es vinagre.</div>", unsafe_allow_html=True)
    else:
        st.error("Resultado deficiente. El producto final no es apto para la venta.")
        st.markdown("<div class='dialogue-box'><b>Milo:</b> Oh no... las bacterias o el calor nos ganaron.<br><b>Kaelen:</b> (Cruza los brazos, decepcionado) Te lo advertí. A limpiar los tanques y empezar de nuevo.</div>", unsafe_allow_html=True)
        
    if st.button("Reiniciar Simulador"):
        st.session_state.paso = 0
        st.session_state.vino_calidad = 100
        st.rerun()
