import React, { useState } from 'react';
import { createPrompt } from '../services/api';

const CreatePrompt = () => {
    const [inputText, setInputText] = useState('');
    const [responseText, setResponseText] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        const response = await createPrompt(inputText, responseText);
        console.log(response.message);
    }

    return (
        <div>
            <h2>Create Prompt</h2>
            <form onSubmit={handleSubmit}>
                <div>
                    <label htmlFor="inputText">Input Text:</label>
                    <textarea id="inputText" value={inputText} onChange={(e) => setInputText(e.target.value)}></textarea>
                </div>
                <div>
                    <label htmlFor="responseText">Response Text:</label>
                    <textarea id="responseText" value={responseText} onChange={(e) => setResponseText(e.target.value)}></textarea>
                </div>
                <button type="submit">Create Prompt</button>
            </form>
        </div>
    );
}

export default CreatePrompt;
