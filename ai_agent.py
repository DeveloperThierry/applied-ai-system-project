import os
import logging
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Setup Logging
logging.basicConfig(filename='game_system.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# --- THE SWITCH ---
# We tell the client to talk to Groq's server instead of OpenAI's
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

def get_ai_hint(secret_number, guess_history, difficulty):
    prompt = f"""
    You are a strategic 'Game Master'. 
    The secret number is {secret_number}. 
    The user has guessed: {guess_history}.
    The difficulty is {difficulty}.

    Provide a short, clever hint WITHOUT revealing the number {secret_number}.
    """

    try:
        response = client.chat.completions.create(
            # --- THE MODEL ---
            # llama3-8b-8192 is fast and free on Groq
            model="llama-3.1-8b-instant",
            messages=[{"role": "system", "content": prompt}],
            temperature=0.7
        )
        hint = response.choices[0].message.content

        # Reliability Guardrail
        if str(secret_number) in hint:
            logging.warning(f"Guardrail Triggered: AI leaked secret {secret_number}")
            return "The Game Master is being cryptic... look at the patterns in your guesses!"
        
        logging.info(f"Groq Hint Generated for secret {secret_number}")
        return hint

    except Exception as e:
        logging.error(f"Groq Service Error: {e}")
        return f"The AI Hint system is taking a nap. Trust your intuition! {e}"