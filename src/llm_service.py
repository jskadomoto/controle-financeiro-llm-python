import ollama
import json
import config
from typing import Dict, Optional

def extract_transaction_data(user_text: str) -> Optional[Dict]:
    """
    Uses the LLM to extract and classify transaction data from user text.

    Args:
        user_text (str): The raw text input from the user.

    Returns:
        Optional[Dict]: A dictionary with the extracted data or None if an error occurs.
    """
    prompt = config.PROMPT_TEMPLATE.format(user_text=user_text)
    
    try:
        response = ollama.chat(
            model=config.LLM_MODEL,
            messages=[{'role': 'user', 'content': prompt}],
            format='json'
        )
        parsed_json = json.loads(response['message']['content'])
        return parsed_json
    except (json.JSONDecodeError, KeyError, Exception) as e:
        print(f"Error processing LLM response: {e}")
        return None