from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from .models import Service

# https://docs.wagtail.io/en/v2.7.1/reference/contrib/modeladmin/primer.html#changing-what-appears-in-the-listing

class ServiceAdmin(ModelAdmin):
    model = Service
    menu_label = 'Services' # ditch this to use verbose_name_plural from model
    menu_icon = 'pilcrow' # change as required
    menu_order = 400 # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('name', 'duration')
    list_filter = ('name',)
    search_fields = ('name',)

# Now you just need to register your customised ModelAdmin class with Wagtail
modeladmin_register(ServiceAdmin)


# https://docs.wagtail.io/en/v2.7.1/reference/hooks.html
from django.utils.safestring import mark_safe

from wagtail.core import hooks

class WelcomePanel:
    order = 50

    def render(self):
        return mark_safe("""
        <section class="panel summary nice-padding">
          <h3>No, but seriously -- welcome to the admin homepage.</h3>
        </section>
        """)

@hooks.register('construct_homepage_panels')
def add_another_welcome_panel(request, panels):
    panels.append(WelcomePanel())