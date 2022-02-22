# Ludic Language
### Project 13 in Python developer path at OpenClassrooms
#### Vocational exercices to enable children to improve their languages problems
Thanks to **Ludic Language** app, parents children and speech-language pathologist may interact with each other. Create a language platform to fight the language problems like dysphasia, dyslexia or stutter pathology. 

_______________________________
**Guidelines**

* Use an agile project methodology
* Implement 12 good parctices of Xtrem programming
* A social impact 
* Create a database with PostgreSQL
* Create .env file for environment variable

_______________________________
**How to install **
**Create an virtual environnement and packages**

``` shell
pip install pipenv
mkdir .venv 
pipenv install --python 3.9 
pipenv install django requests 
```
Install dependencies 
``` shell
pipenv install 
```
_______________________________

**Customer journey description**

*Customer Journey*

* The pathologist could create the patient account after the first workshop with parent and patient. He organize online workshop and could check the patient's exercices, adjust the exercices journey if necessary. 

* The parent could choose the pathologist on the platform. The patient (child) could practice and visualize the record after workshop with theirs parents. 


________________________________
**Functionalities**

* Homepage with pathologist research for the parents and the request of the pathologist for an account
* Responsive interface
* User authentification :
    * pathologist create a patient account with password and username
    * Admin create the pathologist account
* Exercices journey according to the pathology
* Record creation's by the patholgist and visualize by the parents
_____________________________

* Agile methode  -> Users Stories / Boards on Trello :
https://trello.com/b/r56gmbvL/langage-ludique
* Deployment on Heroku



