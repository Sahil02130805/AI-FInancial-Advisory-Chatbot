from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Chatbot logic function
def simple_chatbot(user_query):
    if user_query == "What is the total revenue?":
        return "The total revenue is $394 billion."
    elif user_query == "How has net income changed over the last year?":
        return "The net income has increased by $50 billion over the last year."
    elif user_query == "What is the total assets value?":
        return "The total assets value is $1 trillion."
    elif user_query == "What are the total liabilities?":
        return "The total liabilities amount to $400 billion."
    elif user_query == "What is the cash flow from operating activities?":
        return "The cash flow from operating activities is $250 billion."
    else:
        return "Sorry, I can only provide information on predefined queries."

# Route for handling chatbot requests
@app.route('/chat', methods=['POST'])
def chatbot():
    user_query = request.json.get('query', '')
    response = simple_chatbot(user_query)
    return jsonify({"response": response})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
