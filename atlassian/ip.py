from textblob import TextBlob
from googletrans import Translator
translator = Translator()
# translate a spanish text to english text (by default)
translation = translator.translate("안녕 오늘 날씨는 어때")
print(translation.text)

b = TextBlob(translation.text)
b.detect_language()