from django.shortcuts import render

def main(request):
    user = request.user
    return render(request, 'main.html', {'user':user})
