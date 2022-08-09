from django.shortcuts import render, HttpResponse

# Create your views here.


def main(request):
    return render(request, 'main/index.html')

def test(request):
    return render(request, 'main/test.html')
