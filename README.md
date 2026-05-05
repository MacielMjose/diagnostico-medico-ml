# 🔬 Diagnóstico de SOP (Síndrome dos Ovários Policísticos) — PCOS

Projeto de Machine Learning para classificação e explicabilidade do diagnóstico de PCOS com base em dados clínicos e laboratoriais.

---

## 📋 Sumário

- [Sobre o Projeto](#sobre-o-projeto)
- [Estrutura do Notebook](#estrutura-do-notebook)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Configuração do Kaggle](#configuração-do-kaggle)
- [Como Rodar](#como-rodar)
- [Modelos Utilizados](#modelos-utilizados)
- [Resultados Esperados](#resultados-esperados)

---

## Sobre o Projeto

Este notebook utiliza o dataset **PCOS Without Infertility** do Kaggle para treinar e comparar modelos de classificação que preveem a presença de SOP (Síndrome dos Ovários Policísticos). O projeto cobre desde a análise exploratória (EDA) até a explicabilidade das predições com **SHAP**.

**Dataset:** [Polycystic Ovary Syndrome (PCOS) — Kaggle](https://www.kaggle.com/datasets/prasoonkottarathil/polycystic-ovary-syndrome-pcos)

---

## Estrutura do Notebook

```
1. Importações
2. Funções auxiliares
3. Carregamento dos dados (via KaggleHub)
4. Análise Exploratória (EDA)
   ├── 4.1 Visão geral do dataset
   ├── 4.2 Valores nulos e limpeza
   ├── 4.3 Tratamento de colunas problemáticas
   ├── 4.4 Codificação de variáveis categóricas
   ├── 4.5 Distribuição do target
   ├── 4.6 Correlação com o target
   ├── 4.7 Boxplot + Violin — Top 20 features
   ├── 4.8 Histogramas por classe
   ├── 4.9 Matriz de correlação geral
   └── 4.10 Pares altamente correlacionados
5. Pré-processamento e Pipeline
6. Divisão Treino / Teste
7. Comparação de Modelos (Cross-Validation 5-fold)
8. Análise de Overfitting
9. Curva ROC comparativa
10. Seleção das Top 20 Features
11. Explicabilidade com SHAP
```

---

## Pré-requisitos

- Python **3.9+**
- Conta no [Kaggle](https://www.kaggle.com/) com API configurada (veja [Configuração do Kaggle](#configuração-do-kaggle))
- Google Colab

---

## Instalação

### 1. Clone o repositório (ou baixe o notebook)

```bash
git clone https://github.com/MacielMjose/diagnostico-medico-ml.git
cd diagnostico-medico-ml
```
---

## Configuração do Kaggle

O dataset é baixado automaticamente via **KaggleHub**. Para isso, você precisa configurar suas credenciais da API do Kaggle.

## Como Rodar

### Google Colab (sem instalar nada)

A forma mais rápida de rodar o projeto é direto no navegador, sem precisar configurar ambiente local:

**→ [https://colab.research.google.com/](https://colab.research.google.com/)**

1. Faça o download do repositorio => [diagnostico-medico-ml](https://github.com/MacielMjose/diagnostico-medico-ml)
2. Acesse o link acima (requer conta Google)
3. No colab, clicar em: Arquivo > **"Abrir Notebook"**
4. Selecione a opção **"Upload"**
5. Clicar em **"Procurar"**
4. Clique em **"Ambiente de execução → Executar tudo"**

> ⚠️ No Colab gratuito, sessões são encerradas após ~90 minutos de inatividade. Para notebooks longos, considere manter a aba aberta ou usar o Colab Pro.

---

## Resultados Esperados

Ao final da execução, o notebook gera:

- 📊 Gráficos de EDA (heatmaps, violinplots, histogramas, matriz de correlação)
- 📈 Curvas ROC comparativas entre os modelos
- 🏆 Tabelas de métricas — todas as features vs. Top 20 features
- 🔍 SHAP Summary Plot e Feature Importance — explicando as predições da Regressão Logística
- 🖼️ Arquivo `matriz_metricas.png` salvo no diretório de execução

---

## Observações

- O download do dataset ocorre apenas na **primeira execução** e fica em cache local pelo KaggleHub.
- O notebook foi desenvolvido e testado com **Python 3.11**.
- Gráficos gerados com `shap.summary_plot` abrem em janelas separadas dependendo do backend do matplotlib. No Jupyter, são exibidos inline.


# Tech Challenge - Fase 1 | Projeto EXTRA

## Como Rodar o Projeto

Este projeto foi desenvolvido para ser executado no **Google Colab**.

Para rodar, baixe no GitHub o arquivo:

```text
Challenge_Extra/Tech_challenge_A_PCOS__EXTRA.ipynb
```

Depois, importe esse arquivo no Google Colab e execute as celulas em ordem.

## Imagem para Predicao

Na etapa de predição é utilizada uma imagem que está na pasta `assets` do projeto.

![alt text](https://github.com/MacielMjose/diagnostico-medico-ml/blob/samuel/misc/01-prediction-section.png)

Localização:

```text
Challenge_Extra/assets/image_para_teste.jpeg
```

Durante a execução desta etapa, na célula 15, é necessario enviar manualmente essa imagem no Colab.

![alt text](https://github.com/MacielMjose/diagnostico-medico-ml/blob/samuel/misc/02-prediction-section.png)


## Passo a Passo no Google Colab

### 1. Baixar o projeto do GitHub

Clone o repositorio na sua maquina:

```bash
git clone https://github.com/MacielMjose/diagnostico-medico-ml.git
cd diagnostico-medico-ml
```

Depois de clonar, localize o arquivo do projeto no seguinte caminho:

```text
Challenge_Extra/Tech_challenge_A_PCOS__EXTRA.ipynb
```

### 2. Abrir o Google Colab

Acesse:

```text
https://colab.research.google.com/
```

### 3. Importar o arquivo no Colab

No Google Colab:

1. Clique em **File > Upload notebook**.
2. Selecione o arquivo `Tech_challenge_A_PCOS__EXTRA.ipynb` baixado do GitHub.
3. Aguarde o notebook abrir no Colab.

### 4. Ativar GPU

No menu do Colab:

```text
Runtime > Change runtime type
```

Em **Hardware accelerator**, selecione uma GPU disponivel, como `T4 GPU`.

### 5. Executar o projeto

Execute as células do notebook em ordem, do inicio ao fim.

O notebook baixa o dataset automaticamente usando `kagglehub`.
