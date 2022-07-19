
from multiprocessing import context
from .models import State
from django.shortcuts import render

# Create your views here.
def view_states(request):
    states = State.objects.select_related('country').all()
    context = {
        "states": states
    }
    return render(request, 'view_states.html', context )