from django.shortcuts import render
from django.http import HttpResponse
import requests

def translate_to_indian_language(request):
    if request.method == 'POST':
        input_text = request.POST.get('text', '')
        target_language = request.POST.get('target_language', 'hi')  # Default to Hindi

        if input_text:
            translation = translate_text(input_text, target_language)
            return render(request, 'translation_result.html', {'translation': translation})
        else:
            return HttpResponse('No text provided.')

    return render(request, 'index.html')

def translate_text(text, target_language):
    url = f"https://api.mymemory.translated.net/get?q={text}&langpair=en|{target_language}"
    response = requests.get(url)
    data = response.json()
    return data['responseData']['translatedText']






