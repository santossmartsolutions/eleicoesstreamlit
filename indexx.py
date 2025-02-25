import streamlit as st

def main():
    st.title("Sistema de Votação")
    st.write("Bem-vindo ao Sistema de Votos!")
    st.write("Sua voz é o nosso futuro.")

    # Inicializa o estado da sessão
    if "votos" not in st.session_state:
        st.session_state.votos = {
            1: 0,  # Juscelino KubitscheK
            2: 0,  # Itamar Franco
            3: 0   # Afonso Pena
        }

    # Inicialização do sistema
    if st.button("CONTINUAR"):
        st.session_state.iniciado = True

    if st.session_state.get("iniciado", False):
        st.write("Sistema de Votação inicializado!")

        # Seleção de candidato
        opcao = st.selectbox(
            "Selecione o número do candidato:",
            options=["1 - Juscelino KubitscheK", "2 - Itamar Franco", "3 - Afonso Pena", "0 - Sair e ver resultados"]
        )

        # Extrai o número da opção selecionada
        voto = int(opcao.split(" ")[0])

        if voto == 0:
            st.write("\nResultado da votação:")
            for candidato, quantidade in st.session_state.votos.items():
                st.write(f"Candidato {candidato}: {quantidade} votos")
        elif voto in st.session_state.votos:
            st.session_state.votos[voto] += 1
            st.success("Voto registrado com sucesso!")
        else:
            st.error("Candidato inválido.")

# Executa o aplicativo
if __name__ == "__main__":
    main()  