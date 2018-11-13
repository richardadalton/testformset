from django.test import TestCase
from .forms import ReceiptFormSet

# Create your tests here.
class TestFormset(TestCase):
    
    def test_receipt_less_than_100_valid(self):
        formset = ReceiptFormSet({
            'form-INITIAL_FORMS': '0',
            'form-TOTAL_FORMS': '3',
            'form-0-item': 'Bread',
            'form-0-cost': 35,
            'form-1-item': 'Mild',
            'form-1-cost': 35,
            'form-2-item': 'Jam',
            'form-2-cost': 10
        })
        self.assertTrue(formset.is_valid())
        
        
    def test_receipt_more_than_100_invalid(self):
        formset = ReceiptFormSet({
            'form-INITIAL_FORMS': '0',
            'form-TOTAL_FORMS': '3',
            'form-0-item': 'Bread',
            'form-0-cost': 35,
            'form-1-item': 'Mild',
            'form-1-cost': 35,
            'form-2-item': 'Jam',
            'form-2-cost': 35
        })
        self.assertFalse(formset.is_valid())