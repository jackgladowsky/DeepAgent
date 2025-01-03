import * as React from 'react';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';

interface MultilineTextFieldsProps {
    value: string;
    onChange: (text: string) => void;
    disabled?: boolean;
}

export default function MultilineTextFields({ value, onChange, disabled }: MultilineTextFieldsProps) {
    return (
        <Box
            component="form"
            sx={{ width: '100%' }}
            noValidate
            autoComplete="off"
        >
            <TextField
                fullWidth
                id="outlined-multiline-flexible"
                label="Type a message"
                multiline
                maxRows={4}
                value={value}
                onChange={(e) => onChange(e.target.value)}
                disabled={disabled}
                sx={{
                    '& .MuiOutlinedInput-root': {
                        '&:hover fieldset': {
                            borderColor: 'rgba(255, 255, 255, 0.3)',
                        },
                        '&.Mui-focused fieldset': {
                            borderColor: '#2196f3',
                        },
                    },
                }}
            />
        </Box>
    );
}
