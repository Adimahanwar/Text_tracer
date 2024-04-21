import pytesseract
from PIL import Image
from django.shortcuts import render, redirect
from .forms import HandwrittenImageForm
from .models import HandwrittenText
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def upload_handwritten_image(request):
    if request.method == 'POST':
        form = HandwrittenImageForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = form.cleaned_data['image']

            # Perform OCR on the uploaded image
            image = Image.open(uploaded_image)
            text = pytesseract.image_to_string(image)

            # Save the result to the database
            HandwrittenText.objects.create(image=uploaded_image, text=text)

            return redirect('show_handwritten_text')

    else:
        form = HandwrittenImageForm()

    return render(request, 'upload1.html', {'form': form})

def show_handwritten_text(request):
    texts = HandwrittenText.objects.all()
    return render(request, 'show_text.html', {'texts': texts})









