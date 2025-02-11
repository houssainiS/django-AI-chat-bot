from django.shortcuts import render
from django.http import HttpResponse


#AI BOT HERE 
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

bot = ChatBot('chat',read_only=False,logic_adapters=[{

        'import_path':'chatterbot.logic.BestMatch',
        # 'default_response':"I am sorry, I don't understand.",
        # 'maximum_similarity_threshold':0.9 ,

}]) # initialize the chatbot 

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
    'Yes, I can recommend some books' ,

]
ChatterbotCorpusTrainter = ChatterBotCorpusTrainer(bot)

#list_trainer = ListTrainer(bot)
#list_trainer.train(list_to_train)

ChatterbotCorpusTrainter.train('chatterbot.corpus.english') # train the chatbot with English corpus


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
    chatResponse =str(bot.get_response(userMessage))
    

    return HttpResponse(chatResponse) # return the chatbot's response to the user