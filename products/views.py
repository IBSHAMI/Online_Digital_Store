from django.shortcuts import render, reverse, redirect
from django.http.response import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    FormView,
    View,
)


# create landing page view
class LandingPageView(TemplateView):
    template_name = "landing_page.html"
