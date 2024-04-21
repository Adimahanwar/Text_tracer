from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image
import pytesseract
import openai
from django.shortcuts import render, redirect
from PIL import Image
import pytesseract
from django.contrib.auth.decorators import login_required
from PIL import Image
import pytesseract
import cv2
import numpy as np
from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from PIL import Image
import pytesseract
import requests
from django.shortcuts import render
from PIL import Image
import numpy as np
import requests
from io import BytesIO
from django.shortcuts import render
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from io import BytesIO
import requests
from django.shortcuts import render
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from PIL import Image
import requests
from django.shortcuts import render
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Ensure using the 'Agg' backend for Matplotlib
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from PIL import Image
import requests
from django.shortcuts import render
from django.http import HttpResponse
import matplotlib.pyplot as plt
import numpy as np
from django.conf import settings
import os










@login_required

def extract_text(request):
    if request.method == 'POST':
        uploaded_image = request.FILES.get('image')

        if not uploaded_image:
            return render(request, 'upload.html', {'error': 'No image uploaded. Please upload an image file.'})
        
        # Save the image to the media directory and generate a URL to access it
        fs = FileSystemStorage()
        filename = fs.save(uploaded_image.name, uploaded_image)
        uploaded_image_url = fs.url(filename)

        # Open the uploaded image for text extraction
        img = Image.open(uploaded_image)
        text = pytesseract.image_to_string(img)
        
        return render(request, 'result.html', {
            'text': text,
            'image_url': uploaded_image_url
        })

    return render(request, 'upload.html')






def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
