from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from django.contrib.auth import get_user_model


from django.contrib.auth.models import User
from ludic_language.workshops.models import Workshop
from ludic_language.workshops.views import ReportListView, WorkshopListView


class WorkshopAddViewTest(TestCase):
    def setUp(self):
        self.therapist = get_user_model().objects.create_user(
            username='Marieaumont', password='Therapist@25').pk
        self.patient = User.objects.create_user(
            username='ClarenceBr', password='12test12', 
            email='test@email.com').pk
        self.form_url = reverse('form_workshop')
        self.client = Client()
        self.workshop = {
            'date': '2022-02-12 15:00',
            'shedule_online': 'https://meet.google.com/njy-iipe-rkp',
            'patient': self.patient,
            'therapist': self.therapist
        }

        return super().setUp()

    def test_view_ok(self):
        login = self.client.login(
            username='Marieaumont', password='Therapist@25')
        self.assertTrue(login)
        response = self.client.get(self.form_url)
        self.assertEqual(response.status_code, 200)

    def test_form_ok(self):
        login = self.client.login(
            username='Marieaumont', password='Therapist@25')
        self.assertTrue(login)
        response = self.client.post(self.form_url, self.workshop)
        self.assertEqual(response.status_code, 200)
        workshop = Workshop.objects.filter(
            shedule_online='https://meet.google.com/njy-iipe-rkp')
        workshop.patient_id = self.patient
        workshop.therapist_id = self.therapist


class WorkshopListViewTest(TestCase):
    def setUp(self):
        self.therapist = get_user_model().objects.create_user(
            username='Marieaumont', password='Therapist@25').pk
        self.patient = User.objects.create_user(
            username='ClarenceBr', password='12test12',
            email='test@email.com').pk
        self.form_url = reverse('list_workshop')
        self.client = Client()
        self.workshop = Workshop.objects.filter(date='2022-02-12 15:00',
                                                report='Lorem ipsum dolor sit amet, consectetur adipiscing elit',
                                                shedule_online='https://meet.google.com/njy-iipe-rkp',
                                                patient_id=self.patient, 
                                                therapist_id=self.therapist)

        return super().setUp()

        def test_list_workshop_speech(self):
            login = self.client.login(
                username='Marieaumont', password='Therapist@25')
            self.assertTrue(login)
            response = self.client.post(self.form_url)
            self.assertEqual(response.status_code, 200)

        def test_user_list_worshop(self):
            request = self.factory.get(self.form_url)
            request.user = self.therapist
            response = WorkshopListView.as_view()(request)
            self.assertEqual(response.status_code, 200)


class ReportUpdateTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.therapist = get_user_model().objects.create_user(
            username='Marieaumont', password='Therapist@25').pk
        self.patient = User.objects.create_user(
            username='ClarenceBr', password='12test12', 
            email='test@email.com').pk
        self.workshop = Workshop.objects.create(date='2022-02-12 15:00',
                                                shedule_online='https://meet.google.com/njy-iipe-rkp',
                                                patient_id=self.patient, 
                                                therapist_id=self.therapist)
        self.workshop_id = self.workshop.pk
        self.form_url = reverse('form_report', kwargs={
            'pk': self.workshop_id})
        self.report_update = {
            'report': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit',
        }
        return super().setUp()

    def test_update_report_speech(self):
        login = self.client.login(
            username='Marieaumont', password='Therapist@25')
        self.assertTrue(login)
        response = self.client.post(self.form_url, self.report_update)
        self.assertEqual(response.status_code, 302)
        workshop = Workshop.objects.filter(date='2022-02-12 15:00')
        workshop.report = self.report_update


class ReportListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.therapist = get_user_model().objects.create_user(
            username='Marieaumont', password='Therapist@25').pk
        self.patient = User.objects.create_user(
            username='ClarenceBr', password='12test12', email='test@email.com')
        self.patient_id = self.patient.pk
        self.workshop = Workshop.objects.create(date='2022-02-12 15:00',
                                                shedule_online='https://meet.google.com/njy-iipe-rkp',
                                                report='Lorem ipsum dolor sit amet, consectetur adipiscing elit',
                                                patient_id=self.patient_id, 
                                                therapist_id=self.therapist).pk
        self.form_url = reverse('report_list')
        return super().setUp()

    def test_report_list_patient(self):
        login = self.client.login(username='ClarenceBr', password='12test12')
        self.assertTrue(login)
        response = self.client.get(self.form_url)
        self.assertEqual(response.status_code, 200)

    def test_user_list_report(self):
        request = self.factory.get(self.form_url)
        request.user = self.patient
        response = ReportListView.as_view()(request)
        self.assertEqual(response.status_code, 200)


class ReportDetailViewTest(TestCase):
    def setUp(self):
        self.therapist = get_user_model().objects.create_user(
            username='Marieaumont', password='Therapist@25').pk
        self.patient = User.objects.create_user(
            username='ClarenceBr', password='12test12', 
            email='test@email.com').pk
        self.client = Client()
        self.workshop = Workshop.objects.create(date='2022-02-12 15:00',
                                                shedule_online='https://meet.google.com/njy-iipe-rkp',
                                                report='Lorem ipsum dolor sit amet, consectetur adipiscing elit',
                                                patient_id=self.patient, 
                                                therapist_id=self.therapist).pk
        self.form_url = reverse('report_patient', kwargs={'pk': self.workshop})
        return super().setUp()

    def test_report_list_patient(self):
        login = self.client.login(username='ClarenceBr', password='12test12')
        self.assertTrue(login)
        response = self.client.get(self.form_url)
        self.assertEqual(response.status_code, 200)
