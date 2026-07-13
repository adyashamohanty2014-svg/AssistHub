from django.shortcuts import render

def ask_ai(request):
    response = None
    question = ""

    if request.method == "POST":
        question = request.POST.get("question")

        response = (
            "Thank you for your question! "
            "AssistHub AI is currently under development. "
            "Soon I will be able to answer questions about assistive technologies and accessibility."
        )

    return render(request, "ai_assistant/ask_ai.html", {
        "question": question,
        "response": response
    })
