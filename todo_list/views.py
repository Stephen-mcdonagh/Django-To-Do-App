from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages

def home(requests):
	if request.method =="POST":
		form = ListForm(request.POST or None)

		if form.is_valid():
			form.save()
			all_items = List.objects.all
			messsages.success(request, ('Item Successfully saved'))
			return render(request, 'home.html', {'all_items', all_items})

	else:
		all_items = List.objects.all
		return render(request, 'home.html', {'all_items', all_items})
