from django.contrib import messages
from django.shortcuts import redirect

class AdminAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        if request.path.startswith('/admin/') and not request.user.is_superuser:
            return redirect('home')
        
        return self.get_response(request)

class LoginAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/login/') and request.user.is_authenticated:
            return redirect('home')
        
        return self.get_response(request)