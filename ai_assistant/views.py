from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse

from products.ai_helper import detect_intent, search_devices
from products.ai_service import build_prompt, generate_ai_response


def _answer_question(question):
    intent = detect_intent(question)
    devices = search_devices(question)
    prompt = build_prompt(question, devices, intent)
    response = generate_ai_response(prompt)
    return response, devices


def ask_ai(request):
    response = None
    question = ""
    devices = []

    if request.method == "POST":
        question = request.POST.get("question")

        response, devices = _answer_question(question)

    return render(request, "ai_assistant/ask_ai.html", {
        "question": question,
        "response": response,
        "devices": devices,
    })


def ask_ai_api(request):
    if request.method != "POST":
        return JsonResponse(
            {"error": "This endpoint accepts POST requests only."},
            status=405,
        )

    question = request.POST.get("question", "").strip()
    if not question:
        return JsonResponse(
            {"error": "Please enter a question first."},
            status=400,
        )

    try:
        response, devices = _answer_question(question)
    except Exception:
        return JsonResponse(
            {"error": "Sorry, I'm having trouble connecting right now. Please try again."},
            status=502,
        )

    return JsonResponse({
        "response": response,
        "devices": [
            {
                "name": device.name,
                "brand": device.brand,
                "price": str(device.price),
                "image": device.image.url if device.image else "",
                "detail_url": reverse("device_detail", args=[device.id]),
            }
            for device in devices
        ],
    })