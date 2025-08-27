# 💸 Gerenciador Financeiro Pessoal com LLM

Uma aplicação web simples para controle de despesas e receitas utilizando linguagem natural, construída com **Python**, **Streamlit** e um modelo de linguagem local (**Ollama**).

---

## 📖 Sobre o Projeto

Este projeto nasceu como um estudo prático sobre a integração de **Modelos de Linguagem Grandes (LLMs)** em aplicações do dia a dia.  
A ideia é eliminar a necessidade de preencher formulários tradicionais para controle financeiro, permitindo que o usuário simplesmente **"converse" com a aplicação**, descrevendo suas transações em português.

O **LLM** interpreta o texto, extrai os dados relevantes (**descrição, valor, categoria, tipo**) e a aplicação os armazena em um banco de dados local para visualização em um **dashboard interativo**.

---

## ✨ Funcionalidades Atuais

- 📝 **Adição de Transações por Linguagem Natural**: Registre uma despesa ou receita escrevendo uma frase simples.
- 🏷️ **Classificação Automática**: O LLM categoriza automaticamente a transação (Alimentação, Transporte, Salário, etc.).
- 📊 **Dashboard Interativo**:
  - Total de receitas, despesas e saldo atual
  - Gráfico de pizza com a distribuição de gastos por categoria
  - Tabela com o histórico de transações formatado
- 🌎 **Interface 100% em Português**: Focada na experiência do usuário brasileiro.
- 🔒 **Privacidade Total**: Roda 100% local, sem enviar seus dados financeiros para a nuvem.

---

## 🛠️ Tecnologias Utilizadas

- **Backend**: Python  
- **Frontend**: Streamlit  
- **LLM**: Ollama (modelo *phi3*)  
- **Banco de Dados**: SQLite  
- **Manipulação de Dados**: Pandas  
- **Gráficos**: Plotly Express  

---

## 🚀 Setup e Instalação

### 1. Pré-requisitos
- [Python 3.10+](https://www.python.org/downloads/)  
- [Git](https://git-scm.com/)  
- [Ollama](https://ollama.com) (instalado e funcionando)  

### 2. Passo a Passo

#### 1. Clone o Repositório
```bash
git clone <https://github.com/jskadomoto/controle-financeiro-llm-python.git>
cd <controle-financeiro-llm-python>
```

#### 2. Crie o ambiente virtual
```bash
python -m venv venv

# Ative o ambiente (Windows)
venv\Scripts\activate

# Ative o ambiente (macOS/Linux)
source venv/bin/activate
```

#### 3. Instale as Dependências
```bash
source venv/bin/activate
```

#### 4. Inicie o Servidor LLM (Ollama)
Abra um novo terminal e execute o comando abaixo (mantenha aberto):
```bash
ollama run phi3
```

#### Execute a Aplicação Streamlit
No terminal com o ambiente virtual ativo:
```bash
streamlit run src/main.py
```

## 🎮 Como Utilizar

1. Com a aplicação aberta no navegador, digite no campo **"Descreva sua transação:"** algo como:

   - 💸 *"Gastei 150 reais no supermercado hoje"*  
   - 💰 *"Recebi meu salário de 5000 reais"*  
   - 📺 *"Paguei a mensalidade de R$ 55,90 da Netflix"*  

2. Pressione **Enter** ou clique em **Adicionar Transação**.  
3. O **LLM** processará a informação e o **dashboard** será atualizado automaticamente.  

---

## 🗺️ Roadmap de Novas Funcionalidades

### ✅ Fase 1: Filtros por Período (Mês e Ano)
- Adicionar filtros de período (**ano/mês**) acima do dashboard  
- Filtrar `transactions_df` antes dos cálculos de métricas  
- Atualizar métricas, gráficos e tabelas com `filtered_df`  

### ✅ Fase 2: Visualizações Anuais e Totais
- Visão **Total** (já implementada por padrão)  
- Visão **Anual** com agrupamento de despesas por mês  
- Novo **gráfico de barras** mostrando a evolução de gastos mensais  

---

## 📄 Licença

Este projeto está licenciado sob a **Licença MIT**.  
Veja o arquivo [LICENSE](LICENSE) para mais detalhes.





