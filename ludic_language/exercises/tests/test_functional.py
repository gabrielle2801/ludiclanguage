from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from ludic_language.profiles.models import Profile, User
from ludic_language.exercises.models import Pathology, Exercise
from django.contrib.auth import get_user_model

firefox_options = webdriver.FirefoxOptions()
firefox_options.headless = True
firefox_options.log.errors = "trace"
firefox_options.add_argument('--window-size=1920x1080')


class LudicLanguageExerciseTest(StaticLiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(options=firefox_options)
        self.user = get_user_model().objects.create_user(
            username='Marieaumont', first_name='Marie', password='12test12', email='test@email.com')
        self.user_id = self.user.pk
        self.user.save()
        self.therapist = Profile(user=self.user, birth_date='1975-05-12', state=2,
                                 bio='Marie est spécialisée ......', profile_pic='marieaumont.png'
                                 ).save()
        self.pathology_id = Pathology.objects.create(name='Dyslexie').pk

        self.exercise = Exercise.objects.create(name='Améliorer ....', description="L'aider ...", picture1='Winter.png',
                                                picture2="puzzle.png", pathology_id=self.pathology_id, therapist_id=self.therapist,
                                                description_game="Rassemble ...", title_game='Puzzle').pk
        return super().setUp()

    def test_exercise_list(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.get('%s%s' % (self.live_server_url, '/login/'))
        driver.find_element_by_id('id_username').send_keys('Marieaumont')
        driver.find_element_by_name('password').send_keys('12test12')
        driver.find_element_by_css_selector('.submit').click()
        driver.find_element_by_name('ludic_journey').click()
