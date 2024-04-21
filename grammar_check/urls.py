from django.urls import path
from grammar_check.views import sentence_input, sentence_results

urlpatterns = [
    path('sentence_input/', sentence_input, name='sentence_input'),
    path('results/', sentence_results, name='results'),
]
