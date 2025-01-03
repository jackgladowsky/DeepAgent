import React from 'react';
import logo from './logo.svg';
import './App.css';

import ChatInterface from './components/ChatInterface';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <ChatInterface />
      </header>
    </div>
  );
}

export default App;
