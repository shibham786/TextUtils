#this file is created by me. - simba
from django.http import HttpResponse
from django.shortcuts import render  # this is for rendering html template
def home(request):
    return render(request,"home.html")

def analayzer(request):
    #getting textarea text from home.html
    djtext = request.POST.get('text','defaultvalue') # print data which is coming from home page
    #Get checkbox value  from home page
    punc_text = request.POST.get('punc','off')
    upper_text = request.POST.get('upper','off')
    extraspace = request.POST.get('extraspace','off')
    charcount =  request.POST.get('charcount','off')
    # print(djtext)
    # print(punc_text)
    print(extraspace)
  
    if punc_text == 'on':
        punchuation_list = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analayzed_text = ""
        for char in djtext:
            
                if char not in punchuation_list:
                    analayzed_text += char
        params = {"purpose":"Remove punctuation","analyzed":analayzed_text}
        print("in punch space",analayzed_text)
        djtext = analayzed_text
        #return render(request,"analayzer.html",params)
       
    if upper_text == 'on':
        analayzed_text = ""
        for char in djtext:
           analayzed_text += char.upper()
        params = {"purpose":"Upper CASE","analyzed":analayzed_text}
        print("in upper space",analayzed_text)
        djtext = analayzed_text
        #return render(request,"analayzer.html",params)

    if  extraspace == 'on':
        analayzed_text = ""
        for index,char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):  # enumerate for getting iterable obj index and checking two extra space
                analayzed_text = analayzed_text + char
        params = {"purpose":"Remove Extra Space","analyzed":analayzed_text}
        print("in extra space",analayzed_text)
        djtext = analayzed_text
        
    #     #return render(request,"analayzer.html",params)

    if  charcount == 'on':
        analayzed_text = 0
        for index,char in enumerate(djtext):
            if not (djtext[index] == "  " and djtext[index+1] == "  "):  # enumerate for getting iterable obj index and checking two extra space
                analayzed_text += 1
        params = {"purpose":"Character Count","analyzed":analayzed_text}
       
        #return render(request,"analayzer.html",params)

   
    if punc_text != "on" and upper_text != "on" and extraspace != "on" and charcount != "on":
        return HttpResponse("please select any operation")

    return render(request,"analayzer.html",params)


  