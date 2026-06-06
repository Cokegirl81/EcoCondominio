import streamlit as st

st.set_page_config(
    page_title="EcoCondomínio",
    page_icon="♻️",
    layout="wide"
)

st.sidebar.title("♻️ EcoCondomínio")

pagina = st.sidebar.radio(
    "Menu",
    [
        "Início",
        "O que reciclar",
        "Calendário",
        "Dicas",
	"Indicadores"
    ]
)

if pagina == "Início":

    st.title("♻️ EcoCondomínio")

    st.markdown("""
    ### Sustentabilidade ao alcance de todos

    O EcoCondomínio é um protótipo de aplicativo desenvolvido para incentivar
    a reciclagem em condomínios residenciais por meio da educação ambiental e
    da divulgação de informações sobre coleta seletiva.

    O projeto busca conscientizar moradores sobre a importância da separação
    correta dos resíduos e incentivar práticas sustentáveis no dia a dia.
    """)

    st.success(
        "Pequenas ações geram grandes impactos ambientais."
    )

elif pagina == "O que reciclar":

    st.title("♻️ O Que Reciclar")

    col1, col2 = st.columns(2)

    with col1:
        st.info("📄 Papel")
        st.write("""
        • Jornais  
        • Revistas  
        • Caixas de papelão
        """)

        st.info("🥤 Plástico")
        st.write("""
        • Garrafas PET  
        • Embalagens  
        • Potes
        """)

    with col2:
        st.info("🍾 Vidro")
        st.write("""
        • Garrafas  
        • Frascos
        """)

        st.info("🥫 Metal")
        st.write("""
        • Latas  
        • Tampas metálicas
        """)

elif pagina == "Calendário":

    st.title("🗑️ Calendário de Coleta")

    st.write("**Segunda:** Papel")
    st.write("**Quarta:** Plástico")
    st.write("**Sexta:** Vidro e Metal")

    st.success(
        "Consulte regularmente os dias de coleta seletiva."
    )

elif pagina == "Indicadores":

    st.title("📊 Indicadores da Pesquisa")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Moradores entrevistados",
            10
        )

    with col2:
        st.metric(
            "Conheciam reciclagem",
            "40%"
        )

    with col3:
        st.metric(
            "Consideraram o app útil",
            "90%"
        )

    st.markdown("""
    ### Resultados da Validação

    - 40% dos participantes afirmaram conhecer corretamente a separação dos resíduos.
    - 90% consideraram o aplicativo útil para incentivar a reciclagem.
    - 100% acreditam que a tecnologia pode contribuir para aumentar a conscientização ambiental.
    """)

elif pagina == "Dicas":
    st.title("🌱 Dicas Sustentáveis")

    st.markdown("""
    ✅ Reutilize embalagens

    ✅ Evite desperdício de água

    ✅ Separe corretamente os resíduos

    ✅ Prefira produtos recicláveis

    ✅ Incentive sua família a reciclar
    """)

    st.balloons()

st.divider()

st.caption(
    "Projeto desenvolvido por Marina Frigo | RU: 4492780 | Curso: Tecnologia em Ciência de Dados | UNINTER"
)