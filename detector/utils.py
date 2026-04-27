import base64
import requests
from django.conf import settings

def analyze_plant(image_path):
    if not settings.KINDWISE_API_KEY:
        raise ValueError("KINDWISE_API_KEY is not set")

    headers = {
        "Api-Key": settings.KINDWISE_API_KEY
    }

    details = [
        "common_names",
        "description",
        "treatment",
        "severity",
    ]

    with open(image_path, "rb") as image_file:
        images = [base64.b64encode(image_file.read()).decode("ascii")]

    api_url = settings.KINDWISE_API_URL.rstrip("/") + "/identification"
    response = requests.post(
        api_url,
        headers=headers,
        params={
            "details": ",".join(details),
            "language": "en",
        },
        json={
            "images": images
        },
        timeout=30
    )
    response.raise_for_status()

    return response.json()
