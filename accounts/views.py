from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('events:index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


##class SignUp(generic.CreateView):
##    form_class = UserCreationForm
##    success_url = reverse_lazy('login')
##    template_name = 'signup.html'

##    def form_valid(self, form):
##    to_return = super().form_valid(form)
##    user = authenticate(
##        username=form.cleaned_data["username"],
##        password=form.cleaned_data["password1"],
##    )
##    login(self.request, user)
##    return to_return

