from django import forms
from .models import DiagnosisResult


class DiagnosisForm(forms.ModelForm):
    image = forms.ImageField(
        label="Plant photo",
        help_text="Upload a clear photo of the affected leaf or stem.",
        widget=forms.ClearableFileInput(
            attrs={"accept": "image/*"}
        )
    )

    class Meta:
        model = DiagnosisResult
        fields = ["image"]
