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
from ludic_language.base.views import BaseView, LegalNoticeView, AboutUsView
from ludic_language.profiles.views import LoginView, IndexSpeechView, IndexPatientView, PatientListView, \
    PatientAddView, PatientDetailView, PatientDeleteView, TherapistListView, TherapistDetailView
from ludic_language.workshops.views import WorkshopAddView, WorkshopListView, WorkshopUpdateView,\
    ReportListView, ReportDetailView
from ludic_language.exercises.views import ExerciseListView, PathologyDetailView, LudicJourneyAddView, LudicJouneyListView, \
    LudicJourneyDetailView, LudicJourneyUpdateView, LudicJouneyListTherapistView, AssessementDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BaseView.as_view(), name='index'),
    path('legal_notice', LegalNoticeView.as_view(), name='legal_notice'),
    path('about_us', AboutUsView.as_view(), name='about_us'),
    path('login/', LoginView.as_view(), name='login'),
    path('speech_homepage/', IndexSpeechView.as_view(), name='index_speech'),
    path('patient_homepage/', IndexPatientView.as_view(), name='index_patient'),
    path('therapist_list/', TherapistListView.as_view(), name='therapist_list'),
    path('patient_list/', PatientListView.as_view(), name='patient_list'),
    path('form_patient/', PatientAddView.as_view(), name='form_patient'),
    path('detail_therapist/<int:pk>',
         TherapistDetailView.as_view(), name='detail_therapist'),
    path('detail_patient/<int:pk>',
         PatientDetailView.as_view(), name='detail_patient'),
    path('delete_patient/<int:pk>',
         PatientDeleteView.as_view(), name='delete_patient'),
    path('form_workshop/', WorkshopAddView.as_view(), name='form_workshop'),
    path('form_workshop/<int:patient_id>',
         WorkshopAddView.as_view(), name='form_workshop'),
    path('list_workshop/', WorkshopListView.as_view(), name='list_workshop'),
    path('form_report/<int:pk>',
         WorkshopUpdateView.as_view(), name='form_report'),
    path('report_list/', ReportListView.as_view(), name='report_list'),
    path('report/<int:pk>', ReportDetailView.as_view(), name='report_patient'),
    path('pathology/<int:pk>', PathologyDetailView.as_view(), name='pathology'),
    path('exercise_list/',
         ExerciseListView.as_view(), name='exercise_list'),
    path('form_ludicjourney/<int:exercise_id>',
         LudicJourneyAddView.as_view(), name='form_ludicjourney'),
    path('ludic_journey/',
         LudicJouneyListView.as_view(), name='ludic_journey'),
    path('exercise_therapist/',
         LudicJouneyListTherapistView.as_view(), name='exercise_therapist'),
    path('play_on/<int:pk>',
         LudicJourneyDetailView.as_view(), name='play_on'),
    path('form_assessement/<int:pk>', LudicJourneyUpdateView.as_view(),
         name='form_assessement'),
    path('assessement/<int:pk>', AssessementDetailView.as_view(),
         name='assessement'),
    path('logout/', views.logout_request, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler500 = "ludic_language.profiles.views.handle_server_error"
handler500 = "ludic_language.base.views.handle_server_error"
