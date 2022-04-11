from typing import Counter, Text
from django.http import HttpResponse, request
from django.shortcuts import render


def index(request):
    # return HttpResponse('Index')
    return render(request, 'index.html')

# def analyze(request):
#     return HttpResponse('Analyze')
#     # return render(request,'analyze.html')


def analyze(request):
    TEXT = request.POST.get('text', 'default')
    # print(TEXT)
    removepunc = request.POST.get('removepunc', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    if removepunc == 'on':
        panctuations = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analyzetext = ""
        for char in TEXT:
            if char not in panctuations:
                analyzetext += char
        param = {
            'purpose': 'Removed Panctuations',
            'analyzed_text': analyzetext
        }
        TEXT = analyzetext
        # return render(request,'analyze.html',param)
    if(capitalize == 'on'):
        analyzetext = ""
        for char in TEXT:
            analyzetext = analyzetext+char.upper()

        param = {
            'purpose': 'Capitalized Text',
            'analyzed_text': analyzetext
        }
        TEXT = analyzetext
        # return render(request,'analyze.html',param)
    if(newlineremover == 'on'):
        analyzetext = ""
        for char in TEXT:
            if char != "/n" and char != '/r':
                analyzetext = analyzetext+char

        param = {
            'purpose': 'Remove New Lines',
            'analyzed_text': analyzetext
        }
        TEXT = analyzetext
        # return render(request,'analyze.html',param)

    if(extraspaceremover == 'on'):
        analyzetext = ""
        for index, char in enumerate(TEXT):
            if TEXT[index] == " " and TEXT[index+1] == " ":
                pass
            else:
                analyzetext = analyzetext+char

        param = {
            'purpose': 'Extra Space Removed',
            'analyzed_text': analyzetext
        }
        TEXT = analyzetext

        # return render(request,'analyze.html',param)

    elif(charcount == 'on'):
        Count = 0
        for char in TEXT:
            if char != " ":
                Count += 1
            else:
                pass

        param = {
            'purpose': 'Character Counter',
            'analyzed_text': Count
        }

        return render(request, 'analyze.html', param)

    return render(request, 'analyze.html', param)

    # else:
    # return HttpResponse('Error')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
