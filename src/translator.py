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
    context = "Translate the following text to English. Imagine that you are a helpful assistant that translates non-English posts into English."
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
    context = "You are a helpful assistant that classifies the language of the text. Give the response as a single English word of the language}." 
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
        # Detect the language of the content
        detected_language = get_language(content)
        _validate_detected_language(detected_language)

        if detected_language.lower() == "english":
            return True, content

        # Translate content if not in English
        translated_text = get_translation(content)
        _validate_translated_text(translated_text)

        return False, translated_text

    except Exception as e:
        # Log the error and provide a fallback response
        print(f"Error in translation service: {e}")
        return True, "Sorry, translation is temporarily unavailable."

def _validate_detected_language(detected_language: str) -> None:
    #Validates the format of the detected language.
    if not isinstance(detected_language, str) or " " in detected_language.strip():
        raise ValueError("Unexpected language output format: Expected a single word.")

def _validate_translated_text(translated_text: str) -> None:
    #Validates the format of the translated text.
    if not isinstance(translated_text, str) or not translated_text.strip():
        raise ValueError("Unexpected translation output format: Expected non-empty text.")
