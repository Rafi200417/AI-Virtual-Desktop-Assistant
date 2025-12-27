from googletrans import Translator

def translategl(query, target_lang="te"):
    try:
        translator = Translator()
        translated = translator.translate(query, dest=target_lang)
        return translated.text
    except Exception as e:
        print(f"[ERROR] Unable to translate: {e}")
        return None

text = translategl("query")
print(text)
