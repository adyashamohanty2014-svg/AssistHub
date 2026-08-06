import re
from .models import Device, Category
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


def detect_intent(user_query):
    query = user_query.lower()

    if any(word in query for word in RECOMMENDATION_KEYWORDS):
        return "recommendation"

    elif any(word in query for word in EXPLANATION_KEYWORDS):
        return "explanation"

    elif any(word in query for word in WEBSITE_KEYWORDS):
        return "website_help"

    else:
        return "general"

def search_devices(question):
    STOP_WORDS = {
    "a", "an", "the", "is", "are", "of", "for", "to",
    "and", "or", "i", "need", "want", "recommend",
    "best", "please", "me", "my", "device", "devices"
}
    question = question.lower()

    # -------- STEP 1 : Search by Category --------
    categories = Category.objects.all()

    for category in categories:
        if category.name.lower() in question:
            devices = Device.objects.filter(category=category)

            if devices.exists():
                return devices[:5]

    # -------- STEP 2 : Search by Tags --------
    keywords = [
    word for word in re.findall(r"\w+", question)
    if len(word) > 2 and word not in STOP_WORDS
]

    for word in keywords:
        devices = Device.objects.filter(tags__icontains=word)

        if devices.exists():
            return devices[:5]

    # -------- STEP 3 : Search by Name --------
    for word in keywords:
        devices = Device.objects.filter(name__icontains=word)

        if devices.exists():
            return devices[:5]

    # -------- STEP 4 : Search by Description --------
    query = Q()

    for word in keywords:
        query |= Q(description__icontains=word)

    return Device.objects.filter(query).distinct()[:5]