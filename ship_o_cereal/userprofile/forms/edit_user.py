from django.forms import ModelForm
from main.models import UserInfo, UserImage


class UserEditForm(ModelForm):

    class Meta:
        model = UserInfo
        fields = ['FirstName', 'LastName', 'Country' , 'City', 'PostalCode', 'Address', 'HouseNum', 'MobilePhone', 'Email', 'SSN']

class ChangeImage(ModelForm):

    class Meta:
        model = UserImage
        fields = ['Image']