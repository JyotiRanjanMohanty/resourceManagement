import os
import logging
from flask import Flask, render_template, request, jsonify, session
from werkzeug.middleware.proxy_fix import ProxyFix
from nlp_processor import process_query
from response_generator import generate_response

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key")
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

# Routes
@app.route('/')
def home():
    """Render the main chat interface."""
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    """Render the management dashboard with visualization."""
    return render_template('dashboard.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """Process chat messages and return responses."""
    try:
        logging.debug(f"Received request: {request.json}")
        user_message = request.json.get('message', '')
        
        logging.debug(f"Processing message: '{user_message}'")
        
        if not user_message:
            logging.warning("No message provided in request")
            return jsonify({'error': 'No message provided'}), 400
        
        # Process the user query to understand intent
        intent, entities = process_query(user_message)
        logging.debug(f"Processed intent: {intent}, entities: {entities}")
        
        # Generate appropriate response based on intent and entities
        response = generate_response(intent, entities)
        logging.debug(f"Generated response type: {response['type']}")
        
        result = {
            'response': response['message'],
            'type': response['type'],
            'data': response.get('data', None)
        }
        
        return jsonify(result)
        
    except Exception as e:
        logging.error(f"Error processing chat: {str(e)}")
        import traceback
        logging.error(traceback.format_exc())
        return jsonify({'error': 'An error occurred processing your request'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
