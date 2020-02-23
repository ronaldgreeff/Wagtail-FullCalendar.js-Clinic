creating a custom user model has to be the very first thing, before the rest of the database tables are built. (This is a Django limitation - see the warning at https://docs.djangoproject.com/en/1.10/topics/auth/customizing/#substituting-a-custom-user-model .)

Migrate myusers app before scheduler

myusers.models - comment out Doctor and Patient classes
scheduler.models - comment out Appointment class
- also from scheduler/ wagtail_hooks, admin


Add myusers app to settings/base/installed_apps
Add AUTH_USER_MODEL = 'myusers.User' too

run makemigrations + migrate

Add scheduler app to settings
run makemigrations + migrate

myusers.models - comment back Doctor & Patient classes
run makemigrations + migrate

scheduler.models - comment back Appointment class
run makemigrations + migrate

-- migration files saved to /Temp