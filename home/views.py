from django.shortcuts import render, HttpResponse
from .forms import ReceiptFormSet

# Create your views here.
def get_index(request):
    if request.method=="POST":
        formset=ReceiptFormSet(request.POST)
        if formset.is_valid():
            for receipt in formset:
                cd = receipt.cleaned_data            
                print(cd.get('item'))
            return HttpResponse("Pass")
        else:
            return HttpResponse("Fail")
    else:
        formset = ReceiptFormSet()
        return render(request, "home/index.html", { 'formset': formset })