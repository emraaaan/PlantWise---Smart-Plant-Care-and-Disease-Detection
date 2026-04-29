from django.db import models
from django.conf import settings

class DiagnosisResult(models.Model):

    SEVERITY_CHOICES = [
        ('healthy', 'Healthy'),
        ('mild', 'Mild'),
        ('severe', 'Severe'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='diagnoses'
    )
    image = models.ImageField(upload_to='diagnoses/')
    plant_name = models.CharField(max_length=200, blank=True)
    disease_name = models.CharField(max_length=200, blank=True)
    confidence = models.FloatField(default=0.0)
    description = models.TextField(blank=True)
    treatment = models.TextField(blank=True)
    is_healthy = models.BooleanField(default=False)
    severity = models.CharField(max_length=20, choices=SEVERITY_CHOICES, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} — {self.disease_name or 'Unknown'} ({self.created_at.date()})"

    class Meta:
        ordering = ['-created_at']