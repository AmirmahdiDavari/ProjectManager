from django import forms
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime

from AddUser.admin import _
from .models import Project


class TestForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'date', 'date_time')

    def __init__(self, *args, **kwargs):
        super(TestForm, self).__init__(*args, **kwargs)
        self.fields['date'] = JalaliDateField(label=_('date'),  # date format is  "yyyy-mm-dd"
                                              widget=AdminJalaliDateWidget  # optional, to use default datepicker
                                              )

        # you can added a "class" to this field for use your datepicker!
        # self.fields['date'].widget.attrs.update({'class': 'jalali_date-date'})

        self.fields['date_time'] = SplitJalaliDateTimeField(label=_('date time'),
                                                            widget=AdminSplitJalaliDateTime
                                                            )
