from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib import messages  # pops up message abt thank you for submitting the form....
from .models import (  # so we got out models
    UserProfile,
    Blog,
    Portfolio,
    Testimonial,
    Certificate
)

from django.views import generic  # using generic view, template view, list view and so on...
# these are class-based view built-in specifically for regular tasks
from .forms import ContactForm


class IndexView(generic.TemplateView):
    template_name = "main/index.html"

    # calling methods
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        testimonials = Testimonial.objects.filter(is_active=True)
        certificates = Certificate.objects.filter(is_active=True)
        blogs = Blog.objects.filter(is_active=True)
        portfolio = Portfolio.objects.filter(is_active=True)

        context["testimonials"] = testimonials
        context["certificates"] = certificates
        context["blogs"] = blogs
        context["portfolio"] = portfolio
        return context


# This is a form that contains template, form and its url.
class ContactView(generic.FormView):
    template_name = "main/contact.html"
    form_class = ContactForm
    success_url = "/"  # clients will be re diverted if the form is invalid.

    # calling form valid method
    def form_valid(self, form):  # passing the form through here, which is a contact form
        form.save()  # saving in form instance
        messages.success(self.request, 'Thank you. We will be in touch soon.')
        return super().form_valid(form)  # The Message will be shown in the front-end


# listed view of portfolio
class PortfolioView(generic.ListView):
    model = Portfolio   # this is slug, which will be going through url
    template_name = "main/portfolio.html"
    paginate_by = 10

    def get_queryset(self):     # queryset template
        return super().get_queryset().filter(is_active=True)    # filtering if it's True


class PortfolioDetailView(generic.DetailView):
    model = Portfolio
    template_name = "main/portfolio-detail.html"


class BlogView(generic.ListView):   # same as portfolio view
    model = Blog
    template_name = "main/blog.html"
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class BlogDetailView(generic.DetailView):   # same as portfolio detail view
    model = Blog
    template_name = "main/blog-detail.html"
