from django.shortcuts import render

from products.ai_helper import detect_intent, search_devices
from products.ai_service import build_prompt, generate_ai_response


def ask_ai(request):
    response = None
    question = ""
    devices = []

    if request.method == "POST":
        question = request.POST.get("question")

        # Detect user intent
        intent = detect_intent(question)

        # Search matching devices from database
        devices = search_devices(question)

        # Build AI prompt
        prompt = build_prompt(question, devices)

        # Generate AI response
        response = generate_ai_response(prompt)

    return render(request, "ai_assistant/ask_ai.html", {
        "question": question,
        "response": response,
        "devices": devices,
    })