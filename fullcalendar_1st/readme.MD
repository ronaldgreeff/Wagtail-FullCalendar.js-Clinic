To avoid circular import headaches when running for the first time:
A custom user model has to be the very first thing, before the rest of the database tables are built. (This is a Django limitation - see the warning at https://docs.djangoproject.com/en/1.10/topics/auth/customizing/#substituting-a-custom-user-model .)


# STEP1:

## (make sure there's no existing database)

## in fullcalendar/settings/base.py, comment out these lines:

    'myusers',
    'scheduler',
	AUTH_USER_MODEL = 'myusers.User'


## from myusers.models, comment out Doctor.services:

	class Doctor(models.Model):
	    user = models.OneToOneField(User, on_delete='CASCADE', primary_key=True)
	    * services = models.ManyToManyField('scheduler.Service') <- this line


## from models.scheduler, comment out Appointment class:

	class Appointment(TimeStampedModel):
	    service = models.ForeignKey(Service, on_delete='CASCADE', null=True)
	    doctor = models.OneToOneField(Doctor, on_delete='CASCADE', null=False)
	    patient = models.OneToOneField(Patient, on_delete='CASCADE', null=False)
	    start = models.DateTimeField()
	    end = models.DateTimeField()
	    def __str__(self):
	        return '({0}) {1} {2} - {3}'.format(
	            self.doctor, self.service, self.start, self.end)


## comment out everything in scheduler/wagtail_hooks.py

## then run makemigrations + migrate


# STEP 2:

## from settings/base.py, uncomment

    'myusers',
    AUTH_USER_MODEL = 'myusers.User'

## then run makemigrations + migrate


# STEP 3:

## from myuser.models, uncomment Doctor.servives
## from scheduler.models, uncomment the Appointment class
## then run makemigrations + migrate


# STEP 4

## create superuser
## uncomment everything from wagtail_hooks.py