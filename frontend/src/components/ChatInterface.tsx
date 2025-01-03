import React, { useState } from 'react';
import ButtonUsage from './Button';
import MultilineTextFields from './TextInput';
import ChatDisplay from './ChatDisplay';

export default function ChatInterface() {
    const [messages, setMessages] = useState<string[]>([]);
    const [inputText, setInputText] = useState('');

    const handleSendMessage = () => {
        if (inputText.trim()) {
            setMessages([...messages, inputText]);
            setInputText('');
        }
    };

    return (
        <div className="chat-interface">
            <ChatDisplay messages={messages} />
            <div className="input-container">
                <MultilineTextFields 
                    value={inputText}
                    onChange={(text) => setInputText(text)}
                />
                <ButtonUsage onClick={handleSendMessage} />
            </div>
        </div>
    );
};
