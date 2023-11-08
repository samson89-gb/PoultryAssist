from django.shortcuts import render
import difflib
from .models import Disease, Symptom, Solution
from .forms import SymptomInputForm


def identify_disease(request):
    if request.method == 'post':
        form = SymptomInputForm(request.POST)
        if form.is_valid():
            # process the data
            symptoms = form.cleaned_data['symptoms']

            # Split users input symptoms int a list for comparison
            input_symptoms = [symptom.strip() for symptom in symptoms.split('\n') if symptom.strip()]

            stored_symptoms = Symptom.objects.values_list('name', flat=True)

            best_match = 0
            matching_disease = None

            for disease in Disease.objects.all():
                for stored_symptoms in stored_symptoms:
                    match = difflib.SequenceMatcher(None, symptoms, stored_symptoms).ratio() * 100
                    if match > best_match:
                        best_match = match
                        matching_disease = disease

            if best_match >= 75 and matching_disease:
                solution = Solution.objects.get(disease=matching_disease)
                return render(request, 'result.htm', {'disease': matching_disease, 'solution': solution})

            # FOR DISEASE IDENTIFICATION LOGIC

    else:
        form = SymptomInputForm()

    return render(request, 'DiseaseIdentifier.html', {'form': form})

# Create your views here.
