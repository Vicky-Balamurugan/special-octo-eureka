from flask import Flask, render_template, request, jsonify
import uuid
import requests

app = Flask(__name__)

# Dummy LLM API URL for illustration purposes
LLM_API_URL = 'https://api.example.com/generate'

# Store user configurations and prompts in memory
user_data = {}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/prompt_library')
def prompt_library():
    return render_template('prompt_library.html')

@app.route('/model_tuning')
def model_tuning():
    return render_template('model_tuning.html')

@app.route('/create_prompt', methods=['POST'])
def create_prompt():
    user_id = request.form.get('user_id')
    input_text = request.form.get('input_text')
    response_text = request.form.get('response_text')
    if user_id not in user_data:
        user_data[user_id] = {'prompts': [], 'tuning': {}}
    user_data[user_id]['prompts'].append({'input': input_text, 'response': response_text})
    return jsonify(status='success', message='Prompt created successfully')

@app.route('/test_prompt', methods=['POST'])
def test_prompt():
    user_id = request.form.get('user_id')
    input_text = request.form.get('input_text')
    response = generate_response(input_text, user_data.get(user_id, {}).get('tuning', {}))
    return jsonify(response=response)

@app.route('/tune_model', methods=['POST'])
def tune_model():
    user_id = request.form.get('user_id')
    temperature = float(request.form.get('temperature'))
    top_p = float(request.form.get('top_p'))
    top_k = int(request.form.get('top_k'))
    if user_id not in user_data:
        user_data[user_id] = {'prompts': [], 'tuning': {}}
    user_data[user_id]['tuning'] = {'temperature': temperature, 'top_p': top_p, 'top_k': top_k}
    return jsonify(status='success', message='Model tuning parameters updated')

@app.route('/generate_api_key', methods=['POST'])
def generate_api_key():
    user_id = request.form.get('user_id')
    api_key = str(uuid.uuid4())
    user_data[user_id]['api_key'] = api_key
    return jsonify(api_key=api_key)

def generate_response(input_text, tuning_params):
    payload = {
        'input': input_text,
        'temperature': tuning_params.get('temperature', 1.0),
        'top_p': tuning_params.get('top_p', 0.9),
        'top_k': tuning_params.get('top_k', 50)
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(LLM_API_URL, json=payload, headers=headers)
    return response.json().get('response', 'No response from LLM')

if __name__ == '__main__':
    app.run(debug=True)
