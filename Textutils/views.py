from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Home(request):
    # return HttpResponse("Hello world")
    return render(request,"home.html")


def removepunctuation(request):
    # sourcery skip: extract-method, remove-unnecessary-else, swap-if-else-branches
    # getting the text
    text = request.GET.get('text','default')
    # checking if the value is on or off
    punctuation = request.GET.get('punctuation','off')
    Upper = request.GET.get('upper','off')
    space = request.GET.get('space','off')
    # print(punctuation)
    if punctuation == "on":
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~='''
        analyzed = ""

        for char in text:
            if char not in punc:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request,"removepunctuation.html",params)
    elif Upper == "on":
        analyzed = ""
        for char in text:
            analyzed = analyzed+char.upper()
        params = {'purpose': 'Removed UpperCase', 'analyzed_text': analyzed}
        return render(request,"removepunctuation.html",params)
    elif space == "on":
        analyzed = ""
        for index, char in enumerate(text):
            if text[index] != " " or text[index + 1] != " ":
                analyzed = analyzed + char
        params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}
        return render(request,"removepunctuation.html",params)
    else:
        return HttpResponse("Check the checkbox and try again ")


# def UpperCase(request):
#     text = request.GET.get('text','default')

#     analyzed = ""

#     params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
#     return render(request,"Upper.html",params)
