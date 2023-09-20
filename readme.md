## Voice chat with gpt 3
This is project that allows a user to have a live voice conversation with a chat bot. It consists of a frontend that records the human part of the conversation and plays back gpt replies part of the conversation. The backend parses the voice input using OpenAI's whisper model, retrives the chat history from a postgres database, and gets the new reply using GPTs API.  

### Running the project
In order to run the project, you need to set up the postgres and RabbitMQ instance using docker. 
[docker readme](docker/readme.md)

Then you need to run both backends.
[backend readme](backend/readme.md)

Then you need to run the frontend. It does not need to be run on the same computer, but the ip-address must be set up correctly.
[frontend readme](frontend/readme.md)
