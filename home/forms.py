from django import forms


class ContactForm(forms.Form):
    """Contact form for home page"""

    name = forms.CharField(label='Votre Nom')
    email = forms.EmailField(label='Votre Email')
    subject = forms.CharField(label='Sujet')
    message = forms.CharField(
        label='Votre Message',
        widget=forms.Textarea(
            attrs={
                "rows": 10,
            },
        ),
    )
