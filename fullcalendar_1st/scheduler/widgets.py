from django.forms import DateTimeInput

class XDSoftDateTimePickerInput(DateTimeInput):
    template_name = 'widgets/xdsoft_datetimepicker.html'

    def get_context(self, name, value, attrs):
        datetimepicker_id = 'datetimepciker_{name}'.format(name=name)
        if attrs is None:
            attr = dict()
        attrs['data-target'] = '#id'.format()