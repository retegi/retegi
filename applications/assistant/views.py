
# Create your views here.
from django.shortcuts import render

def assistant_view(request):
    return render(request, 'home/assistant.html')


def assistant_response(request):
    if request.method == "POST":
        user_message = request.POST.get('message', '')
        if not user_message:
            return JsonResponse({'error': 'No message provided'}, status=400)

        response = ask_openai(user_message)
        return JsonResponse({'response': response})
    return JsonResponse({'error': 'Invalid request method'}, status=405)
