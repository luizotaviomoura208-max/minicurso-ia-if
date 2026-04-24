import streamlit as st
import pandas as pd

st.set_page_config(page_title="Calculadora de Notas - IF", page_icon="🎓", layout="centered")
st.title("🎓 Calculadora de Notas do IF")

if "historico" not in st.session_state:
    st.session_state.historico = []

qtd = st.radio("Quantas notas?", [2, 3, 4], horizontal=True)
cols = st.columns(qtd)
notas = [cols[i].number_input(f"Nota {i+1}", 0.0, 10.0, step=0.1) for i in range(qtd)]

if st.button("Calcular Média", use_container_width=True):
    media = round(sum(notas) / qtd, 2)
    aprovado = media >= 6.0

    c1, c2, c3 = st.columns(3)
    c1.metric("Média Final", media)
    c2.metric("Situação", "✅ Aprovado" if aprovado else "❌ Reprovado")
    c3.metric("Falta para aprovação", 0 if aprovado else round(6.0 - media, 2))

    getattr(st, "success" if aprovado else "error")("Aprovado! Parabéns! 🎉" if aprovado else f"Faltam {round(6.0 - media, 2)} pontos para aprovação.")

    df_notas = pd.DataFrame({"Nota": [f"N{i+1}" for i in range(qtd)], "Valor": notas})
    st.bar_chart(df_notas.set_index("Nota"))
    st.markdown("<small>📏 Linha de corte: <b>6.0</b></small>", unsafe_allow_html=True)

    st.session_state.historico.append({"Notas": notas, "Média": media, "Situação": "✅ Aprovado" if aprovado else "❌ Reprovado"})

if st.session_state.historico:
    st.divider()
    st.subheader("📋 Histórico da Sessão")
    st.dataframe(pd.DataFrame(st.session_state.historico), use_container_width=True)
    if st.button("🗑️ Limpar Histórico"):
        st.session_state.historico = []
        st.rerun()
