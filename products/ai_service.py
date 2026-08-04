from google import genai
from google.genai.errors import ServerError
from django.conf import settings

client = genai.Client(api_key=settings.GEMINI_API_KEY)


def generate_ai_response(prompt):
    try:
        response = client.models.generate_content(
            model="models/gemini-flash-latest",
            contents=prompt
        )
        return response.text

    except ServerError:
        return (
            "AssistHub AI is currently experiencing high traffic. "
            "Please try again in a few moments."
        )

    except Exception as e:
        print("Gemini Error:", e)
        raise


def build_prompt(question, devices):

    device_list = ""

    for device in devices:
        device_list += f"""
Name: {device.name}
Brand: {device.brand}
Description: {device.description}
Price: ₹{device.price}

"""

    prompt = f"""
You are AssistHub AI.

You are an AI assistant built ONLY for AssistHub.

You can answer questions about:

- Assistive Technology
- Accessibility
- Disabilities
- Wheelchairs
- Smart Canes
- Braille
- Hearing Aids
- Screen Readers
- Mobility Devices
- AssistHub products

User Question:

{question}

Available AssistHub Products:

{device_list}

Rules:

1. Recommend ONLY products listed above.

2. Never invent products.

3. Explain why each product is suitable.

4. If no matching products are available,
politely tell the user to contact AssistHub Support.

5. Keep answers under 200 words.

6. Never answer unrelated questions.

"""

    return prompt