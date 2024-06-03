from django.shortcuts import render
from django.http import HttpResponse
import json
import requests

# Create your views here.
def index(request):
    return render(request, 'chatbot/index.html')

def getResponse(request):
    ## Using ollama
    userMsg = request.GET.get('userMessage')
    url = 'http://localhost:11434/api/generate'
    headers = {"Content-Type": "application/json"}
    data = {
    "model": "gemma:7b",
    "prompt": f"""{userMsg}
    """,
    "stream": False}

    response = requests.post(url, headers=headers, data=json.dumps(data))
    return HttpResponse(json.loads(response.text)['response'])