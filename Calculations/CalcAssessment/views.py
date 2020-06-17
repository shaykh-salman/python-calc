from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')

def login_request(request):
    if request.method == 'POST':
        username = request.POST.get('user_name')
        print(username)
    return render(request=request,
                  template_name="home.html")
