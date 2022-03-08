from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from django.contrib.auth import get_user_model

from django.contrib.auth.models import User
from ludic_language.profiles.models import Profile
from ludic_language.exercises.models import Pathology, Exercise, LudicJourney
from ludic_language.exercises.views import ExerciseListView, LudicJouneyListView, LudicJourneyDetailView
# from ludic_language.exercises.views import PathologyDetailView


class BaseTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.user = get_user_model().objects.create_user(
            username='LucasD', first_name='Lucas', password='12test12', email='test@email.com')
        self.user_id = self.user.pk
        self.user.save()
        self.therapist = User.objects.create_user(
            username='Marieaumont', password='Therapist@25').pk

        self.pathology_id = Pathology.objects.create(
            name='Dyslexie', description="la pathologie ..... ").pk
        self.profile = Profile(user=self.user, birth_date='2013-05-12', state=1,
                               bio='Lucas est atteint de ......', profile_pic='lucasdesmarais.png',
                               pathology_id=self.pathology_id, therapist_id=self.therapist).save()

        self.exercise = Exercise.objects.create(name='Améliorer ....', description="L'aider ...", picture1='Winter.png',
                                                picture2="puzzle.png", pathology_id=self.pathology_id, therapist_id=self.therapist,
                                                description_game="Rassemble ...", title_game='Puzzle').pk
        return super().setUp()


class PathologyDetailTest(BaseTest):

    def test_detail(self):
        login = self.client.login(
            username='LucasD', password='12test12')
        self.assertTrue(login)
        detail_url = reverse('pathology', kwargs={
            'pk': self.pathology_id
        })
        response = self.client.get(detail_url)
        assert response.status_code == 200
        self.assertTemplateUsed(response, 'pathology.html')


class ExerciseListTest(BaseTest):
    def setUp(self):
        self.list_url = reverse('exercise_list')
        return super().setUp()

    def test_view_ok(self):
        login = self.client.login(
            username='Marieaumont', password='Therapist@25')
        self.assertTrue(login)

        response = self.client.get(self.list_url)
        assert response.status_code == 200

    def test_queryset(self):
        request = self.factory.get(self.list_url)
        view = ExerciseListView()
        view.request = request
        qs = view.get_queryset()
        self.assertQuerysetEqual(qs, Pathology.objects.all())


class LudicJourneyAddTest(BaseTest):

    def test_view_ok(self):
        form_url = reverse('form_ludicjourney', args=[
            self.exercise])
        login = self.client.login(
            username='Marieaumont', password='Therapist@25')
        self.assertTrue(login)
        response = self.client.get(form_url)
        self.assertEquals(response.status_code, 200)

    def test_form_ok(self):
        form_url = reverse('form_ludicjourney', args=[
            self.exercise])
        ludic_journey = {
            'date': '03/03/2022',
            'patient_id': self.user,
            'exercise_id': self.exercise
        }
        login = self.client.login(
            username='Marieaumont', password='Therapist@25')
        self.assertTrue(login)
        response = self.client.post(form_url, ludic_journey)
        self.assertEquals(response.status_code, 200)


class LudicJourneyListTest(BaseTest):
    def test_view_ok(self):
        login = self.client.login(
            username='LucasD', password='12test12')
        self.assertTrue(login)
        response = self.client.get(reverse('ludic_journey'))
        self.assertEquals(response.status_code, 200)

    def test_queryset(self):
        request = self.factory.get(reverse('ludic_journey'))
        view = LudicJouneyListView()
        request.user = self.user
        view.request = request
        qs = view.get_queryset()
        self.assertQuerysetEqual(
            qs, LudicJourney.objects.filter(patient_id=self.user.profile))


class LudicJourneyDetailTest(BaseTest):
    def test_view_ok(self):
        login = self.client.login(
            username='LucasD', password='12test12')
        self.assertTrue(login)
        response = self.client.get(
            reverse('play_on', kwargs={'pk': self.exercise}))
        self.assertEquals(response.status_code, 200)


'''
    def test_queryset(self):
        kwargs = {'pk': self.exercise}
        request = self.factory.get(
            reverse('play_on', kwargs={'pk': self.exercise}))
        view = LudicJourneyDetailView()
        view.request = request
        qs = view.get_queryset()
        self.assertQuerysetEqual(
            qs, LudicJourney.objects.filter(pk=self.kwargs.get('pk')))
'''
