from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import json
import base64
import os
from worker import speech_to_text, text_to_speech, openai_process_message

# Initialize Flask application
app = Flask(__name__)
CORS(app, origins="*")

@app.route('/', methods=['GET'])
def index():
    """
    Main route that serves the HTML interface
    Returns: Rendered HTML template
    """
    return render_template('index.html')

@app.route('/speech-to-text', methods=['POST'])
def speech_to_text_route():
    """
    API endpoint to convert speech to text
    Accepts: Binary audio data in request body
    Returns: JSON response with transcribed text
    """
    print("Processing speech-to-text request...")
    
    # Extract audio binary data from request
    audio_binary = request.data
    
    # Convert speech to text using Watson STT
    text = speech_to_text(audio_binary)
    
    # Create JSON response
    response = app.response_class(
        response=json.dumps({'text': text}),
        status=200,
        mimetype='application/json'
    )
    
    print(f"Speech-to-text response: {response.data}")
    return response

@app.route('/process-message', methods=['POST'])
def process_message_route():
    """
    API endpoint to process user message and return AI response
    Accepts: JSON with userMessage and voice preference
    Returns: JSON with text and audio response
    """
    print("Processing message...")
    
    # Extract user message and voice preference from request
    user_message = request.json['userMessage']
    voice = request.json['voice']
    
    print(f"User message: {user_message}")
    print(f"Selected voice: {voice}")
    
    # Process message through OpenAI GPT-3
    openai_response_text = openai_process_message(user_message)
    
    # Clean response text (remove empty lines)
    openai_response_text = os.linesep.join([
        line for line in openai_response_text.splitlines() if line.strip()
    ])
    
    # Convert response to speech using Watson TTS
    openai_response_speech = text_to_speech(openai_response_text, voice)
    
    # Encode audio response to base64 for JSON transmission
    openai_response_speech_b64 = base64.b64encode(
        openai_response_speech
    ).decode('utf-8')
    
    # Create JSON response with both text and audio
    response = app.response_class(
        response=json.dumps({
            "openaiResponseText": openai_response_text,
            "openaiResponseSpeech": openai_response_speech_b64
        }),
        status=200,
        mimetype='application/json'
    )
    
    print("Message processed successfully")
    return response

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    print("Starting Voice Assistant Server...")
    print("Server running on http://0.0.0.0:8000")
    app.run(host='0.0.0.0', port=8000, debug=False)
