"""ludic_language URL Configuration"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from django.urls import path
from ludic_language.profiles import views
from ludic_language.base.views import BaseView, LegalNoticeView, AboutUsView
from ludic_language.profiles.views import LoginView, IndexSpeechView, \
    IndexPatientView, PatientListView, \
    PatientAddView, PatientDetailView, PatientDelete, \
    TherapistListView, TherapistDetailView
from ludic_language.workshops.views import WorkshopAddView, WorkshopListView, \
    WorkshopUpdateView, \
    ReportListView, ReportDetailView, ReportDeleteView
from ludic_language.exercises.views import ExerciseListView, \
    PathologyDetailView, LudicJourneyAddView, LudicJouneyListView, \
    LudicJourneyDetailView, LudicJourneyUpdateView, \
    LudicJouneyListTherapistView, AssessementDetailView, \
    SentenceApiView, RecorderView, TalesApiView, ExerciseDetailView
from ludic_language.todo.views import TodoListAddView, \
     TodoUpdate, TodoDetail, TodoDelete, WorkshopDateDetailView

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
         PatientDelete.as_view(), name='delete_patient'),
    path('form_workshop/', WorkshopAddView.as_view(), name='form_workshop'),
    path('form_workshop/<int:patient_id>',
         WorkshopAddView.as_view(), name='form_workshop'),
    path('list_workshop/', WorkshopListView.as_view(), name='list_workshop'),
    path('form_report/<int:pk>',
         WorkshopUpdateView.as_view(), name='form_report'),
    path('report_list/', ReportListView.as_view(), name='report_list'),
    path('report_patient/<int:pk>', 
         ReportDetailView.as_view(), name='report_patient'),
    path('delete_report/<int:pk>',
         ReportDeleteView.as_view(), name='delete_report'),
    path('pathology/<int:pk>', PathologyDetailView.as_view(), 
         name='pathology'),
    path('exercise_list/',
         ExerciseListView.as_view(), name='exercise_list'),
    path('form_ludicjourney/<int:exercise_id>',
         LudicJourneyAddView.as_view(), name='form_ludicjourney'),
    path('ludic_journey/',
         LudicJouneyListView.as_view(), name='ludic_journey'),
    path('exercise_therapist/',
         LudicJouneyListTherapistView.as_view(), name='exercise_therapist'),
    path('exercise_detail/<int:pk>',
         ExerciseDetailView.as_view(), name='exercise_detail'),
    path('play_on/<int:pk>',
         LudicJourneyDetailView.as_view(), name='play_on'),
    path('play_on/', SentenceApiView.as_view(), name='exercise_add'),
    path('play_on/', TalesApiView.as_view(), name='exercise_tales'),
    path('recorder_therapist/<int:patient_id>',
         RecorderView.as_view(), name='recorder_therapist'),
    path('form_assessement/<int:pk>', LudicJourneyUpdateView.as_view(),
         name='form_assessement'),
    path('assessement/<int:pk>', AssessementDetailView.as_view(),
         name='assessement'),
    path('index_speech/', IndexSpeechView.as_view(), 
         name='task_list'),
    path('workshop_detail/<int:pk>', WorkshopDateDetailView.as_view(), 
         name='workshop_detail'),
    path('task_create/', TodoListAddView.as_view(),
         name='task_form'),
    path('task_update/<int:pk>', TodoUpdate.as_view(),
         name='task_update'),
    path('task_detail/<int:pk>', TodoDetail.as_view(),
         name='task_detail'),
    path('delete/<int:pk>', TodoDelete.as_view(), name='task_delete'),
    path('logout/', views.logout_request, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler500 = "ludic_language.profiles.views.handle_server_error"
