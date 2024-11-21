# Calculadora de Pegada de Carbono

Este projeto é uma **Calculadora de Pegada de Carbono** desenvolvida com o objetivo de conscientizar os usuários sobre suas emissões de CO₂ e sugerir formas de reduzir seu impacto ambiental. A aplicação foi desenvolvida seguindo os princípios de **Domain-Driven Design (DDD)** e utiliza Python (Flask) no backend e HTML/CSS/JavaScript no frontend.

## 🚀 Funcionalidades
- **Questionário responsivo**: Um formulário com várias etapas que coleta informações sobre transporte, energia, resíduos, estilo de vida e alimentação.
- **Cálculo da pegada de carbono**: A aplicação calcula o total de toneladas de CO₂ emitidas anualmente com base nos dados fornecidos.
- **Sugestões personalizadas**: Fornece recomendações para reduzir a pegada de carbono.
- **Backend com Flask**: Gerencia os cálculos no servidor, seguindo as melhores práticas de arquitetura.

## 🛠️ Tecnologias Utilizadas
### Backend
- **Python 3.10**
- **Flask**: Framework para criar a API REST.
- **MySQL**: Banco de dados para armazenar informações (se aplicável).
- **Chart.js**: Para renderização de gráficos interativos.

### Frontend
- **HTML5**, **CSS3**, **JavaScript**
- **Bootstrap 5.3**: Para estilização responsiva.

## 📊 Exemplos de Uso
1. Preencha o formulário com informações sobre transporte, energia, resíduos, estilo de vida e alimentação.
2. Envie os dados para cálculo.
3. Visualize os resultados:
-Pegada de carbono anual (toneladas de CO₂).
-Sugestões práticas para redução.
-Gráficos detalhados com as emissões.

## 💻 Como Rodar o Projeto Localmente
### Pré-requisitos
- **Python 3.10** ou superior.
- **Git** para clonar o repositório.
- **Virtualenv** para gerenciar dependências (opcional).

### Passo a passo

1. **Crie e ative um ambiente virtual**
   python -m venv venv
   #No Mac/Linux source venv/bin/activate  #No Windows: venv\Scripts\activate
   
2. **Instale as dependências**
   pip install -r requirements.txt

3. **Inicie o servidor Flask**
   python run.py

4. **Acesse a aplicação no navegador**
   URL: http://127.0.0.1:5000

## 👥 Integrantes
- Henrique Santos Nogueira - RM:554666
- Jenifer Souza - RM: 558047
- Sophia Piccirillo - RM: 554768
- Vitor Gabriel Laurindo Borin - RM:558643

## Link PythonAnywhere
https://vxtinxx.pythonanywhere.com/
