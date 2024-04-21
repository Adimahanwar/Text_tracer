from django.shortcuts import render, redirect
from .models import Sentence
from language_tool_python import LanguageTool
import enchant
import spacy

def sentence_input(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        improved_text, entities = perform_sentence_improvement(text)
        Sentence.objects.create(text=text, improved_text=improved_text)
        return redirect('results')
    return render(request, 'input.html')

def sentence_results(request):
    sentences = Sentence.objects.all()
    return render(request, 'result1.html', {'sentences': sentences})

def perform_sentence_improvement(text):
    tool = LanguageTool('en-US')
    matches = tool.check(text)
    improved_text = tool.correct(text)

    # Spell checking using pyenchant
    spell_checker = enchant.Dict("en_US")
    corrected_text = []
    words = improved_text.split()
    for word in words:
        if not spell_checker.check(word):
            suggestions = spell_checker.suggest(word)
            if suggestions:
                corrected_word = suggestions[0]  # Use the first suggestion
                corrected_text.append(corrected_word)
            else:
                corrected_text.append(word)
        else:
            corrected_text.append(word)

    improved_text = ' '.join(corrected_text)

    # NER using spaCy
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(improved_text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    print("Named Entities:", entities)

    return improved_text, entities


