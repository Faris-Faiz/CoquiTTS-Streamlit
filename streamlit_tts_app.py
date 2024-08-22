import streamlit as st
from TTS.api import TTS
import os
import logging
import sys

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize TTS model
@st.cache_resource
def load_tts_model():
    try:
        tts = TTS(model_name="tts_models/en/ljspeech/fast_pitch")
        logger.info("TTS model loaded successfully")
        return tts
    except Exception as e:
        logger.error(f"Error loading TTS model: {str(e)}")
        st.error(f"Failed to load TTS model. Error: {str(e)}")
        return None

# Function to generate audio
def generate_audio(text, tts_model):
    try:
        output_path = "output.wav"
        tts_model.tts_to_file(text=text, file_path=output_path)
        logger.info(f"Audio generated successfully: {output_path}")
        return output_path
    except Exception as e:
        logger.error(f"Error generating audio: {str(e)}")
        st.error(f"Failed to generate audio. Error: {str(e)}")
        return None

# Streamlit UI
st.title("Text-to-Speech with CoquiTTS")

# Load TTS model
tts_model = load_tts_model()

if tts_model:
    # Initialize session state for text input if it doesn't exist
    if 'text_input' not in st.session_state:
        st.session_state.text_input = ""

    # Text input
    text_input = st.text_area("Enter the text you want to convert to speech:", value=st.session_state.text_input, key="text_input")

    # Generate button
    if st.button("Generate Speech"):
        if text_input.strip() == "":
            st.warning("Please enter some text to convert to speech.")
        else:
            with st.spinner("Generating audio..."):
                audio_file = generate_audio(text_input, tts_model)
                if audio_file and os.path.exists(audio_file):
                    st.success("Audio generated successfully!")
                    st.audio(audio_file, format="audio/wav")
                else:
                    st.error("Failed to generate audio. Please try again.")

    # Display some information about the app
    st.markdown("---")
    st.markdown("## About this app")
    st.markdown("This Streamlit application showcases the CoquiTTS package for text-to-speech conversion.")
    st.markdown("It uses the 'tts_models/en/ljspeech/fast_pitch' model to generate high-quality speech from text.")
    st.markdown("Simply enter your text in the box above and click 'Generate Speech' to hear the result!")

    # Display technical information
    st.markdown("---")
    st.markdown("## Technical Information")
    st.markdown(f"- **TTS Model**: tts_models/en/ljspeech/fast_pitch")
    st.markdown(f"- **Python Version**: {'.'.join(map(str, sys.version_info[:3]))}")

    # Note about Torchaudio warning
    st.markdown("---")
    st.markdown("## Note")
    st.markdown("You may see a warning about Torchaudio's I/O functions. This is not a critical error and does not affect the functionality of the app.")

else:
    st.error("Failed to load the TTS model. Please check the logs for more information.")