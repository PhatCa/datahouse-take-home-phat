from django.urls import path
from .views import ScoringView


urlpatterns = [
    path("", ScoringView.as_view(), name="scoring-applicant")
]
