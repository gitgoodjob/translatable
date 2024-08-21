import streamlit as st

st.title('Translatable')

st.write('This uses ai to translate text.')
import requests
import streamlit as st

# Function to call the Text Translator API
def translate_text(text, source_language, target_language):
    url = "https://text-translator2.p.rapidapi.com/translate"

    headers = {
        "Content-Type": "multipart/form-data",
        "x-rapidapi-host": "text-translator2.p.rapidapi.com",
        "x-rapidapi-key": "313ce963c1msh273e89113e2f624p199a36jsn2112424f9549"
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
st.title("Basic Language Translation Chatbot")

# User inputs
input_text = st.text_area("Enter text to translate:")
source_language = st.selectbox("Select source language:", ["en", "fr", "es", "de", "zh", "id"])
target_language = st.selectbox("Select target language:", ["id", "en", "fr", "es", "de", "zh"])

if st.button("Translate"):
    translated_text = translate_text(input_text, source_language, target_language)
    st.write("Translated Text:", translated_text)
