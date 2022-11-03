from django.shortcuts import render
from django.http import HttpResponse;

# Create your views here.
def display(request):
    ss ="<center><h1 style='color:Blue;'> Welcome to Uppala Saloons</h1><hr color = 'yellow' width = '95%'></center>";
    return HttpResponse(ss);
    
def show(request):
      ss ='''<center><h1 style='color:Green;'>Welcome to Uppala saloons</h1>
           <hr color = 'brown' width = '85%' size = '5px'/>
           <p1 style='color:black;' font = '15px'>Uppala saloons is best for your hair cuts in Telangana we provide the first class hair cuts to make your outerimage wonderful</p2>
           <hr color = 'red' width='55%' size= '4px'/></center>''';
      return HttpResponse(ss);
         