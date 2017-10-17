

from googletrans import Translator

translator = Translator()
print(translator.translate('श्रीमती इन्‍द्रा',dest='en').text)
#print(translator.detect('One morning I shot an elephant in my pajamas. How he got into my pajamas I"ll never know.'))