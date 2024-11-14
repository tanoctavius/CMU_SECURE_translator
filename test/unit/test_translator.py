# from src.translator import * 
import ipytest
import pytest
from unittest.mock import patch
import unittest
from src.translator import *

# def test_chinese():
#     is_english, translated_content = translate_content("这是一条中文消息")
#     assert is_english == False
#     assert translated_content == "This is a Chinese message"

# def test_llm_normal_response():
#     pass

# def test_llm_gibberish_response():
#     pass

class MockMessage:
    def __init__(self, content):
        self.content = content

class MockChoice:
    def __init__(self, content):
        self.message = MockMessage(content)

class MockResponse:
    def __init__(self, content):
        self.choices = [MockChoice(content)]

class TestQueryLLMRobust(unittest.TestCase):
    # Added: need to define a class comparison function for assertEqual to work
    def __eq__(self, other):
        return self.is_english == other.is_english and self.translation == other.translation

    @patch.object(client.chat.completions, 'create')
    def test_unexpected_format(self, mock_create):
        # LLM returns output in unexpected format
        mock_create.return_value = MockResponse(1000000)
        result = translate_content("This is an English sentence.")
        self.assertEqual(result, (False, ""), "Should return default value when LLM output is unexpected")

    @patch.object(client.chat.completions, 'create')
    def test_error_message(self, mock_create):
        # LLM returns an error message
        mock_create.return_value = MockResponse(TypeError("yadayada"))
        result = translate_content("This is an English sentence.")
        self.assertEqual(result, (False, ""), "Should return default value when LLM output is an error message")

    @patch.object(client.chat.completions, 'create')
    def test_empty_response(self, mock_create):
        # LLM returns an empty string
        mock_create.return_value = MockResponse("")
        result = translate_content("This is an English sentence.")
        self.assertEqual(result, (False, ""), "Should return default value when LLM output is empty")

    @patch.object(client.chat.completions, 'create')
    def test_api_exception(self, mock_create):
        # LLM API raises an exception
        mock_create.side_effect = Exception("API error")
        result = translate_content("This is an English sentence.")
        self.assertEqual(result, (False, ""), "Should return default value when API raises an exception")


ipytest.run('-vv')
