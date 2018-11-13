from django import forms
from django.forms import BaseFormSet
from django.forms import formset_factory

class BaseReceiptFormSet(BaseFormSet):
    def clean(self):
        """Checks that total cost does not exceed 100"""
        if any(self.errors):
            # Don't bother validating the formset unless each form is valid on its own
            return
        total = 0
        for form in self.forms:
            cost = form.cleaned_data['cost']
            total += cost
            
        if total > 100:
            raise forms.ValidationError("Total cost can not exceed 100")


class ReceiptForm(forms.Form):
    item = forms.CharField()
    cost = forms.DecimalField()


ReceiptFormSet = formset_factory(ReceiptForm, formset=BaseReceiptFormSet, extra=3)


