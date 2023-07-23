from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
    return render(request,"home.html")


def removepunctuation(request):
    # getting the text
    text = request.POST.get('text','default')
    # checking if the value is on or off
    punctuation = request.POST.get('punctuation','off')
    Upper = request.POST.get('upper','off')
    space = request.POST.get('space','off')

    if punctuation == "on":
        punc = '''!()-[]{};:'"\,<>.+/?@#$%^&*_~='''
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
        prev_char_space = False

        for char in text:
            if char != " ":
                analyzed += char
                prev_char_space = False
            elif not prev_char_space:
                analyzed += char
                prev_char_space = True
        params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}
        return render(request,"removepunctuation.html",params)
    
    else:
        return HttpResponse("Check the checkbox and try again ")
