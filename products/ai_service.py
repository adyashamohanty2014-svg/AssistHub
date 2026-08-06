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
def build_prompt(question, devices, intent):

    device_list = ""

    for device in devices:
        device_list += f"""
Name: {device.name}
Brand: {device.brand}
Description: {device.description}
Price: ₹{device.price}

"""

    if intent == "recommendation":
        role = """
You are AssistHub AI.

Recommend ONLY products from the AssistHub database.

Recommend only from the products listed below.
Explain why each product is suitable.
Never invent products.
"""

    elif intent == "explanation":
        role = """
You are AssistHub AI.

Explain assistive technologies in simple language.

If relevant products exist below, mention them.
"""

    elif intent == "website_help":
        role = """
You are AssistHub AI.

Help users use the AssistHub website.

Answer questions related to:
- Login
- Register
- Wishlist
- Cart
- Compare
- Profile
- Ordering
"""

    else:
        role = """
You are AssistHub AI.

Answer politely.

Only answer questions related to AssistHub or assistive technology.
"""

    prompt = f"""
{role}

User Question:

{question}

Available AssistHub Products:

{device_list}

Rules:

1. Recommend ONLY products listed above.

2. Never invent products.

3. If no matching products exist, politely say so.

4. Keep answers under 200 words.

5. Be friendly and easy to understand.
"""

    return prompt