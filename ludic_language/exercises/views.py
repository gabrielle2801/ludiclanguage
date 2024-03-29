from django.views.generic import DetailView
from django.views.generic import ListView, CreateView
from django.views.generic.edit import UpdateView
from .serializers import RecorderSerializer
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
from django.urls import reverse_lazy

from ludic_language.exercises.models import (Pathology,
                                             LudicJourney,
                                             Exercise,
                                             RecorderMessage)
from ludic_language.exercises.forms import (LudicJourneyCreateForm,
                                            LudicJourneyAssessementForm)


class PathologyDetailView(DetailView):
    model = Pathology
    template_name = 'pathology.html'
    context_object_name = 'pathology_des'

    def get_queryset(self):
        qs = super().get_queryset()
        qs.filter(pk=self.request.user.profile.pathology_id)
        return qs


class ExerciseListView(LoginRequiredMixin, ListView):
    template_name = 'exercise_list.html'
    context_object_name = 'pathology_list'
    model = Pathology

    def get_queryset(self):
        qs = super().get_queryset()
        qs.select_related('exercise')
        return qs


class LudicJourneyAddView(LoginRequiredMixin, CreateView):
    form_class = LudicJourneyCreateForm
    model = LudicJourney
    template_name = 'form_ludicjourney.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['therapist'] = self.request.user.profile
        return kwargs

    def get_initial(self):
        initial = super().get_initial()
        initial['exercise'] = self.kwargs.get('exercise_id')
        return initial

    def get_success_url(self):
        return reverse('exercise_list')


class LudicJouneyListView(LoginRequiredMixin, ListView):
    template_name = 'ludic_journey.html'
    model = LudicJourney
    context_object_name = 'ludicjourney_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(
            patient_id=self.request.user.profile.user_id)
        return queryset


class LudicJouneyListTherapistView(LoginRequiredMixin, ListView):
    template_name = 'exercise_therapist.html'
    model = LudicJourney
    context_object_name = 'exercise_therapist'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.select_related('exercise')
        return queryset


class ExerciseDetailView(LoginRequiredMixin, DetailView):
    template_name = 'exercise_detail.html'
    model = Exercise
    context_object_name = 'exercise_detail'


class LudicJourneyDetailView(LoginRequiredMixin, DetailView):
    template_name = 'play_on.html'
    model = Exercise
    context_object_name = 'ludic_journey'


class SentenceApiView(APIView):
    queryset = RecorderMessage.objects.all()
    serializer_class = RecorderSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, * args, **kwargs):

        data = {

            'audio_file': request.FILES.get('audio'),
            'patient': request.user.profile.user_id,
            'sentence': request.data.get('sentence'),
            'exercise': request.data.get('exercise')
        }

        serializer = RecorderSerializer(data=data)
        print('data     ', data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TalesApiView(APIView):
    queryset = RecorderMessage.objects.all()
    serializer_class = RecorderSerializer
    permission_classes = (permissions.AllowAny,)
    pattern_name = "exercise_tales"

    def post(self, request, * args, **kwargs):

        data = {

            'audio_file': request.FILES.get('audio'),
            'patient': request.user.profile.user_id,
            'exercise': request.data.get('exercise')
        }

        serializer = RecorderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecorderView(LoginRequiredMixin, ListView):
    template_name = 'recorder_therapist.html'
    model = RecorderMessage
    context_object_name = 'recorder_therapist'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = RecorderMessage.objects.filter(
            patient_id=self.kwargs['patient_id'])
        return queryset


class LudicJourneyUpdateView(LoginRequiredMixin, UpdateView):
    model = LudicJourney
    form_class = LudicJourneyAssessementForm
    template_name = 'form_assessement.html'
    success_url = reverse_lazy('exercise_therapist')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['patient'] = self.request.user.profile
        return kwargs

    def get_initial(self):
        initial = super().get_initial()
        initial['exercise'] = self.kwargs.get('ludicjourney_id')
        return initial

    def get_success_url(self):
        return reverse('exercise_list')


class AssessementDetailView(LoginRequiredMixin, DetailView):
    model = LudicJourney
    template_name = 'assessement.html'
    context_object_name = 'assessement'


'''
class ExerciseAddView(LoginRequiredMixin, CreateView):
    form_class = ExerciseForm
    model = Exercise
    template_name = 'form_exercise.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['therapist'] = self.request.user.profile
        return kwargs

    def get_success_url(self):
        return reverse('index_speech')
'''

'''
-- Django version --
 class ExerciseListView(LoginRequiredMixin, ListView):
    template_name = 'exercise_list.html'
    context_object_name = 'pathology_list'
    model = Pathology

    def get_queryset(self):
        qs = super().get_queryset()
        qs.select_related('exercise')
        return qs

-- Python version --
class ExerciseListView(LoginRequiredMixin, ListView):
    template_name = 'exercise_list.html'
    context_object_name = 'exercise_list'
    model = Exercise

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        exercises = context['exercise_list']
        pathologies = defaultdict(list)
        for exercise in exercises:
            pathologies[exercise.pathology.name].append(exercise)
        path = sorted(pathologies.items())
        # sorted(pathologies.items())
        context['pathologies'] = path
        return context

test --APi--
class RecorderSentenceAPIView(APIView):
    template_name = 'play_on.html'
    model = RecorderMessage

    def post(self, request, *args, **kwargs):
        data = {
            'audio_file': request.data.get('audio_file'),
            'sentence': request.data.get('sentence'),
            'game': request.exercises.id,
            'patient': request.user.profile
        }
        serializer = RecorderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print('test api')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def post(self, request, *args, **kwargs):
        audio_file = request.FILES.get('audio')
        recorder = RecorderMessage()
        recorder.audio = audio_file
        recorder.save()
        return JsonResponse({
            'success': True
        })
'''
