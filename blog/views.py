from django.shortcuts import render
from django.http import HttpResponse


#AI BOT HERE 
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('chat',read_only=False,logic_adapter=['chatterbot.logic.BestMatch']) # initialize the chatbot 

list_to_train = [
    'Hi',
    'Hello',
    'How are you?',
    'I am doing well',
    'What is your name?',
    'My name is Chatbot',
    'What is the weather like?',
    'It is sunny today',
    'What are you doing today?',
    'I am reading a book',
    'Can you recommend any books?',
    'Yes, I can recommend some books'
    'Here are some books to read: 1. The Great Gatsby, 2. To Kill a Mockingbird, 3. 1984'
    'What is the capital of France?',
    'The capital of France is Paris',
    'What is the population of Paris?',
    'The population of Paris is 2,229,621',
    'What is the most famous painting by Vincent van Gogh?',
    'The most famous painting by Vincent van Gogh is The Starry Night',
    'hello , there ?',
    'hi , there!',
    'what is you favorite color?',
    'my favorite color is blue',
    'what is your favorite food?',
    'my favorite food is pizza',
    'what is your favorite book?',
    'my favorite book is To Kill a Mockingbird',
    'what is your favorite movie?',
    'my favorite movie is The Godfather',
    'what is your favorite author?',
    'my favorite author is Jane Austen',
    'what is your favorite singer?',
    'my favorite singer is Billie Eilish',
]

list_trainer = ListTrainer(bot)
list_trainer.train(list_to_train)



#AI BOT END HERE



# Create your views here.

def index(request):
    return render(request, 'blog/index.html')

def specific(request):
    return HttpResponse ("This is a specific blog post.")

# def article(request, article_id):
#     return render(request, 'blog/article.html', {'article_id': article_id})

def getResponse(request):
    userMessage = request.GET.get('userMessage') # get the user's message from the query string from index.html
    return HttpResponse(userMessage)