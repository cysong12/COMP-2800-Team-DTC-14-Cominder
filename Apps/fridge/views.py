from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import *

# Create your class-based views here.


@login_required()
def home(request):
    fridge = Fridge.objects.all()
    context = {
        'fridge': fridge,
    }
    return render(request, 'fridge/home.html', context)


class FridgeListView(ListView):
    # Tells what model to query
    model = Fridge
    # Template
    template_name = 'fridge/home.html'


class FridgeDetailView(DetailView):
    model = Fridge


# CREATE ITEM
class FridgeCreateView(LoginRequiredMixin, CreateView):
    model = Fridge
    fields = ['name', 'quantity']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# UPDATE ITEM
class FridgeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Fridge
    # When successfully deleted, will take user back to homepage
    success_url = '/fridge'
    fields = ['name', 'quantity']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        fridge_item = self.get_object()
        # Prevents others to update other people's items
        if self.request.user == fridge_item.user:
            return True
        return False


class FridgeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Fridge
    # When successfully deleted, will take user back to homepage
    success_url = '/fridge'

    def test_func(self):
        fridge_item = self.get_object()
        # Prevents others to update other people's items
        if self.request.user == fridge_item.user:
            return True
        return False

