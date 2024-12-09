# Import the package
from googletrans import Translator

# Create a Translator object
translator = Translator(dest='en')

# Use the translate method to translate the text
russian_text = "Моя семья живет в России."
english_translation = translator.translate(russian_text, dest='en')

# Print the translated text
print(english_translation.text)
# Output: My family lives in Russia.
