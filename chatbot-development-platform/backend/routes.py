from flask import jsonify, request
from .app import app, db
from .models import Prompt

@app.route('/api/prompt', methods=['POST'])
def create_prompt():
    data = request.json
    prompt = Prompt(input_text=data['input_text'], response_text=data['response_text'])
    db.session.add(prompt)
    db.session.commit()
    return jsonify(message='Prompt created successfully'), 201

# Define other routes here
