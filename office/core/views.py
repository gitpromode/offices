from .models import PageCounter
from django.views.generic import TemplateView

class HomeView(TemplateView):
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
		context['total_count'] = total_count.total_count
		return context