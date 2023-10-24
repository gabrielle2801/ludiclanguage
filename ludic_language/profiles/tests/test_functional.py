from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from ludic_language.profiles.models import Profile, Address, User
from ludic_language.exercises.models import Pathology
from django.contrib.auth import get_user_model
from selenium.webdriver.common.by import By

firefox_options = webdriver.FirefoxOptions()
firefox_options.headless = True
firefox_options.log.errors = "trace"
firefox_options.add_argument('--window-size=1920x1080')


class LudicLanguageProfileTest(StaticLiveServerTestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(options=firefox_options)
        self.user = get_user_model().objects.create_user(
            username='Marieaumont', first_name='Marie', password='12test12', email='test@email.com')
        self.user_id = self.user.pk
        self.user.save()
        self.therapist = Profile(user=self.user, birth_date='1975-05-12', state=2,
                                 bio='Marie est spécialisée ......', profile_pic='marieaumont.png'
                                 ).save()
        self.address = Address.objects.create(
            num=6, street='rue de ...', zip_code=92500, city='Paris', profile_id=self.user_id)
        self.patient = User.objects.create_user(
            username='LucasD', password='12test12', email='test@email.com')
        self.pathology_id = Pathology.objects.create(name='Dyslexie').pk
        Profile(user=self.patient, birth_date='2013-05-12', state=1,
                bio='Lucas est atteint de ......', profile_pic='lucasdesmarais.png',
                pathology_id=self.pathology_id, therapist_id=self.therapist).save()
        return super().setUp()

    def test_login(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.get('%s%s' % (self.live_server_url, '/login/'))
        driver.find_element(By.ID, 'id_username').send_keys('Marieaumont')
        driver.find_element(By.NAME, 'password').send_keys('12test12')
        driver.find_element(By.CSS_SELECTOR, '.submit').click()
        driver.find_element(By.NAME, 'patient').click()

    def test_form(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.get('%s%s' % (self.live_server_url, '/login/'))
        driver.find_element(By.ID, 'id_username').send_keys('Marieaumont')
        driver.find_element(By.NAME, 'password').send_keys('12test12')
        driver.find_element(By.CSS_SELECTOR, '.submit').click()
        driver.find_element(By.CSS_SELECTOR, '.btn').click()
        driver.get('%s%s' % (self.live_server_url, '/form_patient/'))
        driver.find_element(By.NAME, 'first_name').send_keys('Clarence')
        driver.find_element(By.NAME, 'last_name').send_keys('Grey')
        driver.find_element(By.NAME, 'email').send_keys('helenegrey@email.com')
        driver.find_element(By.NAME, 'username').send_keys('ClarenceGr')
        driver.find_element(By.NAME, 'password1').send_keys('12test12')
        driver.find_element(By.NAME, 'password2').send_keys('12test12')
        driver.find_element(By.NAME, 'birth_date').send_keys('12/05/2015')
        driver.find_element(By.NAME, 'bio').send_keys('Clarence est un ....')
        driver.find_element(By.NAME, 'review').send_keys(
            'Clarence a besoin de  ....')
        driver.find_element(By.NAME, 'pathology').send_keys('Dyslexie')
        driver.find_element(By.NAME, 'num').send_keys('10')
        driver.find_element(By.NAME, 'street').send_keys('rue de ....')
        driver.find_element(By.NAME, 'zip_code').send_keys(92140)
        driver.find_element(By.NAME, 'city').send_keys('Clamart')
        driver.find_element(By.CSS_SELECTOR, '.submit').click()
        driver.find_element(By.NAME, 'patient').click()

    def test_search_therapist(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.get(self.live_server_url)
        search_bar = driver.find_element(By.NAME, "search_therapist")
        search_bar.clear()
        search_bar.send_keys("Paris")
        search_bar.send_keys(Keys.RETURN)
