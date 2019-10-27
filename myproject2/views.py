from django.http import  HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    spaceremover=request.POST.get('spaceremover','off')
    charcount=request.POST.get('charcount','off')
    print(removepunc)
    print(djtext)
    if removepunc=="on":
   ## analyzed=djtext
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params={'purpose':'Removed Punctuation','analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',params)

    if (fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Changed to uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
       # return render(request, 'analyze.html', params)

    if(newlineremover=="on"):
        analyzed=""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzed=analyzed+char
        params = {'purpose': 'removed new line', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if (spaceremover == "on"):
        analyzed = ""
        for  index , char in enumerate(djtext):
            if not (djtext[index]==" " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'space remover line', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if(charcount=="on"):
        c=0
        for char in djtext:
            c=c+1
            analyzed=c
        params = {'purpose': 'character count', 'analyzed_text': analyzed}

    return render(request, 'analyze.html', params)

    if(charcount!="on" and  removepunc!="on"and fullcaps!="on"and spaceremover != "on" and newlineremover!="on"):
        return HttpResponse("Error")

def ex1(request):
    s='''<h1>Navigation Bar </h1>
    <a href="http://www.google.com">google</a><br>
    <a href="http://www.facebook.com">facebook</a>'''
    return HttpResponse(s)
