import nltk
from nltk.chat.util import Chat , reflections

patterns = [
    (r 'hi|hello|hey',['Hello!','Hey there','Hi!']),
    (r 'how are you?',["I'm doing well,thank you!", "I'm good,thanks for asking."]),
    (r 'what is your name?', ["You can call me Chatbot.","I'm just a humble chatbot."]),
    (r 'quit',["Bye Take care.", "Goodbye, have a great day!"]),
]

chatbot = Chat(patterns,reflections)

print("Welcome to the chatbot.Type 'quit' to end the conversation.")
while True:
    user_input = input("You:")
    response = chatbot.respond(user_input)
    print("Chatbot:", response)
    if user_input.lower() == 'quit':
        break
