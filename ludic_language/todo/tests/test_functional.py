from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from django.contrib.auth import get_user_model
from ludic_language.todo.models import Task
from ludic_language.profiles.models import Profile

firefox_options = webdriver.FirefoxOptions()
firefox_options.headless = True
firefox_options.log.errors = "trace"
firefox_options.add_argument('--window-size=1920x1080')


class LudicLanguageTaskTest(StaticLiveServerTestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(options=firefox_options)
        self.user = get_user_model().objects.create_user(
            username='Marieaumont', first_name='Marie', password='12test12', 
            email='test@email.com')
        self.user_id = self.user.pk
        self.user.save()
        self.therapist = Profile(user=self.user, birth_date='1975-05-12',
                                 state=2,
                                 bio='Marie est spécialisée ......', 
                                 profile_pic='marieaumont.png'
                                 ).save()
        self.task = Task(title='Tâche à faire',
                         description='Description de la tâche',
                         completed=True,
                         created_at='2024-05-12 15:00',
                         due_datetime='2024-06-12 15:00',
                         slug='Tâche à faire',
                         priority=2,
                         therapist_id=self.therapist)
        self.task.save()
        self.now = datetime.now()
        self.today_date = self.now.strftime('%Y-%m-%d')
        self.today_hours = self.now.strftime('%H:%M:%S')

    def test_delete_task(self):
        driver = self.driver
        driver.implicitly_wait(5)
        driver.get('%s%s' % (self.live_server_url, '/login/'))
        driver.find_element(By.ID, 'id_username').send_keys('Marieaumont')
        driver.find_element(By.NAME, 'password').send_keys('12test12')
        driver.find_element(By.CSS_SELECTOR, '.submit').click()
        driver.find_element(By.CSS_SELECTOR, '.btn').click()
        driver.get('%s%s' % (self.live_server_url, '/task_create/'))
        driver.find_element(By.NAME, 'title').send_keys('Test delete')
        driver.find_element(By.ID, 'id_description').send_keys('test delete_task')
        driver.find_element(By.ID, 'id_priority').send_keys('HIGH')
        driver.find_element(By.ID, 'id_completed').click()
        date_input = driver.find_element(By.NAME, 'due_datetime')
        date_input.send_keys("29/06/2100")
        date_input.send_keys(Keys.TAB)
        date_input.send_keys("17:45")
        driver.find_element(By.CSS_SELECTOR, '.submit').click()
        driver.get('%s%s' % (self.live_server_url, '/speech_homepage/'))
        driver.find_element(By.CSS_SELECTOR, '#task_icon.close').click()
        driver.switch_to.alert.accept() 
        driver.get('%s%s' % (self.live_server_url, '/speech_homepage/'))
  
    def test_form(self):
        driver = self.driver
        driver.implicitly_wait(5)
        now = datetime.now()
        today_date = now.strftime('%d-%m-%Y')
        today_hours = now.strftime('%H:%M:%S')
        driver.get('%s%s' % (self.live_server_url, '/login/'))
        driver.find_element(By.ID, 'id_username').send_keys('Marieaumont')
        driver.find_element(By.NAME, 'password').send_keys('12test12')
        driver.find_element(By.CSS_SELECTOR, '.submit').click()
        driver.find_element(By.CSS_SELECTOR, '.btn').click()
        driver.get('%s%s' % (self.live_server_url, '/task_create/'))
        driver.find_element(By.NAME, 'title').send_keys('Test à faire')
        driver.find_element(By.ID, 'id_description').send_keys('tests fonctionnels')
        driver.find_element(By.ID, 'id_priority').send_keys('MEDIUM')
        driver.find_element(By.ID, 'id_completed').click()
        date_input = driver.find_element(By.NAME, 'due_datetime')
        date_input.send_keys(today_date)
        date_input.send_keys(Keys.TAB)
        date_input.send_keys(today_hours)
        driver.find_element(By.CSS_SELECTOR, '.submit').click()
        driver.get('%s%s' % (self.live_server_url, '/speech_homepage/'))
     