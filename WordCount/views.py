from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')
def count(request):
    fullText=request.GET['fullText']
    wordList=fullText.split()
    wordContDict={};

    for word in wordList:
        if word in wordContDict:
            wordContDict[word] += 1
        else:
            wordContDict[word] = 1
    sortedWord=sorted(wordContDict.items(), key=operator.itemgetter(1), reverse=True)

    print(fullText) #will print in console
    return render(request, 'count.html',{'fullText':fullText,'count':len(wordList), 'sortedWord':sortedWord})

def about(request):
    return render(request, 'about.html')
