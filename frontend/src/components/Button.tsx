import * as React from 'react';
import Button from '@mui/material/Button';

interface ButtonUsageProps {
    onClick: () => void;
    disabled?: boolean;
}

export default function ButtonUsage({ onClick, disabled }: ButtonUsageProps) {
    return (
        <Button 
            variant="contained" 
            onClick={onClick}
            disabled={disabled}
        >
            Send
        </Button>
    );
}
