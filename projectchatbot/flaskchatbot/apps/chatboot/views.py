from flask import render_template, Blueprint, request, jsonify
from .controller import query  # Import your query function from the controller

main = Blueprint('main', __name__)

# Initialize a dictionary to store previous queries and their results
previous_queries = {}

@main.route('/')
def chat():
    return render_template('pages/chat.html')

@main.route('/msg', methods=['POST'])
def message():
    if request.method == 'POST':
        data = request.get_json()

        if data is not None and 'text' in data:
            text = data['text']

            if text:
                # Check if the query already exists in previous_queries
                if text in previous_queries:
                    result = previous_queries[text]
                else:
                    result = query(text)  # Call your query function here
                    previous_queries[text] = result

                return jsonify({"generated_text": result})

    return jsonify({"error": "Bad Request"}), 400  # Return a JSON error response with a 400 status code
