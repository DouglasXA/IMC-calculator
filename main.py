import streamlit as st


def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc


def classificar_imc(imc):
    if imc < 15.0:
        return "Abaixo do ideal"
    elif imc >= 15.0 and imc <= 25.0:
        return "Ideal"
    else:
        return "Muito acima do ideal"


def main():
    st.title("Calculadora de IMC")

    name = st.text_input("Digite o nome do usuário:")
    peso = st.number_input("Digite o peso do usuário (kg):")
    altura = st.number_input("Digite a altura do usuário (m):")

    if st.button("Calcular"):
        imc = calcular_imc(peso, altura)
        st.write(f"O IMC do usuário {name} é: {imc:.2f}")
        classificacao = classificar_imc(imc)
        st.write(f"Classificação: {classificacao}")


if __name__ == "__main__":
    main()