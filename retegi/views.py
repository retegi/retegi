from django.shortcuts import render
from django.http import JsonResponse
import openai
from django.conf import settings

# Renderiza la página de chat
import os
from django.conf import settings

# views.py

MAX_HISTORY = 30  # Mantén los últimos 10 mensajes


def chat_view(request):
    return render(request, 'home/chat.html')  # Asegúrate de tener una plantilla llamada chat.html

def load_instructions():
    instructions_path = os.path.join(settings.BASE_DIR, 'applications','assistant', 'indications', 'instructions.txt')
    company_data_path = os.path.join(settings.BASE_DIR, 'applications','assistant', 'indications', 'company_data.txt')

    try:
        with open(instructions_path, 'r') as instructions_file:
            instructions = instructions_file.read()
        with open(company_data_path, 'r') as data_file:
            company_data = data_file.read()
        # Combina las instrucciones con los datos de la empresa
        return f"{instructions}\n\nInformación de la empresa:\n{company_data}"
    except FileNotFoundError:
        return "Eres un asistente virtual amigable y útil."


# Maneja las solicitudes al bot

def get_bot_response(request):
    if request.method == 'POST':
        user_message = request.POST.get('message', '')
        openai.api_key = settings.OPENAI_API_KEY

        # Inicializa o recupera el historial de la conversación
        if 'conversation_history' not in request.session:
            request.session['conversation_history'] = [
                {"role": "system", "content": "Eres un asistente útil que recuerda los detalles del usuario (como su nombre) durante esta conversación, pero no guarda información después de que la sesión termina."}
            ]

        # Agrega el mensaje del usuario al historial
        request.session['conversation_history'].append({"role": "user", "content": user_message})

        # Limitar el historial a los últimos 10 mensajes
        request.session['conversation_history'] = request.session['conversation_history'][-MAX_HISTORY:]

        try:
            # Enviar todo el historial a OpenAI
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=request.session['conversation_history']
            )

            # Obtén la respuesta del bot
            bot_reply = response['choices'][0]['message']['content']

            # Agrega la respuesta del bot al historial
            request.session['conversation_history'].append({"role": "assistant", "content": bot_reply})
            request.session.modified = True  # Asegura que los cambios se guarden

            return JsonResponse({'reply': bot_reply})
        except Exception as e:
            return JsonResponse({'error': str(e)})

    return JsonResponse({'error': 'Invalid request'})


def end_conversation(request):
    if 'conversation_history' in request.session:
        del request.session['conversation_history']
    return JsonResponse({'status': 'Conversación finalizada'})
