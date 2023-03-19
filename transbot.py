from flask import Flask, request, jsonify

app = Flask(__name__)

class ChatBot:
    def __init__(self):
        self.prompt = ""
    
    def generate_response(self, user_input):
        prompt = f"User: {user_input}\nBot:"
        response = openai.Completion.create(
          engine="davinci",
          prompt=prompt,
          temperature=0.5,
          max_tokens=1024,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0,
          stop=["\nBot:"]
        )
        message = response.choices[0].text.strip()
        return message
    
    def chat(self, user_input):
        if user_input.lower() == "exit":
            return "Goodbye!"
        elif user_input.lower() == "generate blog post":
            self.prompt = "User: Can you generate a sample text for a blog post on the benefits of meditation?\nBot:"
            bot_response = self.generate_response(user_input)
            return bot_response
        elif user_input.lower() == "recommend book":
            self.prompt = "User: Can you recommend a book on machine learning?\nBot:"
            bot_response = self.generate_response(user_input)
            return bot_response
        elif user_input.lower() == "latest news":
            self.prompt = "User: Can you provide a summary of the latest news in technology?\nBot:"
            bot_response = self.generate_response(user_input)
            return bot_response
        elif user_input.lower() == "healthy breakfast smoothie":
            self.prompt = "User: Can you provide a recipe for a healthy breakfast smoothie?\nBot:"
            bot_response = self.generate_response(user_input)
            return bot_response
        elif user_input.lower() == "workout routine for beginners":
            self.prompt = "User: Can you recommend a workout routine for beginners?\nBot:"
            bot_response = self.generate_response(user_input)
            return bot_response
        elif user_input.lower() == "budget-friendly vacation":
            self.prompt = "User: Can you suggest a travel destination for a budget-friendly vacation?\nBot:"
            bot_response = self.generate_response(user_input)
            return bot_response
        elif user_input.lower() == "继续":
            self.prompt = "User: 继续\nBot:"
            bot_response = self.generate_response(user_input)
            return bot_response
        else:
            self.prompt = f


import googletrans
from googletrans import Translator

class ChatBot:
    def __init__(self):
        self.prompt = ""
        self.translator = Translator()
    
    def generate_response(self, user_input):
        prompt = f"User: {user_input}\nBot:"
        response = self.translator.translate(user_input, dest='en')
        message = response.text.strip()
        return message
    
    def chat(self, user_input):
        if user_input.lower() == "exit":
            return "Goodbye!"
        elif user_input.lower() == "继续":
            self.prompt = "User: 继续\nBot:"
            bot_response = self.generate_response(user_input)
            return bot_response
        else:
            self.prompt = f"User: {user_input}\nBot:"
            bot_response = self.generate_response(user_input)
            return bot_response

chatbot = ChatBot()
print("Welcome to the chatbot!")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    else:
        bot_response = chatbot.chat(user_input)
        print(f"Bot: {bot_response}")
