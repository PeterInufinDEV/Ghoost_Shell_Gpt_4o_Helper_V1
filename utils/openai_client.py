# utils/openai_client.py (for openai>=1.0.0)
import openai
from config import OPENAI_API_KEY, MODEL

client = openai.OpenAI(api_key=OPENAI_API_KEY)

def ask_gpt(prompt, system_msg="You are a helpful assistant"):
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": system_msg},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
            max_tokens=1024
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"XXX Error: {str(e)}"
