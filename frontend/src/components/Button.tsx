import * as React from 'react';
import Button from '@mui/material/Button';

interface ButtonUsageProps {
    onClick: () => void;
}

export default function ButtonUsage({ onClick }: ButtonUsageProps) {
    return (
        <Button variant="contained" onClick={onClick}>
            Send
        </Button>
    );
}
