from django.shortcuts import render

# Create your views here.
from . import store


def index(request):
    return render(request, 'index.html')


def logout_request(request):
    store.removeUser(request.session["user"]);
    request.session["user"] = None;
    return render(request=request,
                  template_name="index.html")


def login_request(request):
    if request.method == 'POST':
        username = request.POST.get('user_name')
        if (store.isUserPresent(username)):
            print(username + " already present")
            return render(request,
                          "index.html",
                          {"error": True})
        else:
            print(username + " is not not present, inserting")
            store.addUser(username);
            request.session["user"] = username;
            return render(request,
                          "home.html",
                          {"user": username})
