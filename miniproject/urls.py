"""
URL configuration for miniproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from miniproject import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.conf import settings # new
from  django.conf.urls.static import static #new



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('extraction/',views.extract_text, name='extract_text'),
    path('ocrapp/', include('ocrapp.urls')),
    path('accounts/', include('allauth.urls')),
    path('translation/', include('translation.urls')),
    path('sentence/', include('grammar_check.urls')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)





# 836535011694-gfsdjni5e4eik8s23qfsira9anifh01j.apps.googleusercontent.com - client id 
#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 - cliet key 

# fbad2db3ee339fdd7d2a17cbd215f9f278c0c921 - client key 
# 15bd147a206093b7951f

#gBAN1M9RumAoCti4 - client sc
# 77dlw5ev20z78g - id 