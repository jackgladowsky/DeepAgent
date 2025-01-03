import * as React from 'react';
import Box from '@mui/material/Box';
import { useEffect, useRef } from 'react';

interface ChatDisplayProps {
    messages: string[];
}

export default function ChatDisplay({ messages }: ChatDisplayProps) {
    const messagesEndRef = useRef<null | HTMLDivElement>(null);

    const scrollToBottom = () => {
        messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
    };

    useEffect(() => {
        scrollToBottom();
    }, [messages]);

    return (
        <Box className="chat-display">
            {messages.map((message, index) => (
                <div key={index} className="message">
                    {message}
                </div>
            ))}
            <div ref={messagesEndRef} />
        </Box>
    );
}
