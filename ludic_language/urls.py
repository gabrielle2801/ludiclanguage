"""ludic_language URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from django.urls import path
from ludic_language.profiles import views
from ludic_language.base.views import BaseView
from ludic_language.profiles.views import LoginView, IndexSpeechView, IndexPatientView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BaseView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('speech_homepage/', IndexSpeechView.as_view(), name='index_speech'),
    path('patient_homepage/', IndexPatientView.as_view(), name='index_patient'),
    path('logout/', views.logout_request, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
