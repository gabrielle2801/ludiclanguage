from django.views.generic import TemplateView
from django.shortcuts import render


class BaseView(TemplateView):
    template_name = "index.html"


class LegalNoticeView(TemplateView):
    template_name = "legal_notice.html"


class AboutUsView(TemplateView):
    template_name = "about_us.html"


def handle_server_error(request):
    return render(request, '500.html')
