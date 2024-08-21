import streamlit as st


st.title('Translatable')

st.write('This uses ai to translate text.')
import streamlit as st
from google.cloud import translate_v2 as translate
from google.oauth2 import service_account

# Initialize the Google Translate API client
def init_translate_client():
    credentials = service_account.Credentials.from_service_account_info(st.secrets["gcp_service_account"])
    client = translate.Client(credentials=credentials)
    return client

@st.cache_data(show_spinner=False)
def detect_language_and_translate(text, target_language, translate_client):
    # Detect the language of the input text
    detection = translate_client.detect_language(text)
    source_language = detection['language']
    
    # Only perform translation if source and target languages are different
    if source_language != target_language:
        translation = translate_client.translate(text, target_language=target_language, source_language=source_language)
        return source_language, translation['translatedText']
    else:
        return source_language, text

# Main Streamlit App
def main():
    st.title("Basic Language Translation Chatbot")
    
    # Initialize the translation client
    translate_client = init_translate_client()
    
    # Input field for user text
    user_input = st.text_input("Enter the text you want to translate:")
    
    # Target language selection
    target_language = st.selectbox("Select target language:", ['es', 'fr', 'de', 'hi', 'id', 'zh', 'ja', 'ru', 'ar', 'sanskrit'])
    
    # Process the translation only if there's user input
    if user_input:
        # Perform language detection and translation
        source_language, translated_text = detect_language_and_translate(user_input, target_language, translate_client)
        
        # Display the results
        st.write(f"**Detected Source Language**: {source_language}")
        st.write(f"**Translated Text**: {translated_text}")
    else:
        st.warning("Please enter text to translate.")

if __name__ == "__main__":
    main()


