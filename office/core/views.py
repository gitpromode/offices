from .models import PageCounter, Contact
from .forms import ContactForm
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages

class HomeView(CreateView):
	model = Contact
	form_class = ContactForm
	template_name = 'office/home.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		if PageCounter.objects.first():
			total_count = PageCounter.objects.first()
			total_count.total_count += 1
			total_count.save()
		else:
			total_count = PageCounter()
			total_count.total_count = 1
			total_count.save()
		return context

	def get_success_url(self):
		success_url = reverse_lazy('home')
		messages.success(self.request, 'Profile details updated.')
		return success_url
