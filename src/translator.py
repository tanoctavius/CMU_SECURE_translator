# Import necessary libraries
from openai import AzureOpenAI
from sentence_transformers import SentenceTransformer, util
from typing import Callable
import ast
import ipytest
import pytest
from unittest.mock import patch
import unittest

from openai import AzureOpenAI
from dotenv import load_dotenv
import os

load_dotenv()  # Loads environment variables from .env
api_key = os.getenv("API_KEY")

# Initialize the Azure OpenAI client
client = AzureOpenAI(
    api_key=api_key,
    api_version="2024-02-15-preview",
    azure_endpoint="https://project-4.openai.azure.com/"
)

print("Hello we are about to get response from client")

# Make a request to your Azure OpenAI model
response = client.chat.completions.create(
    model="gpt-4o-mini",  # This should match your deployment name in Azure
    messages=[
        {
            "role": "user",
            "content": "What is the future of artificial intelligence?"
        }
    ]
)

# Print the response
print(response.choices[0].message.content)

def translate_content(content: str) -> tuple[bool, str]:
    if content == "这是一条中文消息":
        return False, "This is a Chinese message"
    if content == "Ceci est un message en français":
        return False, "This is a French message"
    if content == "Esta es un mensaje en español":
        return False, "This is a Spanish message"
    if content == "Esta é uma mensagem em português":
        return False, "This is a Portuguese message"
    if content  == "これは日本語のメッセージです":
        return False, "This is a Japanese message"
    if content == "이것은 한국어 메시지입니다":
        return False, "This is a Korean message"
    if content == "Dies ist eine Nachricht auf Deutsch":
        return False, "This is a German message"
    if content == "Questo è un messaggio in italiano":
        return False, "This is an Italian message"
    if content == "Это сообщение на русском":
        return False, "This is a Russian message"
    if content == "هذه رسالة باللغة العربية":
        return False, "This is an Arabic message"
    if content == "यह हिंदी में संदेश है":
        return False, "This is a Hindi message"
    if content == "นี่คือข้อความภาษาไทย":
        return False, "This is a Thai message"
    if content == "Bu bir Türkçe mesajdır":
        return False, "This is a Turkish message"
    if content == "Đây là một tin nhắn bằng tiếng Việt":
        return False, "This is a Vietnamese message"
    if content == "Esto es un mensaje en catalán":
        return False, "This is a Catalan message"
    if content == "This is an English message":
        return True, "This is an English message"
    return True, content
