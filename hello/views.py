from django.shortcuts import render
from .forms import InputForm
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = InputForm()
    return render(request, 'index.html', {'form': form})


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
