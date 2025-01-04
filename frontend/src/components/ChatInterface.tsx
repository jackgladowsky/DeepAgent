import React, { useState, useEffect } from 'react';
import ButtonUsage from './Button';
import MultilineTextFields from './TextInput';
import ChatDisplay from './ChatDisplay';
import { FormControl, InputLabel, Select, MenuItem } from '@mui/material';

interface Message {
    role: 'user' | 'assistant';
    content: string;
}

interface ModelOption {
    label: string;
    value: string;
    provider: string;
}

export default function ChatInterface() {
    const [messages, setMessages] = useState<Message[]>([]);
    const [inputText, setInputText] = useState('');
    const [isLoading, setIsLoading] = useState(false);
    const [models, setModels] = useState<ModelOption[]>([]);
    const [selectedModel, setSelectedModel] = useState<ModelOption | null>(null);

    // Fetch available models on component mount
    useEffect(() => {
        const fetchModels = async () => {
            try {
                const response = await fetch('http://localhost:8000/models');
                const data = await response.json();
                setModels(data.models);
                if (data.models.length > 0) {
                    setSelectedModel(data.models[0]);
                }
            } catch (error) {
                console.error('Error fetching models:', error);
            }
        };
        fetchModels();
    }, []);

    const handleSendMessage = async () => {
        if (!selectedModel || !inputText.trim()) return;
        
        // Add user message
        const userMessage: Message = { role: 'user', content: inputText };
        setMessages(prev => [...prev, userMessage]);
        setInputText('');
        setIsLoading(true);

        try {
            const response = await fetch('http://localhost:8000/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    messages: [...messages, userMessage],
                    model: selectedModel.value,
                    provider: selectedModel.provider
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
    };

    return (
        <div className="chat-interface">
            <ChatDisplay messages={messages} />
            <div className="input-container">
                <FormControl fullWidth sx={{ mb: 2 }}>
                    <InputLabel>Model</InputLabel>
                    <Select
                        value={selectedModel?.value || ''}
                        label="Model"
                        onChange={(e) => {
                            const model = models.find(m => m.value === e.target.value);
                            if (model) setSelectedModel(model);
                        }}
                        MenuProps={{
                            PaperProps: {
                                sx: {
                                    maxHeight: 400,
                                    '& .MuiMenuItem-root': {
                                        display: 'flex',
                                        justifyContent: 'space-between',
                                        gap: '12px'
                                    }
                                }
                            }
                        }}
                    >
                        {models.map((model) => (
                            <MenuItem key={model.value} value={model.value}>
                                <span>{model.label}</span>
                                <span style={{ 
                                    opacity: 0.7,
                                    fontSize: '0.85em',
                                    backgroundColor: 'rgba(0, 0, 0, 0.1)',
                                    padding: '2px 8px',
                                    borderRadius: '4px'
                                }}>
                                    {model.provider}
                                </span>
                            </MenuItem>
                        ))}
                    </Select>
                </FormControl>
                <MultilineTextFields 
                    value={inputText}
                    onChange={(text) => setInputText(text)}
                    disabled={isLoading}
                />
                <ButtonUsage 
                    onClick={handleSendMessage}
                />
            </div>
        </div>
    );
};
