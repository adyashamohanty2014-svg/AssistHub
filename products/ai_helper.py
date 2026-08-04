import re
from .models import Device
from django.db.models import Q
RECOMMENDATION_KEYWORDS = [
    "best",
    "recommend",
    "which device",
    "wheelchair",
    "smart cane",
    "hearing aid",
    "screen reader",
    "braille",
    "walker",
    "mobility",
    "blind",
    "visually impaired",
    "low vision",
    "deaf",
    "hearing loss",
    "arthritis",
    "parkinson",
    "autism",
    "cerebral palsy"
]

EXPLANATION_KEYWORDS = [
    "what is",
    "explain",
    "how does",
    "working of",
    "uses of"
]

WEBSITE_KEYWORDS = [
    "order",
    "wishlist",
    "cart",
    "compare",
    "profile",
    "login",
    "register",
    "contact"
]


def detect_intent(question):
    question = question.lower()

    for keyword in WEBSITE_KEYWORDS:
        if keyword in question:
            return "website"

    for keyword in EXPLANATION_KEYWORDS:
        if keyword in question:
            return "explanation"

    for keyword in RECOMMENDATION_KEYWORDS:
        if keyword in question:
            return "recommendation"

    return "unknown"
def search_devices(question):
    question = question.lower()

    keywords = question.split()

    query = Q()

    for word in keywords:
        query |= Q(tags__icontains=word)
        query |= Q(name__icontains=word)
        query |= Q(description__icontains=word)

    devices = Device.objects.filter(query).distinct()[:5]

    return devices