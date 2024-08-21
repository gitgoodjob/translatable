import streamlit as st
pip install google-cloud-translate
st.title('Translatable')

st.write('This uses ai to translate text.')
import streamlit as st
from google.cloud import translate_v2 as translate

# Initialize the Google Translate client
def get_translate_client():
    return translate.Client()

# Function to fetch all supported languages
def get_supported_languages(target_language="en"):
    client = get_translate_client()
    languages = client.get_languages(target_language=target_language)
    return {lang['name']: lang['language'] for lang in languages}

# Function to detect the language of the text using Google Translate
def detect_language(text):
    client = get_translate_client()
    result = client.detect_language(text)
    return result['language']

# Function to translate the text using Google Translate
def translate_text(text, target_language, source_language=None):
    client = get_translate_client()

    # If source_language is not provided, auto-detect it
    if source_language == "auto":
        source_language = detect_language(text)

    translation = client.translate(text, target_language=target_language, source_language=source_language)
    return translation['translatedText']

# Streamlit User Interface
st.title("Comprehensive Language Translation Chatbot with Google Translate")

# Fetch supported languages
languages = get_supported_languages()

# User inputs
input_text = st.text_area("Enter text to translate:")

# Adding "auto" option for source language detection
source_language = st.selectbox("Select source language:", ["auto"] + list(languages.keys()))

# Select target language
target_language = st.selectbox("Select target language:", list(languages.keys()))

if st.button("Translate"):
    source_language_code = "auto" if source_language == "auto" else languages[source_language]
    target_language_code = languages[target_language]
    
    translated_text = translate_text(input_text, target_language_code, source_language_code)
    st.write("Translated Text:", translated_text)


