import React, { useState } from 'react';
import ButtonUsage from './Button';
import MultilineTextFields from './TextInput';
import ChatDisplay from './ChatDisplay';

interface Message {
    role: 'user' | 'assistant';
    content: string;
}

export default function ChatInterface() {
    const [messages, setMessages] = useState<Message[]>([]);
    const [inputText, setInputText] = useState('');
    const [isLoading, setIsLoading] = useState(false);

    const handleSendMessage = async () => {
        if (inputText.trim()) {
            // Add user message
            const userMessage: Message = { role: 'user', content: inputText };
            setMessages(prev => [...prev, userMessage]);
            setInputText('');
            setIsLoading(true);

            try {
                const response = await fetch('http://localhost:8001/chat', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        messages: [...messages, userMessage],
                        model: 'openrouter'
                    }),
                });

                const data = await response.json();
                
                // Add AI response
                setMessages(prev => [...prev, {
                    role: 'assistant',
                    content: data.completion
                }]);
            } catch (error) {
                console.error('Error:', error);
                // Optionally add error message to chat
                setMessages(prev => [...prev, {
                    role: 'assistant',
                    content: 'Sorry, there was an error processing your request.'
                }]);
            } finally {
                setIsLoading(false);
            }
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
                <ButtonUsage 
                    onClick={handleSendMessage}
                />
            </div>
        </div>
    );
};
