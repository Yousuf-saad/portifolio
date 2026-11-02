
from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactMessage
        fields = [
            "name",
            "email",
            "subject",
            "message",
        ]

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Your full name",
                "autocomplete": "name",
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "you@example.com",
                "autocomplete": "email",
            }),
            "subject": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "What is this about?",
            }),
            "message": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Write your message...",
                "rows": 5,
            }),
        }

    def clean_message(self):
        message = self.cleaned_data["message"].strip()

        if len(message) < 10:
            raise forms.ValidationError(
                "Please enter at least 10 characters."
            )

        return message
