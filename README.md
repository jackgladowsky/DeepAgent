# DeepAgent

DeepAgent is a framework/chatbot for building personal AI agents. The goal of this project is to provide a simple 
and easy to use interface for building AI agents and connecting them to various serivces and tools. DeepAgent will
also have a basic web interface for interacting with the agents and to serve as the dashboard for the agent.

## Architecture
- DeepAgent will consist of various agents that work together to perform tasks. 
- **Control Agent**, manages the overall system and the other agents. 
    - Whenever a chat message is recieved, the control agent will interpret the message.
    - If just a simple question, control agent can respond directly.
    - If the message needs a tool call, the control agent will interface with the "tool agent" to perform the tool call.
- **Tool Agent**, interfaces with the tool to perform the tool call.
    - The tool agent will be responsible for calling the tool and getting the result.
    - The tool agent will then return the result to the control agent.