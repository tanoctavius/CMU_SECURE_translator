from src.translator import translate_content
# comment

def test_german():
    is_english, translated_content = translate_content("Hier ist dein erstes Beispiel.")
    assert is_english == False
    assert translated_content == "Here is your first example."

def test_french():
    is_english, translated_content = translate_content("Aujourd'hui, il fait très beau.")
    assert is_english == False
    assert translated_content == "Today, the weather is very nice."

def test_czech():
    is_english, translated_content = translate_content("С днём рождения! Желаю тебе счастья, здоровья, успехов в работе и семейного благополучия. Пусть твои мечты сбываются, и каждый новый день приносит радость и вдохновение.")
    assert is_english == False
    assert translated_content == "Happy birthday! I wish you happiness, health, success at work, and family well-being. May your dreams come true, and may each new day bring joy and inspiration."

def test_japanese():
    is_english, translated_content = translate_content("今日は晴れて、気持ちの良い天気です。友達と一緒に公園でピクニックをする予定です。")
    assert is_english == False
    assert translated_content == "Today is sunny and the weather feels great. I plan to have a picnic in the park with friends."

def test_portuguese():
    is_english, translated_content = translate_content("A educação é um direito fundamental de todos, e garantir que todas as crianças tenham acesso a uma educação de qualidade é essencial para o futuro da sociedade.")
    assert is_english == False
    assert translated_content == "Education is a fundamental right for everyone, and ensuring that all children have access to quality education is essential for the future of society."

def test_italian():
    is_english, translated_content = translate_content("Vorrei ringraziarti per tutto l'aiuto che mi hai offerto durante questi mesi difficili. Non avrei potuto farcela senza il tuo sostegno costante.")
    assert is_english == False
    assert translated_content == "I would like to thank you for all the help you have given me during these difficult months. I couldn't have made it without your constant support."

def test_chinese():
    is_english, translated_content = translate_content("这是你完成任务后的奖励。")
    assert is_english == False
    assert translated_content == "This is your reward for completing the task."

def test_spanish():
    is_english, translated_content = translate_content("¿Cómo estás? Espero que estés bien.")
    assert is_english == False
    assert translated_content == "How are you? I hope you are well."

def test_spanish_2():
    is_english, translated_content = translate_content("Este proyecto tiene un gran potencial para cambiar la forma en que abordamos la sostenibilidad en nuestras comunidades, y espero que podamos trabajar juntos para llevarlo adelante.")
    assert is_english == False
    assert translated_content == "This project has great potential to change how we approach sustainability in our communities, and I hope we can work together to move it forward."

def test_french_2():
    is_english, translated_content = translate_content("Il y a des moments dans la vie où il est important de faire une pause et de réfléchir aux choix que nous avons faits et aux directions que nous voulons prendre.")
    assert is_english == False
    assert translated_content == "There are moments in life when it is important to pause and reflect on the choices we have made and the directions we want to take."

def test_llm_normal_response():
    is_english, translated_content = translate_content("Hello, this is a normal message.")
    assert is_english == True
    assert translated_content == "Hello, this is a normal message."

def test_llm_gibberish_response():
    is_english, translated_content = translate_content("asdfghjkl")
    assert is_english == True
    assert translated_content == "asdfghjkl"
