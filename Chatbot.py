import nltk
import random
from nltk.chat.util import Chat, reflections

# Define some patterns and responses
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hey there!', 'Hi!']),
    (r'how are you?', ['I am doing well, thank you!', 'I\'m fine, thanks!', 'I\'m good, how about you?']),
    (r'what\'?s your name?', ['I\'m a chatbot.', 'I don\'t really have a name.']),
    (r'(.*) your name(.*)', ['I don\'t really have a name.', 'You can call me a chatbot.']),
    (r'(.*) (age|old) are you(.*)', ['I don\'t really have an age.']),
    (r'(.*) (love|like) you(.*)', ['Aww, that\'s sweet.', 'Thank you!']),
    (r'(.*) (weather|temperature)(.*)', ['The weather is nice today.', 'It\'s sunny outside.', 'I\'m not sure, you can check online.']),
    (r'(.*) (created|made) you(.*)', ['I was created by a developer.', 'I\'m a creation of programming.']),
    (r'bye|goodbye', ['Goodbye!', 'Bye!', 'Take care!']),
]

# Create a chatbot with the patterns
chatbot = Chat(patterns, reflections)

# Start the conversation
print("Hello! I'm a chatbot. How can I help you today?")
while True:
    user_input = input("> ")
    response = chatbot.respond(user_input)
    print(response)
    if user_input.lower() == 'exit':
        break
