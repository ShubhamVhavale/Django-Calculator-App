from django.shortcuts import render, HttpResponse

# Create your views here.
def cindex(request):
    return render(request,"index1.html")

def calsubmit(request):
    query=request.GET['query']
    ans=0
    result=False
    try:
        ans=eval(query)
        error = False
        result = True
    except:
        error=True
    mydict={
        'query' : query,
        'answer' : ans,
        'errorpresent' : error, 
        'result' : result
    }
    print(ans)
    return render(request,'index1.html',context=mydict)