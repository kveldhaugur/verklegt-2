from django.shortcuts import render

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form.UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'user/register.html', {
            'form': UserCreationForm()
        })
    #take this out later and un-indent return render(req, user/register
    else:
        return render(request, 'signup/index.html')

def signin(request):
    return render(request, 'signin/index.html')

def logout(request):
    pass
