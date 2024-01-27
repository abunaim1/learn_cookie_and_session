from django.shortcuts import render
from datetime import datetime, timedelta
from django.http import HttpResponse

# Create your views here.

def set_cookie(request):
    response = render(request, 'home.html')
    response.set_cookie('name', 'naim')
    # response.set_cookie('name', 'taru', max_age=10)
    response.set_cookie('name', 'taru', expires=datetime.utcnow()+timedelta(days=7))
    return response

def get_cookie(request):
    name = request.COOKIES.get('name')
    print(request.COOKIES)
    return render(request, 'cookie.html', {'name':name})

def delete_cookie(request):
    response = render(request, 'del.html')
    response.delete_cookie('name')
    return response

"""
cookie vs session
cookie save in client browser or client database or client server, cookie will use when we work with dark theme, language preferences, remmember me 
session save in backend and temporary information, session will use when we work with authentication, shopping card, 

"""

def set_session(request):
    data = {
        'name' : 'naim',
        'age' : 24,
        'language' : 'Bangla'
    }
    print(request.session.get_session_cookie_age())
    print(request.session.get_expiry_date())
    request.session.update(data)
    return render(request, 'home.html')

def get_session(request):
    if 'name' in request.session:
        data = request.session
        request.session.modified = True
        return render(request, 'get_session.html', {'data':data})
    else:
        return HttpResponse("Your session is expired! F*ck again")


def delete_session(request):
    # del request.session['name'] #if i want to delete a particular vlaue of sassion this is the process
    request.session.flush() #for all delete
    return render(request, 'del.html')