ef show_team_page():
    st.title("👥 Anggota Tim")
    st.markdown("---")
    
    col1, col2, col3, col4 = st.columns(4)

    # Anggota 1
    with col1:
        st.subheader("Nama Anggota 1")
        st.image("https://i.ibb.co.com/sdPCM2q/anggota1.png", caption="Foto Anggota 1", width=150)
        st.write("**Peran:** Project Manager & Developer")
        st.write("**Kontribusi:** Backend development, deployment")

    # Anggota 2
    with col2:
        st.subheader("Nama Anggota 2")
        st.image("https://i.ibb.co.com/XrzfGXz/anggota2.png", caption="Foto Anggota 2", width=150)
        st.write("**Peran:** Data Analyst")
        st.write("**Kontribusi:** Preprocessing data, visualisasi")

    # Anggota 3
    with col3:
        st.subheader("Nama Anggota 3")
        st.image("https://i.ibb.co.com/fzmpC1Xg/anggota3.png", caption="Foto Anggota 3", width=150)
        st.write("**Peran:** Matematika & Algoritma")
        st.write("**Kontribusi:** Mathematical modeling, optimization")

    # Anggota 4
    with col4:
        st.subheader("Nama Anggota 4")
        st.image("https://i.ibb.co.com/NdB1CJF/anggota4.png", caption="Foto Anggota 4", width=150)
        st.write("**Peran:** Frontend Developer")
        st.write("**Kontribusi:** UI/UX & layout Streamlit")
