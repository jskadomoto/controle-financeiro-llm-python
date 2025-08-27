# database.py

import sqlite3
import pandas as pd
from datetime import datetime
import config

def get_db_connection():
    """Establishes a connection to the SQLite database."""
    conn = sqlite3.connect(config.DB_FILE)
    return conn

def initialize_database():
    """Creates the transactions table if it doesn't already exist."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            transaction_type TEXT NOT NULL,
            description TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT,
            timestamp TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_transaction(transaction: dict):
    """Adds a new transaction to the database.

    Args:
        transaction (dict): A dictionary containing transaction details.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    current_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    cursor.execute(
        "INSERT INTO transactions (transaction_type, description, amount, category, timestamp) VALUES (?, ?, ?, ?, ?)",
        (
            transaction.get('type'),
            transaction.get('description'),
            transaction.get('amount'),
            transaction.get('category'),
            current_timestamp
        )
    )
    conn.commit()
    conn.close()

def get_all_transactions() -> pd.DataFrame:
    """Retrieves all transactions from the database, sorted by date.

    Returns:
        pd.DataFrame: A DataFrame containing all transaction records.
    """
    conn = get_db_connection()
    df = pd.read_sql_query("SELECT * FROM transactions ORDER BY timestamp DESC", conn)
    conn.close()
    return df