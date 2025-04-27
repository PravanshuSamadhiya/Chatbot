from flask import Flask, render_template, request, jsonify
from chatbot import TornedEducationChatbot

app = Flask(__name__)
chatbot = TornedEducationChatbot()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_categories')
def get_categories():
    return jsonify(chatbot.categories)

@app.route('/get_questions', methods=['POST'])
def get_questions():
    category = request.json.get('category')
    questions = chatbot.show_questions(category)
    return jsonify(questions)

@app.route('/get_answer', methods=['POST'])
def get_answer():
    category = request.json.get('category')
    question_index = request.json.get('question_index')
    answer = chatbot.get_answer(category, question_index)
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True) 