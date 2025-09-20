# voice-assistant-gpt-and-IBM-TTS
Voice Assistant with OpenAI GPT-3 and IBM Watson A comprehensive voice assistant application that combines OpenAI's GPT-3 for intelligent responses, IBM Watson Speech-to-Text for voice recognition, and IBM Watson Text-to-Speech for voice output. 
# Voice Assistant with OpenAI GPT-3 and IBM Watson

A comprehensive voice assistant application that combines OpenAI's GPT-3 for intelligent responses, IBM Watson Speech-to-Text for voice recognition, and IBM Watson Text-to-Speech for voice output.

## 🏗️ Project Structure

```
voice-assistant/
├── README.md
├── requirements.txt
├── Dockerfile
├── .gitignore
├── server.py
├── worker.py
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── assets/
│       └── favicon.ico
├── templates/
│   └── index.html
├── certs/
│   └── rootCA.crt
└── docs/
    ├── API.md
    ├── SETUP.md
    └── TROUBLESHOOTING.md
```

## 📁 Detailed Folder and File Descriptions

### Root Directory Files

#### `server.py` - Main Flask Application Server
**Purpose**: The core Flask web server that handles HTTP requests, routes, and coordinates between frontend and AI services.

**Key Responsibilities**:
- Serves the main HTML interface
- Handles API endpoints for speech-to-text conversion
- Processes messages through OpenAI
- Converts responses back to speech
- Manages CORS policies for cross-origin requests

#### `worker.py` - AI Service Integration Layer
**Purpose**: Contains all the helper functions that interact with external AI services (Watson and OpenAI).

**Key Functions**:
- `speech_to_text()`: Converts audio binary data to text using Watson STT
- `openai_process_message()`: Processes user messages through GPT-3
- `text_to_speech()`: Converts text responses to audio using Watson TTS

#### `requirements.txt` - Python Dependencies
**Purpose**: Lists all Python packages required for the project to run.

**Dependencies Include**:
- Flask: Web framework for creating the server
- Flask-CORS: Handles Cross-Origin Resource Sharing
- openai: Official OpenAI Python client library
- requests: HTTP library for making API calls

#### `Dockerfile` - Container Configuration
**Purpose**: Defines how to build a Docker container for the application.

**Process**:
1. Uses Python 3.10 as base image
2. Sets up working directory
3. Copies project files
4. Installs Python dependencies
5. Configures SSL certificates for OpenAI API
6. Sets environment variables
7. Starts the Flask server

#### `.gitignore` - Git Ignore Rules
**Purpose**: Specifies which files and folders Git should ignore when tracking changes.

### `/static/` - Static Web Assets

#### `/static/css/style.css` - Stylesheet
**Purpose**: Contains all CSS styling for the web interface.

**Features**:
- Responsive design for different screen sizes
- Dark/light theme toggle functionality
- Loading animations using CSS keyframes
- Modern UI components styling
- Mobile-friendly interface elements

#### `/static/js/script.js` - Frontend JavaScript
**Purpose**: Handles all client-side functionality and user interactions.

**Key Features**:
- Audio recording and playback
- Real-time speech-to-text conversion
- Message sending and receiving
- UI state management
- Theme switching
- Error handling and user feedback

#### `/static/assets/` - Static Assets
**Purpose**: Contains images, icons, and other static assets.

### `/templates/` - HTML Templates

#### `index.html` - Main Web Interface
**Purpose**: The main HTML template that creates the user interface.

**Components**:
- Chat interface similar to popular messaging apps
- Voice recording controls
- Message input field
- Settings panel for voice selection
- Theme toggle switch
- Responsive layout components

### `/certs/` - SSL Certificates
**Purpose**: Contains SSL certificates required for secure API communication.

**Files**:
- `rootCA.crt`: Root certificate authority certificate for secure connections

### `/docs/` - Documentation

#### `API.md` - API Documentation
**Purpose**: Detailed documentation of all API endpoints, request/response formats, and usage examples.

#### `SETUP.md` - Setup Instructions
**Purpose**: Step-by-step instructions for setting up the development environment and running the application.

#### `TROUBLESHOOTING.md` - Common Issues and Solutions
**Purpose**: Guide for resolving common problems and debugging tips.

## 🚀 Quick Start

### Prerequisites
- Docker installed on your system
- Internet connection for API access
- Modern web browser with microphone support

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd voice-assistant
   ```

2. **Build Docker Image**
   ```bash
   docker build -t voice-assistant .
   ```

3. **Run the Application**
   ```bash
   docker run -p 8000:8000 voice-assistant
   ```

4. **Access the Application**
   - Open your web browser
   - Navigate to `http://localhost:8000`
   - Allow microphone permissions when prompted

## 🔧 Configuration

### Environment Variables
- `OPENAI_API_KEY`: Set to "skills-network" for lab environment
- `REQUESTS_CA_BUNDLE`: Path to SSL certificate bundle
- `SSL_CERT_FILE`: Path to SSL certificate file

### Watson Service URLs
- Speech-to-Text: `https://sn-watson-stt.labs.skills.network`
- Text-to-Speech: `https://sn-watson-tts.labs.skills.network`

## 🌟 Features

### Core Functionality
- **Voice Input**: Record audio messages using your microphone
- **Text Input**: Type messages directly into the chat interface
- **Intelligent Responses**: Get smart answers powered by OpenAI GPT-3
- **Voice Output**: Hear responses read aloud with natural speech
- **Multi-language Support**: Support for multiple languages and accents

### User Interface
- **Modern Design**: Clean, intuitive interface similar to popular chat applications
- **Dark/Light Themes**: Toggle between dark and light modes
- **Responsive Layout**: Works on desktop, tablet, and mobile devices
- **Real-time Feedback**: Loading indicators and status messages
- **Voice Selection**: Choose from different voice options for speech output

### Technical Features
- **Dockerized Deployment**: Easy deployment with Docker containers
- **RESTful API**: Well-structured API endpoints for integration
- **Error Handling**: Comprehensive error handling and user feedback
- **Security**: SSL/TLS encryption for secure API communication
- **Scalable Architecture**: Modular design for easy maintenance and updates

## 🔄 Application Flow

1. **User Interaction**: User either speaks into microphone or types a message
2. **Audio Processing**: If voice input, audio is sent to Watson Speech-to-Text
3. **Text Processing**: Converted text is sent to OpenAI GPT-3 for processing
4. **Response Generation**: GPT-3 generates an intelligent response
5. **Voice Synthesis**: Response text is converted to speech using Watson Text-to-Speech
6. **User Feedback**: Both text and audio responses are displayed/played to user

## 🧪 Testing

### Manual Testing
- Test voice input with different accents and languages
- Verify text input functionality
- Check audio output quality
- Test theme switching
- Verify responsive design on different devices

### API Testing
- Test each endpoint individually using tools like Postman
- Verify proper error handling
- Check response formats and status codes

## 🚀 Deployment

### Local Development
```bash
python server.py
```

### Docker Deployment
```bash
docker build -t voice-assistant .
docker run -p 8000:8000 voice-assistant
```

### Production Considerations
- Use environment-specific configuration files
- Implement proper logging and monitoring
- Set up SSL certificates for production
- Configure proper CORS policies
- Implement rate limiting for API endpoints

## 📚 Technologies Used

- **Frontend**: HTML5, CSS3, JavaScript (ES6+), Bootstrap, jQuery
- **Backend**: Python, Flask, Flask-CORS
- **AI Services**: OpenAI GPT-3, IBM Watson Speech-to-Text, IBM Watson Text-to-Speech
- **Containerization**: Docker
- **HTTP Client**: Requests library
- **Audio Processing**: Web Audio API, MediaRecorder API

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

If you encounter any issues:
1. Check the troubleshooting guide in `/docs/TROUBLESHOOTING.md`
2. Review the API documentation in `/docs/API.md`
3. Open an issue on GitHub with detailed error information

## 🔮 Future Enhancements

- Multi-user support with user authentication
- Conversation history and context management
- Integration with additional AI models
- Voice command recognition for system controls
- Real-time conversation transcription
- Support for multiple languages in the same conversation
- Integration with external APIs (weather, news, etc.)
- Mobile app development for iOS and Android
