from django.forms import ModelForm
from main.models import UserInfo


class UserEditForm(ModelForm):

    class Meta:
        model = UserInfo
        fields = ['FirstName', 'LastName', 'Country' , 'City', 'PostalCode', 'Address', 'HouseNum', 'MobilePhone', 'Email', 'SSN']
