from src.translator import translate_content

def test_german():
    is_english, translated_content = translate_content("Willkommen in unserem neuen System.")
    assert is_english == False
    assert translated_content == "Welcome to our new system."

def test_french():
    is_english, translated_content = translate_content("Je suis ravi de vous rencontrer aujourd'hui.")
    assert is_english == False
    assert translated_content == "I am delighted to meet you today."

def test_czech():
    is_english, translated_content = translate_content("Děkujeme za váš zájem o náš produkt.")
    assert is_english == False
    assert translated_content == "Thank you for your interest in our product."

def test_japanese():
    is_english, translated_content = translate_content("新しいプロジェクトについて話したいと思います。")
    assert is_english == False
    assert translated_content == "I would like to talk about the new project."

def test_portuguese():
    is_english, translated_content = translate_content("Vamos trabalhar juntos para alcançar nossos objetivos.")
    assert is_english == False
    assert translated_content == "Let's work together to achieve our goals."

def test_italian():
    is_english, translated_content = translate_content("La riunione si terrà domani alle 10 del mattino.")
    assert is_english == False
    assert translated_content == "The meeting will be held tomorrow at 10 AM."

def test_chinese():
    is_english, translated_content = translate_content("这个决定对我们的未来非常重要。")
    assert is_english == False
    assert translated_content == "This decision is very important for our future."

def test_spanish():
    is_english, translated_content = translate_content("Espero que podamos colaborar en este proyecto pronto.")
    assert is_english == False
    assert translated_content == "I hope we can collaborate on this project soon."

def test_spanish_2():
    is_english, translated_content = translate_content("Trabajemos juntos para resolver este problema lo antes posible.")
    assert is_english == False
    assert translated_content == "Let's work together to solve this problem as soon as possible."

def test_french_2():
    is_english, translated_content = translate_content("Prenons un moment pour discuter de la stratégie à adopter.")
    assert is_english == False
    assert translated_content == "Let's take a moment to discuss the strategy to adopt."

def test_llm_normal_response():
    is_english, translated_content = translate_content("This is a simple test message.")
    assert is_english == True
    assert translated_content == "This is a simple test message."

def test_llm_gibberish_response():
    is_english, translated_content = translate_content("qwertyuiop")
    assert is_english == True
    assert translated_content == "qwertyuiop"
