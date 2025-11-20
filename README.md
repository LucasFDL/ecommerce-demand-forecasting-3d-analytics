# E-commerce Demand Forecasting with 3D Analytics

[![pt-br](https://img.shields.io/badge/🇧🇷_Ler_em_Português-Clique_Aqui-green?style=for-the-badge)](#pt-br)

> **Status:** Planning / early development 🚧

Forecasting e-commerce demand per category/SKU using real-world-like data, with a focus on **EDA**, **time-series models**, **3D visualizations** and an **interactive BI dashboard**.

---

## 📌 Project Overview

**Goal** Analyze e-commerce sales data to understand **purchase patterns** and build a **demand forecasting model** (per category/SKU) with proper **backtesting** and **business-oriented metrics**.

**Key outputs**

- Clean and well-documented dataset (`data/raw`, `data/processed`)
- EDA with 2D and 3D visualizations (Plotly)
- Time-series forecasting models with rolling-origin backtesting
- Interactive dashboard (Power BI / Plotly) with a **price & promotion simulator**

---

## 📊 Dataset

_To be defined._

Planned options:

- Public e-commerce datasets from Kaggle (e.g. Brazilian e-commerce data)
- Synthetic dataset generated to simulate categories/SKUs, price and promotions

Once defined, this section will include:

- Link to the original source
- Data dictionary (main columns)
- Basic notes about preprocessing and limitations

---

## 🗂 Repository Structure

Planned structure (may evolve as the project grows):

```text
.
├── data
│   ├── raw/          # Original datasets (not tracked in Git if sensitive/large)
│   └── processed/    # Cleaned / feature-engineered data
├── notebooks
│   ├── 01_eda.ipynb               # Exploratory data analysis
│   └── 02_modeling_forecast.ipynb # Modeling and backtesting
├── src
│   ├── data_prep.py               # Data cleaning and feature engineering
│   ├── models.py                  # Forecasting models and evaluation
│   └── viz.py                     # Plotly visualizations (2D/3D)
├── reports
│   └── figures/                   # Saved plots (PNG/HTML)
├── dashboard
│   └── ...                        # Power BI / Plotly dashboard files
├── requirements.txt
└── README.md
```

> ⚠️ `data/raw` and `data/processed` should be documented, and large/sensitive files should not be committed directly to Git.

---

## 🧰 Tech Stack

- **Python** (Pandas, NumPy, Scikit-learn, Plotly)
- **Time-series & forecasting** (baseline models, optionally LightGBM/XGBoost/Prophet)
- **Jupyter Notebook**
- **Power BI / Plotly** for dashboards
- **Git & GitHub** for version control

---

## 🔍 Work Plan (high-level)

1. **Data Collection & Preparation**
   - Select a public e-commerce dataset
   - Save raw data in `data/raw/`
   - Build a simple data dictionary and initial checks
2. **Cleaning & Feature Engineering**
   - Handle missing values and outliers
   - Create calendar features (weekday, month, holidays)
   - Create lags and moving averages (e.g. `sales_t-1`, `sales_t-7`)
   - Aggregate at the chosen grain (category and/or SKU)
3. **EDA & 3D Visualizations**
   - Explore seasonality and trends by category
   - Correlation analysis (price, discount, sales, lags)
   - 3D scatter/line plots (price × sales × discount, color = category)
4. **Forecasting Models & Backtesting**
   - Baselines: Naive, Seasonal Naive, Moving Average
   - Models: ElasticNet / Gradient Boosting / LightGBM or similar
   - Rolling-origin backtesting with MAE and wMAPE
   - Error analysis by category and by time window
5. **Dashboard & Simulator**
   - Build an interactive dashboard (Power BI / Plotly)
   - Price/promotion sliders and comparison vs current scenario
   - Highlight main insights and recommendations
6. **Documentation**
   - Document how to run the project and main insights
   - Add plots and dashboard screenshots to the README
   - Save metrics and backtesting results in structured files (e.g. `metrics.json`)

---

## 🚀 How to Run (work in progress)

1. **Clone this repository**
   
```bash
git clone [https://github.com/LucasFDL/ecommerce-demand-forecasting-3d-analytics.git](https://github.com/LucasFDL/ecommerce-demand-forecasting-3d-analytics.git)
cd ecommerce-demand-forecasting-3d-analytics
```

2. **Create a virtual environment**

```bash
python -m venv .venv
```

3. **Activate the virtual environment**

**On Windows:**
```bash
.venv\Scripts\activate
```

**On Linux/macOS:**
```bash
source .venv/bin/activate
```

4. **Install dependencies**
```bash
pip install -r requirements.txt
```

5. **Open the notebooks**
```bash
jupyter notebook
```
> This section will be updated as the project evolves (specific commands, scripts, and environment details).

---

## ✅ Status & Next Steps

- [x] Create repository and initial README  
- [ ] Choose dataset and describe it in the **Dataset** section  
- [ ] Set up `requirements.txt` and initial folder structure  
- [ ] Implement and document EDA (`notebooks/01_eda.ipynb`)  
- [ ] Implement forecasting models and backtesting (`notebooks/02_modeling_forecast.ipynb`)  
- [ ] Build dashboard and add screenshots to `reports/` and this README  

---

## 📬 Contact

Suggestions, ideas or feedback are welcome:
  - GitHub: @LucasFDL
  - LinkedIn: Lucas Dias
  - Email: lucasdias000722@gmail.com

<br>
<br>

---

<a name="pt-br"></a>

<details>
<summary><strong>🇧🇷 Clique aqui para ver a versão em Português / Click to read in Portuguese</strong></summary>

<br>

# 🇧🇷 Previsão de Demanda E-commerce com Analytics 3D

> **Status:** Planejamento / desenvolvimento inicial 🚧

Previsão de demanda de e-commerce por categoria/SKU utilizando dados realistas, com foco em **EDA**, **modelos de séries temporais**, **visualizações 3D** e um **dashboard de BI interativo**.

---

## 📌 Visão Geral do Projeto

**Objetivo** Analisar dados de vendas de e-commerce para entender **padrões de compra** e construir um **modelo de previsão de demanda** (por categoria/SKU) com **backtesting** adequado e **métricas orientadas a negócios**.

**Principais entregas**

- Dataset limpo e bem documentado (`data/raw`, `data/processed`)
- EDA com visualizações 2D e 3D (Plotly)
- Modelos de previsão de séries temporais com backtesting de origem rolante (*rolling-origin*)
- Dashboard interativo (Power BI / Plotly) com um **simulador de preços e promoções**

---

## 📊 Dataset

_A definir._

Opções planejadas:

- Datasets públicos de e-commerce do Kaggle (ex: dados de e-commerce brasileiro)
- Dataset sintético gerado para simular categorias/SKUs, preços e promoções

Assim que definido, esta seção incluirá:

- Link para a fonte original
- Dicionário de dados (colunas principais)
- Notas básicas sobre pré-processamento e limitações

---

## 🗂 Estrutura do Repositório

Estrutura planejada (pode evoluir conforme o projeto cresce):

```text
.
├── data
│   ├── raw/          # Datasets originais (não rastreados no Git se sensíveis/grandes)
│   └── processed/    # Dados limpos / feature engineering
├── notebooks
│   ├── 01_eda.ipynb               # Análise exploratória de dados
│   └── 02_modeling_forecast.ipynb # Modelagem e backtesting
├── src
│   ├── data_prep.py               # Limpeza de dados e feature engineering
│   ├── models.py                  # Modelos de previsão e avaliação
│   └── viz.py                     # Visualizações Plotly (2D/3D)
├── reports
│   └── figures/                   # Gráficos salvos (PNG/HTML)
├── dashboard
│   └── ...                        # Arquivos do dashboard Power BI / Plotly
├── requirements.txt
└── README.md
```

> ⚠️ `data/raw` e `data/processed` devem ser documentados, e arquivos grandes/sensíveis não devem ser commitados diretamente no Git.

---

## 🧰 Tecnologias Utilizadas

- **Python** (Pandas, NumPy, Scikit-learn, Plotly)
- **Séries temporais e previsão** (modelos base, opcionalmente LightGBM/XGBoost/Prophet)
- **Jupyter Notebook**
- **Power BI / Plotly** para dashboards
- **Git & GitHub** para controle de versão

---

## 🔍 Plano de Trabalho (Alto Nível)

1. **Coleta e Preparação de Dados**
   - Selecionar um dataset público de e-commerce
   - Salvar dados brutos em `data/raw/`
   - Criar dicionário de dados simples e verificações iniciais
2. **Limpeza e Engenharia de Atributos (Feature Engineering)**
   - Tratar valores ausentes e outliers
   - Criar atributos de calendário (dia da semana, mês, feriados)
   - Criar defasagens (lags) e médias móveis (ex: `vendas_t-1`, `vendas_t-7`)
   - Agregar no nível escolhido (categoria e/ou SKU)
3. **EDA e Visualizações 3D**
   - Explorar sazonalidade e tendências por categoria
   - Análise de correlação (preço, desconto, vendas, lags)
   - Gráficos de dispersão/linha 3D (preço × vendas × desconto, cor = categoria)
4. **Modelos de Previsão e Backtesting**
   - Baselines: Naive, Sazonal Naive, Média Móvel
   - Modelos: ElasticNet / Gradient Boosting / LightGBM ou similar
   - Backtesting de origem rolante com MAE e wMAPE
   - Análise de erro por categoria e por janela de tempo
5. **Dashboard e Simulador**
   - Construir dashboard interativo (Power BI / Plotly)
   - Sliders de preço/promoção e comparação vs cenário atual
   - Destacar principais insights e recomendações
6. **Documentação**
   - Documentar como rodar o projeto e principais insights
   - Adicionar gráficos e screenshots do dashboard ao README
   - Salvar métricas e resultados de backtesting em arquivos estruturados (ex: `metrics.json`)

---

## 🚀 Como Executar (em andamento)

1. **Clonar este repositório**
   
```bash
git clone [https://github.com/LucasFDL/ecommerce-demand-forecasting-3d-analytics.git](https://github.com/LucasFDL/ecommerce-demand-forecasting-3d-analytics.git)
cd ecommerce-demand-forecasting-3d-analytics
```

2. **Criar um ambiente virtual**

```bash
python -m venv .venv
```

3. **Ativar o ambiente virtual**

**No Windows:**
```bash
.venv\Scripts\activate
```

**No Linux/macOS:**
```bash
source .venv/bin/activate
```

4. **Instalar dependências**
```bash
pip install -r requirements.txt
```

5. **Abrir os notebooks**
```bash
jupyter notebook
```
> Esta seção será atualizada conforme o projeto evolui (comandos específicos, scripts e detalhes do ambiente).

---

## ✅ Status e Próximos Passos

- [x] Criar repositório e README inicial  
- [ ] Escolher dataset e descrevê-lo na seção **Dataset** - [ ] Configurar `requirements.txt` e estrutura inicial de pastas  
- [ ] Implementar e documentar EDA (`notebooks/01_eda.ipynb`)  
- [ ] Implementar modelos de previsão e backtesting (`notebooks/02_modeling_forecast.ipynb`)  
- [ ] Construir dashboard e adicionar screenshots em `reports/` e neste README  

---

## 📬 Contato

Sugestões, ideias ou feedbacks são bem-vindos:
  - GitHub: @LucasFDL
  - LinkedIn: Lucas Dias
  - Email: lucasdias000722@gmail.com

</details>
