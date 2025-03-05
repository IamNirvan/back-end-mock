from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/test-endpoint', methods=['POST'])
def test_endpoint():
    """
    A simple POST endpoint for testing purposes.
    Accepts JSON data and returns it back with an additional message.
    """
    try:
        # Get the JSON data from the request
        data = request.get_json()
        
        # If no data is provided, return an error
        if not data:
            return jsonify({
                "error": "No data provided",
                "status": "failure"
            }), 400
        
        # Return the received data with a success message
        return jsonify({
            "message": "Data received successfully",
            "status": "success",
            "received_data": data
        }), 200
    
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({
            "error": str(e),
            "status": "error"
        }), 500

# This is needed for Vercel serverless functions
def handler(event, context):
    return app