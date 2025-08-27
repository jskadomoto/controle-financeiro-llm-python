
#--- Database Config ---#
DB_FILE = "finance_tracker.db"

#--- LLM Service Config ---#
LLM_MODEL = 'phi3'

#--- App Config ---#
VALID_TRANSACTION_TYPES = ["income", "expense"]
VALID_CATEGORIES = ["Alimentação", "Transporte", "Moradia", "Lazer", "Saúde", "Educação", "Compras", "Salário", "Assinaturas", "Outros"]

PROMPT_TEMPLATE = f"""
  Você é um assistente de finanças pessoais especialista em extrair dados de texto em português.
  Analise o texto do usuário e retorne um objeto JSON com as seguintes chaves:
  - "type": deve ser um dos seguintes: {VALID_TRANSACTION_TYPES}. Use "income" para entradas e "expense" para saídas.
  - "description": uma breve descrição da transação.
  - "amount": o valor numérico da transação.
  - "category": a categoria mais apropriada da lista: {VALID_CATEGORIES}.
  
  Texto do usuário: "{{user_text}}"
  
  Se o texto indicar uma entrada de dinheiro (ex: salário, recebimento), use o tipo "income".
  Se for um gasto, pagamento ou compra, use o tipo "expense".
  
  Retorne APENAS o objeto JSON válido.
"""