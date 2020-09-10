#Wagtail + FullCalendar.js
I was taking a look at FullCalendar.js when I thought it would be cool to build a package that a clinic could use to manage their schedule as well as content (through wagtail).

It seemed a bit useless without some sort of user management (myusers), so added that. Then I integrated those components into the Wagtail dashboard.

I added an enquiry form in the form of an include (so that it can easily be placed anywhere) and a simple process behind that which allows an admin to convert an enquiry into a patient.

It's a blue print that covers the basics a normal clinic might require (managing content, users, patients, a schedule and patient flow), which can be maintained and extended with ease.

#Getting it running

There is a circular dependency between scheduler and myusers, so at initial migrations you need to do the following:

- in /settings/base.py, comment out these 3 lines:

  'myusers',
  'scheduler',
	AUTH_USER_MODEL = 'myusers.User'

- in scheduler.models comment out lines as specified in the file

- comment out everything in wagtail_hooks

- run makemigrations

- uncomment the lines above again, re-run makemigrations + migrate

- create superuser, etc.

*To avoid circular import headaches when running for the first time:
A custom user model has to be the very first thing, before the rest of the database tables are built. (This is a Django limitation - see the warning at https://docs.djangoproject.com/en/1.10/topics/auth/customizing/#substituting-a-custom-user-model).*
