import openai
from django.conf import settings

def ask_openai(prompt):
    openai.api_key = settings.OPENAI_API_KEY

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "Eres un asistente virtual útil."},
                      {"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=150,
        )
        return response.choices[0].message['content']
    except Exception as e:
        return f"Hubo un error: {e}"
