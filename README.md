# Documentation on the api 

Hey!! This is an API built in typical simulation of the common transaction pdf generator we use day to day in mobile banking and ecommerce apps, i built this small api using django as a restful api and you can have it run locally and as well hosted on the port : http://sodiq-dukkainic.herokuapp.com/  feel free to test run each endpoint as i’m about to describe below. 

Of Course you must be an authorized user to access most areas of the product, so as such login at the end point : http://sodiq-dukkainic.herokuapp.com/login-auth/  to get a bearer token (jwt)  to access all areas and if you’re not a registered user kindly visit the end point : http://sodiq-dukkainic.herokuapp.com/register/ to register, this register endpoint could be accessed via the django rest framework gui with your browser easily. For this work I have used jwt authentication, see the documentation @ https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html to grab a better understanding . It’s an assumption that the person reading this is someone with knowledge of http request headers set-up and if not grab your coffee and relax the ui provided by swagger is really nice to play with. So sure! It'll be fun playing with this api.

## Navigation With swagger

Scroll to the bottom to either register or login to get a token, click on the icon you wanna visit (login or register) and click the “try it out”, provide necessary pay-load (noting username & email interchangeability in the login request) and copy the returned -access :key-  pair. Just below the top right corner is an icon “authorize” click the link and paste the given pair as :: Bearer key*******   (please note the format), then login and boom!! all your requests will be shipped with this authorization in the http header. Once we’re done with authorization visit the endpoint : http://sodiq-dukkainic.herokuapp.com/transactions/ to create a transaction, this will automatically generate 10 pdf’s for this transaction and save in the database accordingly, get an ordered list of the pdf documents on the transactions end point:: http://sodiq-dukkainic.herokuapp.com/transactions/ click  get to all documents grouped by transactions. Click the post icon to create a new transaction and gerate 10 copies of pdf receipts accordingly. The endpoint :http://sodiq-dukkainic.herokuapp.com/documents/ allows only a get-request to get all created pdf document files and can do a query parameter at the end point : http://sodiq-dukkainic.herokuapp.com/documents/?transaction=<transaction_id>  
  to return documents for a specified transaction. 

Note: the access token automatically expires after 5 mins after which you can refresh the access token at the endpoint :http://sodiq-dukkainic.herokuapp.com/login-auth/refresh/
by providing the provided refresh token at login.

## Other than Swagger

Even though swagger doc is really a nice ui feature you can ofcourse and most eventually will access this api from some different end point, in any case just follow the standard http header requests using jwt bearer token, register a new user in our data base on the port:http://sodiq-dukkainic.herokuapp.com/register/ then login and get access token on the port :http://sodiq-dukkainic.herokuapp.com/login-auth/. Get all documents at :http://sodiq-dukkainic.herokuapp.com/documents/ and filter specific transaction documents on :http://sodiq-dukkainic.herokuapp.com/documents/<transaction-id>/ and see all documents nicely grouped by transactions at :http://sodiq-dukkainic.herokuapp.com/transactions/

# Running 

This app is pushed to :https://github.com/mallamsiddiq/StayQrious and hosted on heroku on port :http://sodiq-dukkainic.herokuapp.com/  . you can run locally just follow the following steps:

In you cli run 

** git clone https://github.com/SODIQ-STAYQRIOUS/sodiq-dukkainc.git



To have the app locally on your machine.


## With docker :

If docker and docker-compose is installed right inside the app’s root directory kidly run

** docker-compose up

** docker-compose run

And boom!! Your app is running locally on port :8000


## Without docker:

If docker is not installed relax you’re still good to go. Inside the root directory again run (with python and pip installed):

**  pip install -r requirements.txt

**  python manage.py migrate

**  python manage.py runserver

And again boom!! Your app is running locally on port :8000

And navigating locally is only different from the hosted one by the port url, change 'sodiq-dukkainic.herokuapp.com' to '127.0.0.1:8000'


# Limitations:

As at the time of pushing the app I'm having issues with my aws account and so uploaded files might not be saved into the bucket until later. One of the reasons why I'm turning in so late.

note: i have the the .env file here only for ease of running locally, relax!! no special info or key is exposed.

