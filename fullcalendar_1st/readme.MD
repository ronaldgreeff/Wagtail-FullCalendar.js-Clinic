creating a custom user model has to be the very first thing, before the rest of the database tables are built. (This is a Django limitation - see the warning at https://docs.djangoproject.com/en/1.10/topics/auth/customizing/#substituting-a-custom-user-model .)

Add users app to settings/base/installed_apps
Add AUTH_USER_MODEL = 'users.User' too
users.models - comment out Doctor and Patient classes
run makemigrations + migrate

Add scheduler app to settings
scheduler.models - comment out Appointment class
run makemigrations + migrate

users.models - comment back Doctor & Patient classes
run makemigrations + migrate

scheduler.models - comment back Appointment class
run makemigrations + migrate

-- migration files saved to /Temp