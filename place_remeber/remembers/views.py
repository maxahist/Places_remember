from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from .models import Remember
from .forms import RememberForm


@login_required
def main(request):
    user = request.user
    remembers = Remember.objects.all().filter(author=user)

    return render(request, 'main.html', {'remembers':remembers})


@login_required
def remember_edit(request, remember_id):
    remember = get_object_or_404(Remember, id=remember_id)
    if remember.author == request.user:
        if request.method == 'POST':
            form = RememberForm(
                request.POST,
                instance=remember
            )
            if form.is_valid():
                form.save()
                return redirect('remembers:main')
        form = RememberForm(instance=remember)
        return render(request, 'remember_edit.html', 
                      {'form': form, 
                       'remember_id': remember.id,
                       'is_edit': True})
    
def remember_create(request):
    if request.method == 'POST':
        form = RememberForm(request.POST)
        if form.is_valid():
            remember = form.save(commit=False)
            remember.author = request.user
            remember.save()
            return redirect('remembers:main')
    form = RememberForm()
    return render(request, 'remember_edit.html', {'form': form})
        
