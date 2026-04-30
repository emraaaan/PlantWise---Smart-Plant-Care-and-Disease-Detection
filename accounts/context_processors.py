from django.conf import settings


def google_oauth(request):
    google_profile_picture_url = ""

    if request.user.is_authenticated:
        social_account = request.user.socialaccount_set.filter(provider="google").first()
        if social_account:
            google_profile_picture_url = social_account.extra_data.get("picture", "")

    return {
        "google_oauth_configured": bool(
            settings.GOOGLE_OAUTH_CLIENT_ID and settings.GOOGLE_OAUTH_CLIENT_SECRET
        ),
        "google_profile_picture_url": google_profile_picture_url,
    }
