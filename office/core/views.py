from .models import PageCounter, Contact
from .forms import ContactForm
from django.views.generic import TemplateView
from django.views import generic


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
		return context


class ContactView(generic.CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'office/home.html'

    def get_form(self):
        form = super(ContactView, self).get_form(form_class=self.ContactForm)
        return form
