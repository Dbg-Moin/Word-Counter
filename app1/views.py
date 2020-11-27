from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, 'app1/form.html')


def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    words = {}
    for word in wordlist:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

    sortWord = sorted(words.items(), key=operator.itemgetter(1), reverse=True)
    print(sortWord)
    return render(request, 'app1/result.html',
                  {'fulltext': fulltext,
                   'count': len(wordlist),
                   'words': words,
                   'sorted': sortWord})
