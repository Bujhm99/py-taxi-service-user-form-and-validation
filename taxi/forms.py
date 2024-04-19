from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

from taxi.models import Car


class DriverCreationForm(UserCreationForm):
    license_number = forms.CharField(
        max_length=8,
        required=True,
        validators=[RegexValidator(
            regex=r"[A-Z]{3}\d{5}",
            message="It should has 3 serial big char and 5 digits",
        )]
    )

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = (UserCreationForm.Meta.fields
                  + ("license_number", "first_name", "last_name",))


class DriverLicenseUpdateForm(forms.ModelForm):

    license_number = forms.CharField(
        max_length=8,
        required=True,
        validators=[RegexValidator(
            regex=r"[A-Z]{3}\d{5}",
            message="It should has 3 serial big char and 5 digits",
        )]
    )

    class Meta:
        model = get_user_model()
        fields = ("license_number",)


class CarForm(forms.ModelForm):
    drivers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False)

    class Meta:
        model = Car
        fields = "__all__"
