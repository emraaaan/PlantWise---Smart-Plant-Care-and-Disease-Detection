from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import DiagnosisForm
from .models import DiagnosisResult
from .utils import analyze_plant

@login_required
def diagnose_plant(request):
    if request.method == "POST":
        form = DiagnosisForm(request.POST, request.FILES)
        if form.is_valid():
            diagnosis = form.save(commit=False)
            diagnosis.user = request.user
            diagnosis.save()

            api_error = False
            api_error_message = None
            try:
                api_response = analyze_plant(diagnosis.image.path)
            except Exception as exc:
                api_response = {}
                api_error = True
                api_error_message = str(exc)

            try:
                result = api_response.get("result", {})
                disease_info = result.get("disease", {})
                suggestions = disease_info.get("suggestions", [])

                if suggestions:
                    top = suggestions[0]

                    diagnosis.disease_name = top.get("name", "")
                    diagnosis.confidence = round(top.get("probability", 0) * 100, 2)

                    details = top.get("details") or {}
                    description = details.get("description", "")
                    if isinstance(description, dict):
                        description = description.get("value", "")
                    diagnosis.description = description or ""

                    treatment = details.get("treatment", "")
                    if isinstance(treatment, dict):
                        treatment = treatment.get("value", "")
                    diagnosis.treatment = treatment or ""

                    severity = details.get("severity", "") or top.get("severity", "")
                    if isinstance(severity, dict):
                        severity = severity.get("value", "")
                    diagnosis.severity = severity or ""

                    diagnosis.is_healthy = (
                        diagnosis.disease_name.lower() == "healthy"
                    )

                plant = result.get("plant", {})
                diagnosis.plant_name = plant.get("name", "")

            except Exception:
                diagnosis.disease_name = "Unknown"
                diagnosis.confidence = 0
                diagnosis.is_healthy = False

            diagnosis.save()
            if api_error:
                if api_error_message and "KINDWISE_API_KEY" in api_error_message:
                    messages.warning(
                        request,
                        "Detection isn't configured yet. Add a KINDWISE_API_KEY "
                        "to your environment and try again."
                    )
                else:
                    messages.warning(
                        request,
                        "We couldn't reach the detection service right now. "
                        "Your upload was saved, but the analysis may be incomplete."
                    )
            return redirect("detector:diagnosis_result", diagnosis.id)
    else:
        form = DiagnosisForm()

    return render(request, "detector/diagnose.html", {"form": form})

@login_required
def diagnosis_result(request, pk):
    diagnosis = get_object_or_404(
        DiagnosisResult,
        pk=pk,
        user=request.user
    )
    return render(request, "detector/result.html", {"diagnosis": diagnosis})

@login_required
def history(request):
    diagnoses = (
        DiagnosisResult.objects
        .filter(user=request.user)
        .order_by("-created_at")
    )
    return render(request, "detector/history.html", {"diagnoses": diagnoses})
