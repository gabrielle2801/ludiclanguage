from django.views.generic import TemplateView


class BaseView(TemplateView):
    template_name = "index.html"


class LegalNoticeView(TemplateView):
    template_name = "legal_notice.html"


class AboutUsView(TemplateView):
    template_name = "about_us.html"
