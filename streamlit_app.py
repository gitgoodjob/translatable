import streamlit as st

st.title('Translatable')

st.write('This uses ai to translate text.')
import requests
import streamlit as st

# Function to detect the language of the text
def detect_language(text):
    url = "https://text-translator2.p.rapidapi.com/detect"

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "x-rapidapi-host": "text-translator2.p.rapidapi.com",
        "x-rapidapi-key": "YOUR_RAPIDAPI_KEY"
    }

    form_data = {
        "text": text
    }

    response = requests.post(url, headers=headers, data=form_data)
    result = response.json()
    
    return result.get('data', {}).get('language', 'en')  # Default to 'en' if detection fails

# Function to call the Text Translator API
def translate_text(text, source_language, target_language):
    # Detect language if source_language is not provided or is 'auto'
    if source_language == "auto":
        source_language = detect_language(text)

    url = "https://text-translator2.p.rapidapi.com/translate"

    headers = {
        "Content-Type": "multipart/form-data",
        "x-rapidapi-host": "text-translator2.p.rapidapi.com",
        "x-rapidapi-key": "YOUR_RAPIDAPI_KEY"
    }

    form_data = {
        "source_language": source_language,
        "target_language": target_language,
        "text": text
    }

    response = requests.post(url, headers=headers, files=form_data)
    result = response.json()
    
    return result.get('data', {}).get('translatedText', 'Translation failed')

# Streamlit User Interface
st.title("Basic Language Translation Chatbot with Auto-Detect")

# User inputs
input_text = st.text_area("Enter text to translate:")
source_language = st.selectbox("Select source language:", ["auto", "en", "fr", "es", "de", "zh", "id"])
target_language = st.selectbox("Select target language:", ["en", "fr", "es", "de", "zh", "id"])

if st.button("Translate"):
    translated_text = translate_text(input_text, source_language, target_language)
    st.write("Translated Text:", translated_text)
