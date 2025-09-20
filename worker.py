#AI Services Integration

from openai import OpenAI
import requests
import json

# Initialize OpenAI client
openai_client = OpenAI()

def speech_to_text(audio_binary):
    """
    Convert speech audio to text using Watson Speech-to-Text
    
    Args:
        audio_binary: Binary audio data
        
    Returns:
        str: Transcribed text or 'null' if no speech detected
    """
    # Watson Speech-to-Text API configuration
    base_url = 'https://sn-watson-stt.labs.skills.network'
    api_url = base_url + '/speech-to-text/api/v1/recognize'
    
    # API parameters
    params = {
        'model': 'en-US_Multimedia',
    }
    
    try:
        # Send POST request to Watson STT
        response = requests.post(
            api_url, 
            params=params, 
            data=audio_binary,
            timeout=30
        ).json()
        
        print(f'Speech-to-text API response: {response}')
        
        # Extract text from response
        text = 'null'
        if response.get('results') and len(response['results']) > 0:
            alternatives = response['results'][0].get('alternatives', [])
            if alternatives:
                text = alternatives[0].get('transcript', 'null')
                print(f'Recognized text: {text}')
        
        return text
        
    except Exception as e:
        print(f'Error in speech_to_text: {e}')
        return 'null'

def openai_process_message(user_message):
    """
    Process user message using OpenAI GPT-3
    
    Args:
        user_message: User's text message
        
    Returns:
        str: AI-generated response
    """
    # System prompt to define assistant behavior
    system_prompt = """Act like a personal assistant. You can respond to questions, 
    translate sentences, summarize news, and give recommendations. Be helpful, 
    friendly, and concise in your responses."""
    
    try:
        # Call OpenAI Chat Completions API
        response = openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            max_tokens=4000,
            temperature=0.7
        )
        
        print(f"OpenAI API response: {response}")
        
        # Extract response text
        response_text = response.choices[0].message.content
        return response_text
        
    except Exception as e:
        print(f'Error in openai_process_message: {e}')
        return "I'm sorry, I couldn't process your request right now. Please try again."

def text_to_speech(text, voice=""):
    """
    Convert text to speech using Watson Text-to-Speech
    
    Args:
        text: Text to convert to speech
        voice: Voice preference (optional)
        
    Returns:
        bytes: Audio data in WAV format
    """
    # Watson Text-to-Speech API configuration
    base_url = 'https://sn-watson-tts.labs.skills.network'
    api_url = base_url + '/text-to-speech/api/v1/synthesize?output=output_text.wav'
    
    # Add voice parameter if specified
    if voice and voice != "default":
        api_url += "&voice=" + voice
    
    # Request headers
    headers = {
        'Accept': 'audio/wav',
        'Content-Type': 'application/json',
    }
    
    # Request body
    json_data = {
        'text': text,
    }
    
    try:
        # Send POST request to Watson TTS
        response = requests.post(
            api_url, 
            headers=headers, 
            json=json_data,
            timeout=30
        )
        
        print(f'Text-to-speech API status: {response.status_code}')
        
        # Return audio content
        return response.content
        
    except Exception as e:
        print(f'Error in text_to_speech: {e}')
        # Return empty audio data on error
        return b''
