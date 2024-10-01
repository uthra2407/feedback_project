from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = [
            'name', 'email', 'department', 'course',
            'feedback_curriculum', 'feedback_delivery',
            'feedback_methods', 'feedback_resources',
            'feedback_evaluation', 'feedback_support',
            'feedback_overall'
        ]

        widgets = {
            'feedback_curriculum': forms.Textarea(attrs={'rows': 4}),
            'feedback_delivery': forms.Textarea(attrs={'rows': 4}),
            'feedback_methods': forms.Textarea(attrs={'rows': 4}),
            'feedback_resources': forms.Textarea(attrs={'rows': 4}),
            'feedback_evaluation': forms.Textarea(attrs={'rows': 4}),
            'feedback_support': forms.Textarea(attrs={'rows': 4}),
            'feedback_overall': forms.Textarea(attrs={'rows': 4}),
        }
