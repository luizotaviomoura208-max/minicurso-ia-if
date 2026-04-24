import streamlit as st
 
st.set_page_config(page_title="Calculadora de Notas - IF", page_icon="🎓")
st.title("🎓 Calculadora de Notas do IF")
 
n1, n2 = st.number_input("Nota 1", 0.0, 10.0, step=0.1), st.number_input("Nota 2", 0.0, 10.0, step=0.1)
 
if st.button("Calcular Média", use_container_width=True):
    media = round((n1 + n2) / 2, 2)
    status = ("✅ Aprovado!", "success") if media >= 6 else ("❌ Reprovado.", "error")
    st.metric("Média Final", media)
    getattr(st, status[1])(status[0])
