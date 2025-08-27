# src/main.py

import streamlit as st
import plotly.express as px
import pandas as pd
import database
import llm_service

# --- Page Config ---
st.set_page_config(layout="wide", page_title="Meu Gerenciador Financeiro")

# --- Application State ---
# Initialize the database on first run
database.initialize_database()

# --- UI Layout ---
st.title("💸 Meu Gerenciador Financeiro Pessoal")
st.write("Use linguagem natural para adicionar suas receitas e despesas.")

st.header("Adicionar Nova Transação")

# --- Formulário de Adição ---
with st.form(key="transaction_form", clear_on_submit=True):
    user_input = st.text_input(
        "Descreva sua transação:",
        placeholder="Ex: Paguei R$ 39,90 na Netflix",
        key="user_input_box",
        label_visibility="collapsed"
    )
    
    submitted = st.form_submit_button("Adicionar Transação")

if submitted:
    if user_input:
        with st.spinner("Classificando sua transação..."):
            transaction_data = llm_service.extract_transaction_data(user_input)

        if transaction_data:
            try:
                # Valida e extrai os dados
                transaction_data['amount'] = float(transaction_data.get('amount', 0))
                description = transaction_data.get('description', 'N/A')
                amount = transaction_data.get('amount', 0)
                
                # Adiciona a transação ao banco de dados
                database.add_transaction(transaction_data)
                
                # Mostra a mensagem de sucesso
                st.success(f"Transação adicionada: {description} - R$ {amount:,.2f}")

            except (ValueError, TypeError) as e:
                st.error(f"Não foi possível processar os detalhes. Tente ser mais específico. Erro: {e}")
                st.json(transaction_data)
    else:
        st.warning("Por favor, descreva uma transação.")

st.divider()

#--- Financial Dashboard ---#
st.header("Seu Resumo Financeiro")
transactions_df = database.get_all_transactions()

if not transactions_df.empty:
    # --- Metrics --- #
    col1, col2, col3 = st.columns(3)
    total_income = transactions_df[transactions_df['transaction_type'] == 'income']['amount'].sum()
    total_expenses = transactions_df[transactions_df['transaction_type'] == 'expense']['amount'].sum()
    balance = total_income - total_expenses

    col1.metric("Total de Receitas", f"R$ {total_income:,.2f}")
    col2.metric("Total de Despesas", f"R$ {total_expenses:,.2f}")
    col3.metric("Saldo Atual", f"R$ {balance:,.2f}")

    st.divider()

    #--- Charts and Data Tables ---#
    charts_col, table_col = st.columns([0.4, 0.6])

    with charts_col:
        st.subheader("Despesas por Categoria")
        expense_df = transactions_df[transactions_df['transaction_type'] == 'expense']

        if not expense_df.empty:
            fig = px.pie(expense_df, names='category', values='amount', hole=.3, title='Distribuição de Gastos')
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.write("Nenhuma despesa registrada ainda.")

    with table_col:
        st.subheader("Últimas Transações")
        
        # Cria uma cópia para evitar avisos de alteração no DataFrame original
        display_df = transactions_df.copy()
        
        # --- FORMATAÇÃO DOS DADOS ---
        # Converte a coluna 'timestamp' para o formato de data e hora do pandas
        display_df['timestamp'] = pd.to_datetime(display_df['timestamp'])
        
        # Traduz transaction_type
        display_df['transaction_type'] = display_df['transaction_type'].replace({
          'expense': 'Despesa',
          'income': 'Receita'
        })
        
        # Formata a data para o padrão brasileiro (dd/mm/aaaa às HH:MM)
        display_df['timestamp'] = display_df['timestamp'].dt.strftime('%d/%m/%Y às %H:%M')
        
        # Formata a coluna 'amount' como moeda brasileira (R$ 1.234,56)
        display_df['amount'] = display_df['amount'].apply(lambda x: f"R$ {x:,.2f}".replace(",", "v").replace(".", ",").replace("v", "."))

        # Renomeia as colunas para exibição em pt-BR
        display_df = display_df.rename(columns={
            'timestamp': 'Data',
            'description': 'Descrição',
            'category': 'Categoria',
            'transaction_type': 'Tipo',
            'amount': 'Valor'
        })
        
        st.dataframe(
            display_df[['Data', 'Descrição', 'Categoria', 'Tipo', 'Valor']],
            use_container_width=True
        )
else:
    st.info("Nenhuma transação registrada. Adicione uma acima para começar!")