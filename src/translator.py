import os
from openai import AzureOpenAI

env_api_key = os.environ.get('API_KEY')

if not env_api_key:
    raise ValueError("Environment variable API_KEY is not set.")

client = AzureOpenAI(
    api_key=os.getenv("API_KEY"),
    api_version="2024-02-15-preview",
    azure_endpoint="https://project-4.openai.azure.com/"
)

def get_translation(post: str) -> str:
    context = "You are a helpful assistant specialized in translating text. Translate the following text to English."
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": context
            },
            {
                "role": "user",
                "content": post
            }
        ]
    )
    return response.choices[0].message.content

def get_language(post: str) -> str:
    context = "You are an assistant that identifies the language of the provided text. Specify the language of the following text. Answer in 1 word, with just the name of the language (use the English name)."
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": context
            },
            {
                "role": "user",
                "content": post
            }
        ]
    )
    return response.choices[0].message.content


def translate_content(content: str) -> tuple[bool, str]:
    try:
        detected_language = get_language(content)

        # Check if detected language is in the expected format (a single word)
        if not isinstance(detected_language, str) or " " in detected_language.strip():
            raise ValueError("Unexpected language output format: Expected a single word.")

        if detected_language.lower() == "english":
            return (True, content)

        translated_text = get_translation(content)

        # Verify translation output format (should be a non-empty string)
        if not isinstance(translated_text, str) or len(translated_text.strip()) == 0:
            raise ValueError("Unexpected translation output format: Expected non-empty text.")

        return (False, translated_text)

    except Exception as e:
        # Log the error and respond with a safe fallback to avoid breaking NodeBB
        print(f"Error in LLM response handling: {e}")
        return (True, "Sorry, translation is temporarily unavailable.")
