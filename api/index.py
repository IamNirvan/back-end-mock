from flask import Flask, request, jsonify
from flask_cors import CORS

# Create Flask app
app = Flask(__name__)
CORS(app)

# Root endpoint for debugging
@app.route('/', methods=['GET'])
def home():
    return jsonify({"status": "alive"}), 200

# Specific test endpoint
@app.route('/api/test-endpoint', methods=['POST'])
def test_endpoint():
    try:
        data = request.get_json()
        return jsonify({
            "message": "Data received successfully",
            "received_data": data
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Vercel requires a handler
def handler(event, context):
    return app