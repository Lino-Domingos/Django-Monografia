from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": 'Username',
                "class": "form-control",
                "font-family": 'Times New Roman',
            }
        ))
    
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        )
    )

    