const API_BASE_URL = 'http://localhost:5000/api';

export const createPrompt = async (inputText, responseText) => {
    const response = await fetch(`${API_BASE_URL}/prompt`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ input_text: inputText, response_text: responseText })
    });
    return await response.json();
}

// Define other API functions here
