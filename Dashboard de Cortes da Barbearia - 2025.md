# Dashboard de Cortes da Barbearia - 2025

Este é um dashboard interativo construído com Streamlit para visualizar dados de cortes de cabelo de uma barbearia ao longo de 2025.

## Funcionalidades

- Gráfico de linhas mostrando a evolução mensal de cortes.
- Gráfico de barras para comparar mês a mês.
- Destaque para os meses de pico.
- Indicadores Principais (KPIs): Total de cortes no ano, Média mensal de cortes, Mês com maior número de cortes, Mês com menor número de cortes.
- Seletor interativo para o usuário escolher quais meses visualizar.

## Como Executar Localmente

1.  **Certifique-se de ter Python instalado.**
2.  **Crie um ambiente virtual (opcional, mas recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: .venv\Scripts\activate
    ```
3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Execute o aplicativo Streamlit:**
    ```bash
    streamlit run app.py
    ```
    O aplicativo será aberto automaticamente no seu navegador padrão.

## Como Implantar no Streamlit Community Cloud (Gratuito e Fácil)

Para implantar este dashboard permanentemente e de forma gratuita, siga estes passos:

1.  **Crie uma conta no GitHub** (se ainda não tiver).
2.  **Crie um novo repositório no GitHub** e faça o upload dos seguintes arquivos para ele:
    -   `app.py` (o código do seu dashboard)
    -   `requirements.txt` (lista de dependências)
    -   `README.md` (este arquivo, opcional, mas útil)
3.  **Vá para o [Streamlit Community Cloud](https://share.streamlit.io/)** e faça login com sua conta GitHub.
4.  **Clique em "New app"** e selecione o repositório que você acabou de criar.
5.  **Configure as opções de implantação:**
    -   **Repository:** Selecione o repositório onde você fez o upload dos arquivos.
    -   **Branch:** Geralmente `main` ou `master`.
    -   **Main file path:** `app.py` (o nome do seu arquivo principal do Streamlit).
    -   **Python version:** Escolha a versão do Python que você usou (por exemplo, 3.9, 3.10, 3.11).
6.  **Clique em "Deploy!"**

O Streamlit Community Cloud irá construir e implantar seu aplicativo. Uma vez concluído, você receberá um URL público para o seu dashboard, que estará disponível 24/7.

---

**Arquivos fornecidos:**

-   `app.py`
-   `requirements.txt`


