#  PyVolt — Simulador de Circuitos Elétricos CC

O **PyVolt** é um simulador e laboratório virtual de circuitos elétricos de corrente contínua (CC) focado em circuitos RC (Resistor-Capacitor). O projeto foi desenvolvido como **Trabalho Final da disciplina de Computação II**.

O aplicativo utiliza conceitos de **Programação Orientada a Objetos (POO)** em Python para calcular a física do circuito e oferece uma interface interativa via **Streamlit** para comparar o comportamento do circuito manual com dispositivos do mundo real.

---

##  Funcionalidades

- **Cálculos Físicos em Tempo Real:**
  - Resistência Equivalente ($R_{eq}$) em série e paralelo.
  - Corrente Elétrica Total ($I$) pela Lei de Ohm.
  - Potência Dissipada ($P$) por Efeito Joule nos resistores.
  - Constante de Tempo ($\tau = R \cdot C$) e curva de carga exponencial do capacitor $V(t)$.
- **Interface Interativa (Streamlit):**
  - Ajuste de parâmetros (Tensão, Resistência e Capacitância) através de sliders intuitivos.
  - Gráfico dinâmico da curva de carga do capacitor.
- **Análise Comparativa:**
  - Comparação visual entre o circuito configurado pelo usuário e circuitos reais pré-configurados (como carregadores de celular, fontes de PC ou flash de câmera).

---

##  Tecnologias Utilizadas

- **Python 3** (Lógica do simulador e Orientação a Objetos)
- **Streamlit** (Interface gráfica Web interativa)
- **Matplotlib & NumPy** (Geração e plotagem dos gráficos de física)
