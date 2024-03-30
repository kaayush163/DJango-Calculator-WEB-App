from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
# Create your views here.


def index(request):
    # return HttpResponse("server started")
    return render(request,'index.html')


def submitquery(request):
    q = request.GET['query']  #request.GET this GET comes from HTML form submission method and the query comes from name from the input field tag
    #whatever written in html <input type='submit' name='query' id='query'>
    #we need input field whatever we do 2+3 or any calculation we need to build logic here so that's why we atke query named input tag
    # return HttpResponse(q)

    # jsondict = {
    #     "q":q
    # }
    # return JsonResponse(jsondict) 

    try:
        ans = eval(q)   #Inbuilt python function takes string of number matemetical expression and evaluates resul in inetger
        mydict = {
            "q" : q,
            "ans" : ans,
            "error" : False,
            "result":True  #this is for because even if we put equal sign in input box the alert becom success so to handle that we do this
            #This is calld Logical Error not error found on terminal or syntax this is about logic is wrong have to find on our own
        }
        return render(request,'index.html',context=mydict)
    
    except:
        #  pass
        # for handling 1 divide by zero kind of operation
        mydict={
 
            "error":True,
            "result":False
        }

        return render(request,'index.html',context = mydict)
    